# Relación dirigida: `matercerosuc` → `materceros` (nit)

- Schema: `bronze_guajiranet`
- Conexión: read-only
- No se infiere significado de campos; solo conteos y unicidad observados

## Volúmenes
- `matercerosuc` registros: **15389**
- `matercerosuc` nit distintos (no nulos): **14938**
- `matercerosuc` filas con nit nulo: **0**
- `materceros` registros: **14938**
- `materceros` nit distintos: **14938**
- `materceros` filas con nit nulo: **0**
- `nit` único en padre: **True**

## Cobertura del join
- nit del hijo que existen en el padre: **14938**
- nit del hijo que no existen en el padre: **0**
- Filas del hijo cuyo nit no está en el padre: **0**
- Cobertura: **100.0%**
- nit del padre sin filas en el hijo: **0**
- Muestra de nit ausentes en padre: (vacía)

## Cardinalidad
- Dirección hijo → padre: **N:1**
- Filas por nit en hijo: min=1, max=38, avg=1.0302
- nit con 1 fila: **14661**
- nit con 2 filas: **233**
- nit con 3+ filas: **44**

## Unicidad en hijo
- `(nit, idsuc)`: unique=True, distinct=15389/15389, nulos_en_llave=0, grupos_duplicados=0
- `(nit, id)`: unique=True, distinct=15389/15389, nulos_en_llave=0, grupos_duplicados=0

## Campos foco (hijo)
- `idcontrato` (character varying): nulos=4452, no_nulos=10937, distinct=10935; unique_no_nulos=False
  - grupos no nulos duplicados: 2
  - muestra duplicados: `[{"value": "8fa604c6-77d2-41fe-9109-a7160ade28f9", "count": 2}, {"value": "6bc212a6-40f5-4cc5-8fb7-f90895fdbac4", "count": 2}]`
- `idperfilcartera` (integer): nulos=1146, no_nulos=14243, distinct=17; unique_no_nulos=False
  - distribución: 11=5763, 1=4008, 18=2921, 21=822, 4=219, 5=113, 22=81, 9=69, 8=48, 16=45, 6=32, 10=32, 7=30, 2=24, 12=18, 0=17, 13=1
- `idperfilcartera_anterior` (integer): nulos=13039, no_nulos=2350, distinct=7; unique_no_nulos=False
  - distribución: 21=1583, 1=539, 11=201, 4=14, 9=8, 8=4, 0=1
- `fecharetiroisp` (date): nulos=13040, no_nulos=2349, distinct=13; min=2025-11-01, max=2026-08-01, filas_con_min=246, unique_no_nulos=False
  - distribución: 2026-01-02=323, 2026-03-01=317, 2026-08-01=290, 2025-11-01=246, 2026-02-01=232, 2026-07-01=215, 2025-12-01=199, 2026-06-01=182, 2026-05-01=176, 2026-04-01=163, 2026-02-02=4, 2026-04-02=1, 2026-01-03=1
- `finiciopermanencia` (date): nulos=4356, no_nulos=11033, distinct=641; min=1899-12-30, max=2026-08-22, filas_con_min=936, unique_no_nulos=False
  - grupos no nulos duplicados: 627
  - muestra duplicados: `[{"value": "1899-12-30", "count": 936}, {"value": "2025-10-31", "count": 61}, {"value": "2025-08-26", "count": 58}, {"value": "2025-10-01", "count": 55}, {"value": "2025-05-14", "count": 51}, {"value": "2025-05-15", "count": 49}, {"value": "2025-10-07", "count": 47}, {"value": "2025-10-30", "count": 44}, {"value": "2025-07-10", "count": 44}, {"value": "2025-08-27", "count": 43}]`
- `activo` (character): nulos=0, no_nulos=15389, distinct=2; unique_no_nulos=False
  - distribución: S=15371, N=18

## Co-ocurrencias observadas
- `idperfilcartera_vs_anterior`: `{"both_not_null_and_equal": 323, "both_not_null_and_different": 2027, "anterior_not_null_current_null": 0}`
- `activo_vs_fecharetiroisp_null`: `[{"activo": "N", "fecharetiroisp_is_null": true, "count": 18}, {"activo": "S", "fecharetiroisp_is_null": false, "count": 2349}, {"activo": "S", "fecharetiroisp_is_null": true, "count": 13022}]`

## Nota
Evidencia de conteo y unicidad únicamente. No se asigna negocio a los campos.
