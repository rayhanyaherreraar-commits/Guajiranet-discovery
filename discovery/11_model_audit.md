# Auditoría definitiva del modelo GuajiraNet (pre-Silver Hop)

- Alcance: **solo lectura**. No se modificó Bronze, Silver, Gold ni workflows.
- Significado de campos: **no inferido**. Textos (`denominacion`, `name`, `categoria` ERP) se reportan como valores almacenados.
- Método: `information_schema`, conteos/unicidad en tablas **nombradas**, evidencia en `output/`. No se perfilaron las 829 tablas.
- Medición: 2026-08-24.

## Hallazgo rector

El Silver actual **no es un modelo Cliente 360 de ISP**. Es un estrella de **facturación ERP + un recorte de cartera**.

| objeto | filas | grano observado |
|---|---:|---|
| `silver_guajiranet.tbl_dim_cliente` | 15 389 | **sucursal** `(nit, idsuc)` = `matercerosuc` |
| `tbl_dim_servicio` | 877 | **SKU ERP** `maproductos.idproducto`. **No** es `tmjsonplan_server` |
| `tbl_dim_geografia` | 234 | barrio (229 combinaciones dpto+mun+barrio) |
| `tbl_dim_documento` | 91 | tipo de documento |
| `tbl_dim_tiempo` | 5 844 | día |
| `tbl_fact_facturacion` | 214 837 | **línea** = `trfacturasdet` (igualdad 214 837=214 837) |
| `tbl_fact_cartera` | 15 857 | ítem AR; **≠** `tmcartera` (122 050) ni `stg_fact_cartera` (11 633) |

Gold (5 vistas) lee **solo** `tbl_fact_facturacion`. No hay contrato, plan ISP, retiro ni pagos. `vw_transaccionalidad_clientes` agrupa por **nit** (13 715 filas) y pierde `idsuc`.

Sirve para facturación/cobertura **ERP**. **No** sirve para 360 ISP, deserción, Mintic de plan, recaudo ni marketing hasta incorporar las fuentes de abajo.

---

## A. Dimensiones definitivas propuestas

| DIM | Acción | Grano | Fuente Bronze confirmada |
|---|---|---|---|
| **DIM_TIEMPO** | Conservar | 1 día | `tbl_dim_tiempo` |
| **DIM_PERSONA** | Nueva (partir cliente) | 1 `nit` | `materceros` (14 938, nit único) + `tmjsonclient` |
| **DIM_SUCURSAL** | Nueva (resto de `tbl_dim_cliente`) | 1 `(nit,idsuc)` | `matercerosuc` (15 389; NK única) |
| **DIM_CONTRATO** | Nueva | 1 UUID contrato | `tmjsoncontract.idcontrato` (10 998 únicos) |
| **DIM_PLAN** | Nueva | 1 UUID plan tipo P | `tmjsonplan_server` `tipo='P'` (282; 109 usados en contratos; cobertura 100%) |
| **DIM_PRODUCTO_ERP** | Renombrar `tbl_dim_servicio` | 1 `idproducto` | `maproductos` (877). No sustituye DIM_PLAN |
| **DIM_GEOGRAFIA** | Conservar; una sola geo | 1 barrio | `mabarrio` (245) + `madepartamentos` (40); sucursal aporta `idbarrio`,`dpto`,`mun` |
| **DIM_DOCUMENTO** | Conservar | 1 tipo doc | Silver (91) |
| **DIM_PERFIL_CARTERA** | Nueva | 1 id | `maperfilcartera` (17; p.ej. 1 Residencial, 11 Proyecto Mintic, 18 Proceso Retiro, 21 Proceso Retiro Mintic) |
| **DIM_ESTRATO** | Mini-dim o atributo | 1 código | `maestrato` (10). `matercerosuc.estrato` vacío en **14 681 / 15 389** |
| **DIM_FORMA_PAGO** | Solo si hay FACT_PAGOS | 1 forma | `maformasdepago` (83) |
| **DIM_VENDEDOR** | No crear aún | — | `mavendedores` = **1 fila** |

**No crear:** DIM categoría/tecnología/cobertura de plan (no hay clave JSON); DIM motivo retiro (`maipsmotivocancelo` = 0); DIM demografía; DIM campaña hasta investigación L.

---

## B. Facts definitivas propuestas

| FACT | Acción | ¿Hop ahora? |
|---|---|---|
| **FACT_FACTURACION** | Conservar grano línea; añadir SK sucursal/persona; contrato/plan **nullable** si no hay join | Sí |
| **FACT_CARTERA** | Reconstruir y **declarar** snapshot vs libro | Sí, tras L.1 |
| **FACT_PAGOS** | Nueva condicional | Solo si L.2 aprueba fuente |
| **FACT_CONTRATO** | No | El contrato vigente es **dim**; no hay eventos de cambio |

Sin fact de instalación, activación, cambio de plan ni mudanza: no hay tablas de evento (`trlogmudanza` = 0).

---

## C. Bridges necesarias

| Bridge | Grano | Fuente | Nota |
|---|---|---|---|
| **BRG_PERSONA_UUID** | `idcliente` UUID | `materceros.idcliente` + `tmjsonclient.idcliente` | Cobertura contratos 99,9534%; 5 UUID ausentes; 5 UUID con 2 nit |
| **BRG_SUCURSAL_CONTRATO** | `(nit,idsuc,idcontrato)` | `matercerosuc.idcontrato` | Ambas 10 466; solo suc 469; solo JSON 532; cobertura suc 95,711%; 2 UUID duplicados en suc |
| **BRG_CONTRATO_PLAN** | contrato → plan vigente | `tmjsoncontract.datajson->>'plan_id'` | N:1 actual; **sin histórico** |

---

## D. Granularidad de cada FACT

### FACT_FACTURACION (existe)

- **Grano:** 1 línea `trfacturasdet` `(idsuc, prefijo, numero, pos)`.
- Cabecera `trfacturas`: 212 763; NK `(idsuc,prefijo,numero)` única; `fecha` 2021-12-28 … 2026-08-22; `anulado` N=212 584 / S=179.
- Líneas/factura: min 1, max 28, avg 1,0099.
- Silver = det; 0 huérfanos a dims actuales.
- `sk_cliente` distinct 13 974 &lt; 15 389 sucursales.
- `sk_servicio` = producto ERP de la línea, **no** plan ISP.

### FACT_CARTERA (existe, no equivale al libro)

- 15 857 filas; `(sk_cliente,cuenta,ref_doc,ref_num)` distinct 15 178 (no único).
- 6 073 clientes; 733 `sk_tiempo`; `fecha_vencimiento` 2021-11-11 … 2026-11-01.
- STG 11 633 ≠ TBL 15 857.
- `tmcartera` 122 050; 610 fechas; columnas `saldo,debito,credito,fvence,dias,rango1-6,idformapago,idvendedor,transaccion,interes`.
- `vsaldoscartera` 6 428; `vmovcartera` 11 708.
- `maedadescartera`: SIN VENCER, 0-30, 31-60, 61-90, MAS DE 90.
- **Antes de Hop:** elegir (1) snapshot abiertos o (2) libro `tmcartera`.

### FACT_PAGOS (no existe)

| fuente | filas | columnas relevantes (nombres, no negocio) |
|---|---:|---|
| `vpagodiasfactura` | 183 646 | factura + `rc_idsuc/prefijo/numero/fecha` + `pagorc` + `carteraaplicado` + `idformapago` |
| `vfacturas_abono` | 173 651 | `nit,total,abono,saldo,fecha,fvence` |
| `trpagodigital` | 55 529 | `foperacion,total,rec_*,codigo_respuesta,numero_autorizacion` |
| `trformaspago` | 197 073 | `valor,plazo,cuota,capital,saldo,fvence` — **parece plazo de factura, no recaudo** |

Grano **si** se valida `vpagodiasfactura`: 1 aplicación de recaudo a 1 factura.

---

## E. Fuente Bronze de cada objeto

| Objeto | Fuente | No es |
|---|---|---|
| Persona | `materceros` | `idcliente` = `nit` (0 igualdades) |
| Sucursal, contactos, geo, perfil, `fecharetiroisp`, `finiciopermanencia`, `idcontrato`, `activo` | `matercerosuc` | — |
| UUID ISP | `tmjsonclient` (`datajson.id` = `idcliente`) | columna `nit` en esa tabla |
| Contrato / state / start_date / address_* / lat-long / ont_* / olt_* / plan_id | `tmjsoncontract.datajson` | — |
| Plan / price / ceil_*_kbps / cir / name | `tmjsonplan_server` tipo P | `maproductos` (0 overlap de UUID) |
| Perfil | `maperfilcartera` + `idperfilcartera` | — |
| Factura | `trfacturas` + `trfacturasdet` | — |
| Cartera libro | `tmcartera` | el fact Silver actual |
| Geo catálogo | `mabarrio`, `madepartamentos` | repetir textos en 3 dims |

---

## F. Llaves naturales

| Entidad | NK |
|---|---|
| Persona | `nit` |
| Sucursal | `(nit, idsuc)` |
| UUID cliente | `idcliente` (36) |
| Contrato | `idcontrato` = `datajson.id` |
| Plan | `datajson.id` tipo P |
| Producto ERP | `idproducto` |
| Factura | `(idsuc, prefijo, numero)` |
| Línea | `(idsuc, prefijo, numero, pos)` |
| Barrio | `idbarrio` |
| Perfil | `maperfilcartera.id` |

---

## G. Llaves sustitutas propuestas

| SK | Sobre |
|---|---|
| `sk_persona` | `nit` |
| `sk_sucursal` | `(nit,idsuc)` — **reemplaza** el actual `sk_cliente` |
| `sk_contrato` | `idcontrato` |
| `sk_plan` | UUID plan |
| `sk_producto` | `idproducto` (hoy `sk_servicio`) |
| `sk_geografia` / `sk_tiempo` / `sk_documento` | conservar |
| `sk_perfil_cartera` | id perfil |
| `sk_fact_facturacion` | conservar; FKs nuevas nullable |
| `sk_fact_pago` | nuevo si hay fact |

No reutilizar el nombre `sk_cliente` para persona.

---

## H. Riesgos de duplicación

1. **Persona vs sucursal vs dim cliente:** 14 938 nit / 15 389 sucursales. Gold por nit fusiona sucursales.
2. **Contrato vs sucursal:** no 1:1. 11 filas `idsuc=0` con `tmjsoncontract.idcliente` ≠ `materceros.idcliente`.
3. **Plan ISP vs SKU factura:** 0 overlap UUID. Gold capilaridad usa `tbl_dim_servicio.categoria` (MATERIALES 225, EQUIPOS 208, RESIDENCIAL 75…).
4. **Geo triple:** sucursal vs JSON contrato vs dim 234 vs `mabarrio` 245. Una DIM_GEOGRAFIA.
5. **Estados:** `activo`, `idperfilcartera`, `fecharetiroisp`, `datajson.state` (`enabled` 8 637 / `disabled` 2 361). No son la misma columna.
6. **Cartera:** stg 11 633 / tbl 15 857 / `tmcartera` 122 050.
7. **Pago:** cuatro tablas; una fact sin validar duplica recaudo.

---

## I. Datos confirmados

Sucursal/persona: nit, razonsocial, idsuc, direccion1/2, dpto/departamento, mun/ciudad, idbarrio, telefonos, movil, email, emailfe, coordenada (7 577 vacías de 15 389), estrato (poco poblado), idcontrato, idperfilcartera + anterior, activo, finiciopermanencia, fecharetiroisp, descuento, idconvenio, idvendedor.

JSON cliente (14 614, mismas claves): id, name, email, phone, phone_mobile, national_identification_number, taxpayer_identification_number, custom_id, kind_person, address, city, street, state, latitude, longitude, neighborhood_id, seller_id, vat_condition, zone_name, created_at, updated_at. Clave `password` (no llevar a Silver analítico).

Contrato JSON (60 claves, 10 998): `start_date`, `created_at`, `updated_at`, `state`, `plan_id`, `address_*`, lat/long, `ont_*`, `olt_id`, `interface_gpon`, `mac_address`, `coverage_id` (51 no null).

Plan tipo P (11 claves, 282): id, name, public_id, ceil_down_kbps, ceil_up_kbps, cir, price (string), frequency_in_months=1, contracts_count, created_at, updated_at.

Facturación/cartera/geo: volúmenes en D–E.

---

## J. Datos ambiguos

- `fecharetiroisp`: 2 349 no null; 13 fechas 2025-11-01…2026-08-01; **todas** `activo=S`; 1 089 perfil 18; 190 perfil 21; **0** perfil 22 con fecha; 833 perfil 11.
- `state` ≠ perfil retiro ≠ `activo`.
- `start_date` existe; **no** se llama instalación ni activación.
- `finiciopermanencia` vs primera factura vs `start_date`: cuatro relojes, ninguna “vinculación” certificada.
- `categoria` en dim servicio = familia ERP.
- Mintic: perfil 11 **y/o** subcadena en `name` (4 planes). Sin flag.
- Residencial/comercial/empresarial/dedicado: subcadena en `name` **o** perfil sucursal; pueden divergir.
- `coverage_id` casi vacío.
- `seller_id` en JSON: clave presente; cardinalidad no medida.
- `idgenero` en `materceros`/`maproductos`: no perfilado; no asumir demografía.

---

## K. Datos faltantes

| Pedido | Evidencia |
|---|---|
| Motivo de retiro | `maipsmotivocancelo` = 0 |
| Histórico plan/estado/dirección | `trlogmudanza` = 0; contrato es foto |
| Fecha instalación / activación | 0 claves con esos nombres en JSON contrato |
| Tecnología / vigencia / municipio del plan | 0 claves en tipo P |
| FACT_PAGOS Silver | no existe |
| Dim vendedor/campaña ISP | catálogo vendedor 1 fila; CRM no enlazado a contrato |
| Demografía/etnografía de clientes | sexo/etnia/nacimiento en tablas **NRH**, no en terceros ISP |

---

## L. Investigaciones que todavía son necesarias

1. Grano FACT_CARTERA: 15 857 vs filtro de `tmcartera`.
2. FACT_PAGOS: unicidad/suma `vpagodiasfactura` vs `trpagodigital` vs `vfacturas_abono`; confirmar que `trformaspago` es plazo.
3. ¿Hay `idcontrato` o plan ISP en `trfacturas`/`trfacturasdet`? En columnas listadas, `idproducto` es ERP.
4. Cardinalidad `seller_id` y `neighborhood_id` en `tmjsonclient`.
5. Valores de `idgenero` en `materceros`.
6. Homologar `mabarrio` (245) vs dim 234 vs `idbarrio` sucursal.
7. 5 UUID contrato sin `materceros`; 11 `idsuc=0` con UUID distinto.
8. `trcrmoportunidad` (8 205) vs nit: ¿altas ISP u otro proceso?
9. Parseo de `comentarios` / `details`: fuera del modelo hasta regla escrita.

---

## M. Orden exacto en Apache Hop

No ejecutar en este repo.

1. DIM_TIEMPO (existe).
2. DIM_GEOGRAFIA (`mabarrio`+`madepartamentos`); sucursal/contrato con FK, no copiar geo en 3 dims.
3. DIM_PERSONA (`materceros`) + BRG_PERSONA_UUID.
4. DIM_SUCURSAL (`matercerosuc`) + DIM_PERFIL_CARTERA + estrato.
5. DIM_PLAN (`tmjsonplan_server` tipo P).
6. DIM_CONTRATO + BRG_SUCURSAL_CONTRATO + BRG_CONTRATO_PLAN.
7. DIM_PRODUCTO_ERP (ex `tbl_dim_servicio`) + DIM_DOCUMENTO.
8. FACT_FACTURACION (mismo grano); `sk_sucursal` en lugar de `sk_cliente`; contrato/plan null si no hay join.
9. FACT_CARTERA con grano de L.1.
10. FACT_PAGOS solo si L.2 aprueba.
11. Gold: vistas sobre sucursal+contrato+plan; no agrupar 360 solo por nit; no usar SKU ERP como plan de internet.

---

## N. Tableros

### Con Silver actual

Facturación por tiempo, documento, SKU ERP, geo de la factura. Ticket y primera/última factura. “Capilaridad” **engañosa** (productos ERP).

**No:** 360 ISP, retiro, Mintic de plan, recaudo, mora completa, vendedor, campaña, demografía.

### Con el modelo propuesto (fuentes confirmadas)

| Tablero | Alcance real |
|---|---|
| Cliente 360 | Persona + sucursales + contratos + plan actual + perfil + contactos + geo + facturas. Sin histórico de plan/dir |
| Transaccionalidad | Facturas. Pagos solo si L.2. Meses pagados no sin pagos |
| Cobertura | Sucursal + contrato. `coverage_id` insuficiente |
| Facturación | Ya; mejorar FKs |
| Cartera/mora | Tras L.1; aging en Bronze |
| Retención | Parcial: `fecharetiroisp`, perfiles 18/21, `state=disabled`. Sin motivo ni fecha de activación |
| Comercial | Débil: descuento/convenio; CRM no validado |
| Demográfico | **No** |

JSON: `discovery/model_audit.json`.
