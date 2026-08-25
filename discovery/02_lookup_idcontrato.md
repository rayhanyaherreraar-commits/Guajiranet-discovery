# Lookup: `matercerosuc.idcontrato`

- Schema: `bronze_guajiranet`
- Read-only
- Columna buscada (nombre exacto): `idcontrato`
- No se asigna negocio al campo

## Origen

| métrica | valor |
|---|---:|
| filas | 15389 |
| nulos | 4452 |
| no nulos | 10937 |
| distinct no nulos | 10935 |
| único entre no nulos | no |

Duplicados en origen (2 valores, 2 filas cada uno): `8fa604c6-77d2-41fe-9109-a7160ade28f9`, `6bc212a6-40f5-4cc5-8fb7-f90895fdbac4`.

## Tablas Bronze con columna `idcontrato`

| tabla | tipo | tipo dato | nulos permitidos | pos | filas |
|---|---|---|---|---:|---:|
| matercerosuc | BASE TABLE | varchar | YES | 61 | 15389 |
| tmin_liqinteres | BASE TABLE | varchar | YES | 11 | 0 |
| tmjsoncontract | BASE TABLE | varchar | YES | 4 | 10998 |
| tndocinmobiliariadet | BASE TABLE | varchar | YES | 4 | 0 |
| trinfacturasdet | BASE TABLE | varchar | YES | 6 | 0 |
| trinliqinteres | BASE TABLE | varchar | YES | 12 | 0 |

## Medición vs `matercerosuc` (claves no nulas = 10935)

| tabla | nulos | distinct | único no nulos | cobertura claves | en ambas | solo suc | solo candidata | cardinalidad suc→cand |
|---|---:|---:|---|---:|---:|---:|---:|---|
| tmjsoncontract | 0 | 10998 | sí | **95.711%** | 10466 | 469 | 532 | N:1* |
| tmin_liqinteres | 0 | 0 | no | 0% | 0 | 10935 | 0 | n/a (vacía) |
| tndocinmobiliariadet | 0 | 0 | no | 0% | 0 | 10935 | 0 | n/a (vacía) |
| trinfacturasdet | 0 | 0 | no | 0% | 0 | 10935 | 0 | n/a (vacía) |
| trinliqinteres | 0 | 0 | no | 0% | 0 | 10935 | 0 | n/a (vacía) |

\*N:1 sobre el conjunto de `matercerosuc` porque hay 2 `idcontrato` repetidos ahí. En el cruce efectivo: 10466 filas de suc = 10466 claves = 10466 filas de `tmjsoncontract` (1:1 en la intersección). Los 2 duplicados de suc **no** están en `tmjsoncontract`.

## Candidata con datos: `tmjsoncontract`

Columnas observadas: `id` integer NOT NULL, `datajson` jsonb, `idcliente` varchar, `idcontrato` varchar.

| métrica | valor |
|---|---|
| filas | 10998 |
| `id` nulos / distinct | 0 / 10998 (único) |
| `idcontrato` nulos / distinct | 0 / 10998 (único) |
| filas suc no nulas encontradas | 10466 |
| filas suc no nulas sin match | 471 (= 469 claves + 2 repeticiones) |

Muestra de claves en suc y no en `tmjsoncontract`: `000db2be-32f6-4788-b87b-b9125bb9e1a3`, `006b79cc-4031-4774-9759-09a19e03ea8f`, `00c83a05-7cce-48bb-a6d9-c2aa266e24d4`.

## Padre/maestra observada

No hay padre **confirmado**: ninguna tabla cubre ≥99% de los `idcontrato` no nulos de `matercerosuc` con unicidad.

**Mejor candidata:** `tmjsoncontract`  
Única tabla no vacía con los mismos valores, `idcontrato` único y `id` único. Falta cobertura completa (469 claves solo en suc; 532 solo en `tmjsoncontract`).

Las otras cuatro tablas con la columna están vacías (0 filas): no pueden actuar como maestra ahora.

JSON: `output/lookup_idcontrato.json`
