# Validación final del modelo GuajiraNet (5 puntos)

- Solo lectura. Bronze, Silver, Gold y workflows **no** se modificaron.
- Significado de campos **no** inferido. Clasificación al final de cada punto.

---

## 1. `seller_id` y `neighborhood_id` (`tmjsonclient.datajson`)

**Filas:** 14 614. Ambas claves están en **todas** las filas.

### seller_id
| | |
|---|---:|
| jsonb null | 10 097 |
| string no vacío | 4 517 |
| distinct no nulos | **17** (UUID) |
| match `mavendedores.idvendedor` | **0** |
| match `mavendedores.codvendedor` | **0** |

`mavendedores` tiene 1 fila y PK numérica `idvendedor`, no UUID. Otras tablas `*vendedor*` no se usaron como catálogo UUID.

### neighborhood_id
| | |
|---|---:|
| jsonb null | 10 739 |
| distinct no nulos | **92** (UUID) |
| match `mabarrio.idbarrio` | **0** |
| igualdad `matercerosuc.idbarrio` vía nit | **0** (2 113 ambos llenos y distintos) |

`mabarrio.idbarrio` es entero (245). El JSON usa otro espacio de identificadores.

**Clasificación: NO UTILIZABLE** para relaciones Silver (dim vendedor / dim barrio JSON). Pueden guardarse como atributos crudos en persona JSON, sin FK.

---

## 2. `materceros.idgenero`

| | |
|---|---:|
| filas | 14 938 |
| NULL | 14 916 |
| `''` (vacío) | 22 |
| distinct no nulos | 1 (`''`) |
| tipo | `character varying` |
| tabla `magenero` | **no existe** |

No hay catálogo. No hay valores de código. **No** se afirma que sea género: la columna existe y está vacía.

**Clasificación: NO UTILIZABLE**

---

## 3. Geografía

| fuente | hecho medido |
|---|---|
| `mabarrio` | 245 filas; `idbarrio` único; NK observada `idbarrio` (también hay `dpto`,`mun`,`nombrebarrio`) |
| `madepartamentos` | 40 filas; `dpto` + texto `departamento` |
| `matercerosuc.idbarrio` | 12 517 no nulos / 15 389; **12 515** cruzan a `mabarrio`; **2** códigos huérfanos; 233 `idbarrio` distintos |
| `matercerosuc.dpto` | 21 códigos; **21/21** existen en `madepartamentos` |
| textos sucursal | `dpto='44'` tiene **8** textos de departamento distintos (14 725 filas). No usar texto como NK |
| JSON contrato | `address_city` 60 / `address_state` 9; lat/lon sin vacíos en 10 998. **No** es el catálogo de barrio |
| JSON cliente `neighborhood_id` | UUID; 0 match a `mabarrio` |
| `tbl_dim_geografia` Silver | 234 filas (cerca de 245; no es la fuente canónica Bronze) |

**Fuente canónica DIM_GEOGRAFIA:** `mabarrio` (códigos `dpto`/`mun` desde `madepartamentos` + `mabarrio`).  
**NK definitiva:** `idbarrio`.  
Sucursal: FK `idbarrio` (12 515/12 517). Contrato: lat/lon y `address_*` como **atributos de contrato**, no como dim paralela.

**Clasificación: CONFIRMADO**

---

## 4. `trcrmoportunidad` (vinculación)

| | |
|---|---:|
| filas | 8 205; `anulado='N'` 8 205 |
| `fecha` | 2024-09-18 … 2026-07-18 (0 nulos) |
| NIT distintos | 8 026 (1 null) |
| NIT en `materceros` | 8 076 / 8 205 |
| match sucursal `(nit,idsucursal)` | 8 041 |
| NIT de opp con contrato JSON | 7 403 |
| `idcampana=0` | 5 005 |
| `tipo` (muestra) | `Oportunidad` |
| `start_date` contratos JSON | desde **2019-02-14** |

Hay solape de NIT con terceros/contratos, pero el CRM **empieza en 2024-09** y la base de contratos en **2019**. Columnas: pipeline (`idetapa`,`estado`,`asunto`,`ingreso`,`idvendedor`,`fecha_cierre`). **No** hay `idcontrato` ni `plan_id`.

No es el reloj de alta ISP de toda la base. No sustituye `start_date` / `finiciopermanencia` / primera factura.

**Clasificación: NO UTILIZABLE** como vinculación ISP. **CANDIDATO** solo si más adelante se quiere un fact CRM aparte (fuera del núcleo Silver).

---

## 5. Facturación ↔ contrato / plan ISP

En `trfacturas` / `trfacturasdet`:
- columnas `*contrato*` / `*plan*` / `idcliente` UUID: **no** hay `idcontrato` ni `plan_id` poblados (`doccontrato` lleno = **0**).
- `trfacturasdet.idproducto`: 193 distinct; **0** igualdades con `tmjsonplan_server.datajson.id`.

Cruce **inferido** factura `(nit,sucursal)` → `matercerosuc.idcontrato`: 172 827 / 212 763 cabeceras caen en sucursal con contrato; 0 cabeceras sin sucursal en el join `nit+sucursal`. Eso asigna el **contrato vigente de la sucursal** a **todas** las facturas históricas de esa sucursal. No es una FK de la factura. Distorsiona plan/tiempo.

**No** unir por nombre de producto/plan.

**Clasificación: NO UTILIZABLE** como relación confiable factura→contrato/plan. FACT_FACTURACION queda con sucursal/persona/producto ERP; `sk_contrato`/`sk_plan` **null**.

---

## Resumen de clasificación

| # | Tema | Estado |
|---|---|---|
| 1 | seller_id / neighborhood_id | **NO UTILIZABLE** (FK) |
| 2 | idgenero | **NO UTILIZABLE** |
| 3 | DIM_GEOGRAFIA | **CONFIRMADO** (`mabarrio.idbarrio`) |
| 4 | CRM = vinculación ISP | **NO UTILIZABLE** |
| 5 | Factura → contrato/plan ISP | **NO UTILIZABLE** |

Nada de estos cinco queda en **FALTA INVESTIGAR** para el Silver acordado.

---

## A. Qué entra en Silver

- DIM_TIEMPO, DIM_PERSONA (`materceros` + UUID), DIM_SUCURSAL, DIM_CONTRATO, DIM_PLAN (JSON tipo P), DIM_PRODUCTO_ERP, DIM_GEOGRAFIA (`mabarrio`), DIM_DOCUMENTO, DIM_PERFIL_CARTERA.
- FACT_FACTURACION (línea), FACT_CARTERA (snapshot latest-open `tmcartera`), FACT_PAGO_APLICACION (`vpagodiasfactura` DISTINCT), FACT_PAGO_PASARELA (`trpagodigital`).
- Atributos de sucursal: contactos, `idbarrio`, perfil, `fecharetiroisp`, `activo`.
- Atributos de contrato: `state`, `start_date`, ONT/OLT, lat/lon, `address_*`.

## B. Qué queda fuera

- seller_id / neighborhood_id como dims.
- idgenero / demografía.
- CRM como fecha de vinculación.
- Join factura→plan ISP.
- Categoría/tecnología de plan, motivo de retiro, histórico de plan/dirección.
- `trformaspago` como recaudo; libro de movimientos desde `tmcartera`.
- `tbl_dim_servicio` como plan ISP; `tbl_fact_cartera` actual (grano).

## C. BRG realmente necesarias

1. **BRG_PERSONA_UUID** — `materceros.idcliente` ∪ `tmjsonclient.idcliente`
2. **BRG_SUCURSAL_CONTRATO** — `matercerosuc.idcontrato`
3. **BRG_CONTRATO_PLAN** — `tmjsoncontract.datajson.plan_id`

No: BRG factura–contrato, BRG seller, BRG neighborhood JSON.

## D. Duplicación que permanece

- Persona vs sucursal vs agregados Gold por nit.
- Textos depto/ciudad vs códigos `dpto`/`mun`/`idbarrio`.
- JSON `neighborhood_id` vs `mabarrio` (no unir).
- Si alguien pega factura al `idcontrato` vigente de sucursal: facturas viejas con plan actual.

## E. Cierre

**DISCOVERY COMPLETO** para construir el Silver definido en A–C.

No queda investigación **crítica** bloqueante. Lo excluido en B es decisión de alcance, no pendiente de evidencia.
