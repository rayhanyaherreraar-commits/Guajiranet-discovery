# `bronze_guajiranet.tmjsonplan_server` (`tipo='P'`)

- Read-only. No se interpreta el significado de nombres o claves.
- Alcance: solo esta tabla. `tipo='S'` no se detalla (otro JSON).

## Tabla

| columna | tipo |
|---|---|
| `id` | integer |
| `datajson` | jsonb |
| `tipo` | character |

| tipo | filas |
|---|---:|
| `P` | 282 |
| `S` | 27 |

## `datajson` tipo P

| métrica | valor |
|---|---:|
| filas | 282 |
| `datajson` object | 282 |
| `datajson` null / otro | 0 / 0 |
| claves top-level | **11** |
| claves en las 282 filas | sí |
| objetos anidados | 0 |
| arrays | 0 |
| `datajson.id` distinct | 282 (long. 36–36) |
| `datajson.name` distinct / vacío | 282 / 0 |
| `public_id` distinct / null | 282 / 0 |
| `id` integer = `datajson.id` | 0/282 |

## Claves JSON

| clave | filas | tipos | distinct ≠null | vacío str | min–max (number) |
|---|---:|---|---:|---:|---|
| `ceil_down_kbps` | 282 | number:282 | 83 | 0 | 0–2010000 |
| `ceil_up_kbps` | 282 | number:282 | 87 | 0 | 0–8000000 |
| `cir` | 282 | string:282 | 9 | 0 |  |
| `contracts_count` | 282 | number:282 | 47 | 0 | 0–5851 |
| `created_at` | 282 | string:282 | 282 | 0 |  |
| `frequency_in_months` | 282 | number:282 | 1 | 0 | 1–1 |
| `id` | 282 | string:282 | 282 | 0 |  |
| `name` | 282 | string:282 | 282 | 0 |  |
| `price` | 282 | string:282 | 41 | 0 |  |
| `public_id` | 282 | number:282 | 282 | 0 | 4–348 |
| `updated_at` | 282 | string:282 | 282 | 0 |  |

### Valores (compacto)

- `ceil_down_kbps`: `1`×36; `1000`×12; `150000`×12; `100000`×10; `0`×9; `40000`×9; `80000`×9; `200000`×8 …
- `ceil_up_kbps`: `1`×36; `1000`×12; `75000`×11; `50000`×10; `0`×9; `15000`×9; `20000`×9; `200000`×8 …
- `cir`: `0.125`×94; `1.0`×87; `0.25`×41; `0.1667`×27; `0.13`×16; `0.05`×7; `0.5`×5; `0.11`×4; `0.0625`×1
- `contracts_count`: `0`×173; `1`×17; `2`×17; `3`×10; `4`×6; `9`×5; `5`×3; `8`×3 …
- `created_at`: `2019-02-13T21:19:04.640-05:00`×1; `2019-02-13T21:30:52.199-05:00`×1; `2019-02-13T22:59:01.030-05:00`×1; `2019-02-13T23:17:21.077-05:00`×1; `2019-02-13T23:18:05.594-05:00`×1; `2019-02-14T11:47:02.806-05:00`×1; `2019-02-14T11:47:49.333-05:00`×1; `2019-02-14T11:49:11.705-05:00`×1; `2019-02-14T11:51:05.232-05:00`×1; `2019-02-14T11:52:18.408-05:00`×1; `2019-02-14T11:54:26.416-05:00`×1; `2019-02-23T15:48:59.224-05:00`×1; `2019-03-03T16:53:43.849-05:00`×1; `2019-03-05T20:00:18.788-05:00`×1; `2019-03-05T20:04:52.067-05:00`×1
- `frequency_in_months`: `1`×282
- `id`: 282 valores distintos (no se listan todos).
- `name`: 282 valores distintos (no se listan todos).
- `price`: `0.0`×92; `1.0`×18; `150000.0`×18; `95000.0`×16; `180000.0`×14; `80000.0`×13; `110000.0`×12; `220000.0`×9 …
- `public_id`: `10`×1; `100`×1; `101`×1; `102`×1; `103`×1; `104`×1; `105`×1; `106`×1; `107`×1; `108`×1; `109`×1; `110`×1; `111`×1; `112`×1; `113`×1
- `updated_at`: `2019-12-02T16:31:25.465-05:00`×1; `2020-02-09T15:54:21.009-05:00`×1; `2020-02-09T15:55:26.127-05:00`×1; `2020-02-09T15:56:29.780-05:00`×1; `2020-04-10T13:30:45.622-05:00`×1; `2020-07-24T12:16:16.081-05:00`×1; `2020-08-04T15:36:21.028-05:00`×1; `2020-08-04T15:36:53.678-05:00`×1; `2021-02-14T15:26:26.538-05:00`×1; `2021-02-14T15:35:13.407-05:00`×1; `2021-02-14T15:35:48.033-05:00`×1; `2021-02-14T15:37:17.147-05:00`×1; `2021-02-14T15:38:27.470-05:00`×1; `2021-02-14T15:43:25.106-05:00`×1; `2021-02-14T15:44:44.026-05:00`×1

## Búsqueda por nombre de clave (subcadena, no semántica)

- **categoria_tipo_plan**: ninguna clave cuyo nombre contenga las subcadenas usadas.
- **velocidad**: `ceil_down_kbps`, `ceil_up_kbps`, `cir` (`updated_at` excluido: coincidencia accidental con subcadena `up`)
- **precio_tarifa**: `price`
- **estado**: ninguna clave cuyo nombre contenga las subcadenas usadas.
- **fechas_vigencia**: `created_at`, `updated_at`
- **tecnologia**: ninguna clave cuyo nombre contenga las subcadenas usadas.
- **municipio_cobertura**: ninguna clave cuyo nombre contenga las subcadenas usadas.

## Campos numéricos / fechas presentes

| campo | detalle |
|---|---|
| `frequency_in_months` | distinct 1; `1`×282 |
| `price` | **string** 282/282; distinct 41; valor almacenado `0.0` → 92 |
| `created_at` | min `2019-02-13T21:19:04.640-05:00` · max `2024-11-23T11:10:48.178-05:00` |
| `updated_at` | min `2019-12-02T16:31:25.465-05:00` · max `2026-05-29T12:05:18.766-05:00` |
| `contracts_count` | min 0 · max 5851 · sum 10848 |

`price` valores (todos):

| price | n |
|---:|---:|
| 0.0 | 92 |
| 1.0 | 18 |
| 10000.0 | 1 |
| 26400.0 | 3 |
| 31600.0 | 1 |
| 58000.0 | 8 |
| 68000.0 | 9 |
| 78000.0 | 2 |
| 80000.0 | 13 |
| 88000.0 | 1 |
| 90000.0 | 1 |
| 95000.0 | 16 |
| 100000.0 | 2 |
| 110000.0 | 12 |
| 120000.0 | 1 |
| 126050.0 | 6 |
| 130000.0 | 6 |
| 140000.0 | 1 |
| 150000.0 | 18 |
| 180000.0 | 14 |
| 190000.0 | 1 |
| 200000.0 | 7 |
| 210000.0 | 1 |
| 220000.0 | 9 |
| 240000.0 | 2 |
| 250000.0 | 9 |
| 300000.0 | 7 |
| 340000.0 | 1 |
| 350000.0 | 5 |
| 360000.0 | 1 |
| 400000.0 | 2 |
| 420000.0 | 1 |
| 449999.0 | 1 |
| 476000.0 | 1 |
| 500000.0 | 2 |
| 550000.0 | 1 |
| 600000.0 | 1 |
| 650000.0 | 1 |
| 700000.0 | 1 |
| 800000.0 | 2 |
| 1000000.0 | 1 |

## Distinción residencial / comercial / …

No hay clave JSON de categoría/segmento. Solo texto almacenado en `name`.
Conteos ILIKE (evidencia de subcadena, no taxonomía):

| token en `name` | filas |
|---|---:|
| `Residencial` | 113 |
| `Comercial` | 42 |
| `Empresarial` | 41 |
| `Dedicado` | 43 |
| `Mintic` | 4 |
| `MINTIC` | 4 |
| `MiNTIC` | 4 |
| `Fibra` | 30 |
| `Radio` | 8 |
| `Wireless` | 0 |
| `GPON` | 0 |
| `FTTH` | 0 |
| `Hatonuevo` | 9 |
| `MFOR` | 50 |
| `FOR ` | 177 |

| cruce | filas |
|---|---:|
| `Residencial` | 113 |
| `Comercial` | 42 |
| `Empresarial` | 41 |
| `Dedicado` | 43 |
| `Mintic` | 4 |
| `Residencial_and_Mintic` | 4 |
| `none_of_Residencial_Comercial_Empresarial_Dedicado_Mintic` | 43 |

Nombres **sin** esas 5 subcadenas:

| name almacenado | n |
|---|---:|
| ------------------------------------------ | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (1000 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (1100 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (1200 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (1300 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (1400 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (1500 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (700 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (800 MB) | 1 |
| Canal de Internet Alta Disponibilidad Cerrejon (900 MB) | 1 |
| ----->Corregimientos Locales Interconectado por Fibra<------ | 1 |
| ----->Corregimientos Rurales Interconectado por Radio Enlace<------ | 1 |
| DC1 | 1 |
| DC12 | 1 |
| DC13 | 1 |
| DC15 | 1 |
| DC16 | 1 |
| DC17 | 1 |
| DC18 | 1 |
| DC19 | 1 |
| DC2 | 1 |
| DC20 | 1 |
| DC6 | 1 |
| DC7 | 1 |
| DC9 | 1 |
| ----->Fincas-Parcelas<------ | 1 |
| Guajiranet Recidencial Rural Tipo2 (3mega) | 1 |
| Internet Recidencial NCFT6 Diamante2 (15MB) | 1 |
| Internet Recidencial NCFT7 Diamante3 (20MB) | 1 |
| Internet Recidencial NCFT8 Diamante Especial (30MB) | 1 |
| ----->Internet Rural Casa Finca Radio Sigma<------ | 1 |
| Internet Rural Casa Finca Radio T1 (10Megas) | 1 |
| Internet Rural Casa Finca Radio T2 (20Megas) | 1 |
| Internet Rural Casa Finca Radio T3 (30Megas) | 1 |
| Internet Rural Casa Finca Radio T4 (40Megas) | 1 |
| Internet Rural Casa Finca Radio T5 (xxMegas) | 1 |
| no en el momento | 1 |
| Proyecto Internet Down 10M up 5M | 1 |
| --------------------------TARIFAS ESTANDAR MUNICIPALES CORRE LOCALES Sigma-------------------------- | 1 |
| --------------------------TARIFAS ESTANDAR RURAL POR RADIO Sigma------------------------- | 1 |
| xxxxxxxxxx | 1 |
| xxxxxxxxxxxxxxxxxx | 1 |
| zxxxxxxxxxxxxxxxxx | 1 |

No hay claves de municipio/cobertura/tecnología. Esas palabras, si aparecen, están en `name`.
