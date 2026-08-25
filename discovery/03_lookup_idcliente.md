# Lookup: `tmjsoncontract.idcliente`

- Schema: `bronze_guajiranet`. Read-only.
- **No se asume `idcliente = nit`.** `idcliente` es UUID (longitud 36).
- Catálogo: columna `idcliente` **o** nombre que contenga `client_id`.

## Origen

| métrica | valor |
|---|---:|
| filas | 10998 |
| nulos | 0 |
| distinct | 10740 |
| único | no (hasta 30 filas / clave) |

## Catálogo

Columnas `idcliente`: `materceros`, `tmjsonclient`, `tmjsoncontract`, `tmjsonnuplin`, `trispmensajedet`.

Columnas cuyo nombre contiene `client_id`: **ninguna**. (`datajson` de contrato tiene clave JSON `client_id`; no es columna.)

## Candidatas vs `tmjsoncontract.idcliente`

| tabla.columna | filas | distinct | único | cobertura claves | ambas | solo contrato | nit en tabla |
|---|---:|---:|---|---:|---:|---:|---|
| **tmjsonclient.idcliente** | 14614 | 14614 | sí | **100%** | 10740 | 0 | no |
| **materceros.idcliente** | 14938 | 14259 | no | **99.9534%** | 10735 | 5 | **sí** (`nit` único en la tabla) |
| tmjsonnuplin.idcliente | 252 | 1 | no | 0% | 0 | 10740 | no |
| trispmensajedet.idcliente | 0 | 0 | — | 0% | 0 | 10740 | — |

Cardinalidad contrato → `tmjsonclient`: **N:1**.  
Contrato → `materceros`: casi N:1; 5 `idcliente` con 2 `nit`; cada `nit` tiene a lo sumo 1 `idcliente`.

5 UUID de contrato ausentes en `materceros` (muestra en JSON).

`tmjsonclient`: columnas `id`, `datajson`, `idcliente`. `datajson.id` = `idcliente` en 14614/14614. Sin columna `nit`.

## Relación observada hacia NIT (igualdad de strings, no identidad de `idcliente`)

`tmjsoncontract.idcliente` comparado directo con `materceros.nit`: **0**.

Puente UUID: `tmjsoncontract.idcliente` = `materceros.idcliente` (10735/10740) → `materceros.nit` (columna aparte).

En el join `tmjsonclient` ⋈ `materceros` por `idcliente` (13895 filas):

| campo JSON de `tmjsonclient` | filas = `materceros.nit`::text |
|---|---:|
| `national_identification_number` | 13853 |
| `custom_id` | 13853 |
| `taxpayer_identification_number` | 4055 |

Subconjunto clientes de contrato (10736 filas / 10735 UUID): nin=10709, custom_id=10710, tin=1924.

Camino `idcontrato` → `matercerosuc` → `nit` → `materceros`: 10466 filas; `tmjsoncontract.idcliente` = `materceros.idcliente` en **10455**; distinto en 11.

## Padre / puente

- **Padre UUID:** `tmjsonclient.idcliente` (único, cobertura 100%). No trae `nit` como columna.
- **Puente a NIT de GuajiraNet:** `materceros.idcliente` + `materceros.nit` (cobertura 99.9534%; `nit` único en esa tabla). No es la misma columna que `idcliente`.

JSON: `output/lookup_idcliente.json`
