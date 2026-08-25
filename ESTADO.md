# Estado del proyecto (post-formateo, 2026-08-24)

Este archivo es el ancla de contexto. Si se abre un chat nuevo, leer esto y `discovery/INDEX.md`.

## Qué es este repositorio

Scanner Python de **solo lectura** contra Aurora PostgreSQL (`db_bronze` / `bronze_guajiranet`) más el **archivo de discovery** que se había avanzado antes de formatear el PC.

Flujo acordado: **descubrir → validar significado → diseñar modelo → Silver/Gold → Power BI**.  
No modelar por nombres de tabla. No modificar Bronze/Silver/Gold desde aquí.

## Qué se recuperó del zip

Los 18 archivos de `guajiranet_discovery_docs_backup.zip` están en `discovery/` (nombres limpios) y la copia binaria del zip en `discovery/archivo_guajiranet_discovery_docs_backup.zip`.

El scanner en GitHub `main` no traía `scanner/targeted.py` (sí existía en `origin/feat/targeted-table-analysis`). Se restauró. Encima se reconstruyeron las auditorías dirigidas en `scanner/directed.py` y `sql/auditoria/`.

## Números de Bronze (medición 2026-08-24)

| objeto | filas / dato |
|---|---|
| Tablas Bronze (inventory inicial) | 829 tablas, 11 029 columnas, 221 relaciones candidatas por nombre |
| `materceros` | 14 938, `nit` único |
| `matercerosuc` | 15 389, NK `(nit,idsuc)` única |
| `tmjsonclient` | 14 614 |
| `tmjsoncontract` | 10 998 contratos, 10 740 `idcliente` |
| `tmjsonplan_server` tipo P | 282 planes; 109 usados; cobertura 100% |
| `trfacturas` / `trfacturasdet` | 212 763 / 214 837 |
| `tmcartera` | 122 050 |
| Silver `tbl_fact_facturacion` | 214 837 (= det) |
| Silver `tbl_fact_cartera` | 15 857 (no equivale al libro) |
| `fecharetiroisp` no nulo | 2 349; todas `activo=S` |
| `maipsmotivocancelo` | 0 |

## Modelo Silver acordado (no implementado en este repo)

**Entran:** DIM_TIEMPO, DIM_PERSONA, DIM_SUCURSAL, DIM_CONTRATO, DIM_PLAN (JSON tipo P), DIM_PRODUCTO_ERP, DIM_GEOGRAFIA (`mabarrio.idbarrio`), DIM_DOCUMENTO, DIM_PERFIL_CARTERA, FACT_FACTURACION (línea), FACT_CARTERA (snapshot latest-open), FACT_PAGO_APLICACION, FACT_PAGO_PASARELA. Bridges UUID, sucursal-contrato, contrato-plan.

**Fuera:** seller/neighborhood JSON como FK, demografía, CRM como alta ISP, join factura→plan, motivo de retiro, histórico de plan/dirección, `trformaspago` como recaudo.

## Conexión

Usar `.env` local (no se sube). Plantilla: `.env.example`.  
Host, base, usuario y esquema están documentados en `discovery/00_contexto_maestro.md`. La contraseña **no** se documenta ni se versiona.

## GitHub

Remote: `https://github.com/rayhanyaherreraar-commits/Guajiranet-discovery.git`  
Rama de trabajo: `main`.
