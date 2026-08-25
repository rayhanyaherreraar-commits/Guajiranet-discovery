# Índice del discovery GuajiraNet

Última medición consolidada: **2026-08-24** (solo lectura).  
Copia original del backup: `archivo_guajiranet_discovery_docs_backup.zip`.

## Cómo leer esto

1. `00_contexto_maestro.md` — panorama, modelo actual, reglas de trabajo.
2. `11_model_audit.md` — modelo Silver propuesto (dims, facts, bridges, riesgos).
3. `12_final_model_validation.md` — cinco validaciones; discovery **cerrado** para el Silver acordado.
4. `13_cutover_silver_plan.md` — plan de reemplazo geo + facts (no ejecutado).
5. Informes 01–10 — evidencia de tablas y cruces.
6. `evidencia/` — JSON crudo de las corridas.

No usar el catálogo automático por nombres (`output/mapa_capacidades.json`) para modelar.

## Documentos (backup → repo)

| Archivo en el zip | Archivo en el repo |
|---|---|
| `GUAJIRANET_CONTEXTO_MAESTRO_V2(2).md` | `00_contexto_maestro.md` |
| `GUAJIRANET_CONTEXTO_MAESTRO(2).md` | `00_contexto_maestro_v1.md` |
| `relacion_matercerosuc_materceros_nit.md` | `01_relacion_matercerosuc_materceros.md` |
| `relacion_matercerosuc_materceros_nit(1).json` | `evidencia/relacion_matercerosuc_materceros.json` |
| `analisis_matercerosuc.json` | `evidencia/analisis_matercerosuc.json` |
| `lookup_idcontrato.md` | `02_lookup_idcontrato.md` |
| `lookup_idcliente.md` | `03_lookup_idcliente.md` |
| `lookup_plan_id.md` | `04_lookup_plan_id.md` |
| `lookup_matercerosuc_maperfilcartera_idperfilcartera.md` | `05_lookup_perfil_cartera.md` |
| `analisis_fecharetiroisp.md` | `06_fecharetiroisp.md` |
| `cruce_idperfilcartera_fecharetiroisp.md` | `07_cruce_perfil_retiro.md` |
| `analisis_tmjsoncontract.md` | `08_tmjsoncontract.md` |
| `analisis_tmjsonplan_server_tipo_P.md` | `09_tmjsonplan.md` |
| `11_idcliente_mismatch.md` | `10_idcliente_mismatch.md` |
| `fact_cartera_pagos_audit.json` | `evidencia/fact_cartera_pagos_audit.json` |
| `model_audit.md` | `11_model_audit.md` |
| `final_model_validation.md` | `12_final_model_validation.md` |
| `cutover_silver_plan.md` | `13_cutover_silver_plan.md` |

## Scripts para repetir mediciones

Python (requiere `.env`):

```bash
python main.py --mode table --table matercerosuc
python main.py --mode audit --audit all
```

SQL en `sql/auditoria/`:

| Script | Tema |
|---|---|
| `01_cliente_sucursal.sql` | nit, sucursal, perfil |
| `02_contratos_planes.sql` | contrato, UUID, plan P |
| `03_retiro_perfil.sql` | `fecharetiroisp` |
| `04_cartera_pagos.sql` | L.1 / L.2 |
| `05_validacion_modelo.sql` | 5 puntos del cierre |
| `06_cutover_gold.sql` | `pg_get_viewdef` (pre-DROP) |

## Hallazgos que no se deben perder

- Silver actual = facturación ERP + recorte de cartera. **No** es Cliente 360 ISP.
- `tbl_dim_servicio` = SKU `maproductos`, **no** plan ISP (`tmjsonplan_server` tipo P).
- Persona = `materceros.nit`. Sucursal = `(nit, idsuc)` en `matercerosuc`.
- Contrato = `tmjsoncontract.idcontrato`. Plan = `datajson.plan_id` tipo P (cobertura 100% de 109 planes usados).
- Factura **no** tiene FK a contrato/plan; no unir facturas históricas al contrato vigente de la sucursal.
- `seller_id` / `neighborhood_id` JSON **no** cruzan a `mavendedores` / `mabarrio`.
- `idgenero` vacío. CRM (`trcrmoportunidad`) no es fecha de vinculación ISP.
- Motivo de retiro: `maipsmotivocancelo` = 0 filas.
- Gold (5 vistas) lee solo `tbl_fact_facturacion`. Cutover de nombres iguales implica ventana con Gold caído.

## Qué no estaba en el zip

Estos artefactos se mencionan en los informes y **no** venían en el backup. Hay que regenerarlos contra Aurora o el repo Hop si se necesitan:

- `output/catalogo_tablas.json`, `catalogo_columnas.json`, `perfil_columnas.json`, `relaciones_candidatas.json`, `mapa_capacidades.json`, `resumen_discovery.md`
- `discovery/model_audit.json`, `cutover_silver_plan.json`
- `sql/silver/*.sql` y workflows Apache Hop (`wf_actualizacion_silver*`) — otro repositorio ETL
- `07_drop_obsolete.sql` — **no ejecutar completo** (CASCADE rompe Gold)

## Siguiente paso operativo

El discovery del Silver acordado está **cerrado** (`12_final_model_validation.md` sección E).  
El trabajo siguiente no es más inventario: es implementación Hop/DDL **fuera de este repo** según `11` y `13`, sin ejecutar DROP hasta capturar `pg_get_viewdef`.
