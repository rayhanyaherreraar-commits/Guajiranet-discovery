# `matercerosuc.fecharetiroisp` (solo NO NULL)

- Schema: `bronze_guajiranet`
- Read-only
- Texto de perfiles: valor almacenado en `maperfilcartera.denominacion`
- No se asigna negocio a los campos

## Volumen

| métrica | valor |
|---|---:|
| filas tabla | 15389 |
| `fecharetiroisp` NULL | 13040 |
| `fecharetiroisp` NO NULL | **2349** |
| fechas distintas | 13 |
| min / max | 2025-11-01 / 2026-08-01 |

Tipo: `date`, nullable. Posición 71.

## Distribución de fechas (2349)

| fecha | filas | fecha | filas |
|---|---:|---|---:|
| 2025-11-01 | 246 | 2026-04-01 | 163 |
| 2025-12-01 | 199 | 2026-04-02 | 1 |
| 2026-01-02 | 323 | 2026-05-01 | 176 |
| 2026-01-03 | 1 | 2026-06-01 | 182 |
| 2026-02-01 | 232 | 2026-07-01 | 215 |
| 2026-02-02 | 4 | 2026-08-01 | 290 |
| 2026-03-01 | 317 | | |

Día del mes: día 1 = 2020; día 2 = 328; día 3 = 1.

Llaves en el subconjunto NO NULL: `(nit,idsuc)` 2349/2349 único; `(nit,id)` 2349/2349 único; `nit` distintos = 2344 (5 nit con 2 filas, distinta sucursal).

## vs `idperfilcartera`

| idperfilcartera | denominacion | filas NO NULL |
|---:|---|---:|
| 18 | Proceso Retiro | 1089 |
| 11 | Proyecto Mintic | 833 |
| 1 | Residencial | 206 |
| 21 | Proceso Retiro Mintic | 190 |
| 9 | Plazo 30 | 7 |
| 4 | Comercial, Empresarial | 6 |
| 8 | Plazo 15 | 6 |
| 6 | Cortesia | 4 |
| 12 | Sucesion | 4 |
| 2 | Deshabilitado | 3 |
| 7 | Comercial, empresa_espec | 1 |

Códigos 0, 5, 10, 13, 16, **22** y NULL no aparecen en este subconjunto.

## vs `idperfilcartera_anterior`

Ningún NULL en el subconjunto (2349/2349).

| idperfilcartera_anterior | denominacion | filas |
|---:|---|---:|
| 21 | Proceso Retiro Mintic | 1583 |
| 1 | Residencial | 539 |
| 11 | Proyecto Mintic | 201 |
| 4 | Comercial, Empresarial | 14 |
| 9 | Plazo 30 | 8 |
| 8 | Plazo 15 | 4 |

Cambio actual vs anterior (solo NO NULL):

| condición | filas |
|---|---:|
| anterior = actual | 323 |
| anterior ≠ actual | 2026 |
| anterior NULL | 0 |

Pares más frecuentes: 18←21 (787), 11←21 (728), 18←1 (293), 1←1 (191), 21←11 (131).

## vs `activo`

| activo | filas NO NULL |
|---|---:|
| S | 2349 |
| N | 0 |

## vs `idcontrato`

| métrica | valor |
|---|---:|
| `idcontrato` NULL | 324 |
| `idcontrato` NO NULL | 2025 |
| distinct no nulos | 2025 (sin duplicados en este subconjunto) |

## vs `finiciopermanencia`

| métrica | filas |
|---|---:|
| inicio NULL | 118 |
| inicio NO NULL | 2231 |
| retiro > inicio | 2225 |
| retiro = inicio | 0 |
| retiro < inicio | 6 |
| inicio = 1899-12-30 | 64 |

Los 6 `fecharetiroisp < finiciopermanencia`: nit 17954549, 17957311, 77096529, 77102116, 1006714386, 1120751356. Todos `activo=S`, `idsuc=0`.

## Otras tablas con columna `fecharetiroisp`

Búsqueda en `information_schema.columns` del schema `bronze_guajiranet`:

- nombre exacto `fecharetiroisp`
- `ILIKE '%fecharetiroisp%'`, `'%retiroisp%'`, `'%retiro%isp%'`
- tablas con nombre `ILIKE '%retiro%'`

Resultado: **solo** `matercerosuc.fecharetiroisp`. No hay otra tabla/columna homónima ni tabla cuyo nombre contenga `retiro` en este schema. No hay estructura ni join que comparar.

## Conclusiones

### Confirmado

- 2349 filas con `fecharetiroisp` no nulo; 13 valores; rango 2025-11-01 a 2026-08-01.
- En ese subconjunto, `activo` es siempre `S`.
- En ese subconjunto, `idperfilcartera_anterior` nunca es NULL.
- `(nit,idsuc)` identifica de forma única esas 2349 filas.
- Si `idcontrato` no es NULL, no se repite en el subconjunto (2025 valores, 2025 filas).
- No existe otra tabla en `bronze_guajiranet` con columna `fecharetiroisp`.

### Relación candidata

- Co-ocurrencia frecuente con `idperfilcartera` 18 (1089) y 21 (190), y con `idperfilcartera_anterior` 21 (1583). Es conteo, no prueba de regla.
- 2020/2349 fechas caen el día 1 del mes; el resto el día 2 o 3. Patrón de carga/corte posible; no verificado.
- 2025/2349 tienen `idcontrato`; la fecha podría asociarse a sucursal con contrato, no a todas.

### Dato ambiguo

- 833 filas con fecha y `idperfilcartera=11` (Proyecto Mintic); 206 con código 1 (Residencial). La fecha no está restringida a 18/21.
- Código 22 (No_Quiere_Servicio): 81 filas en la tabla y **0** con `fecharetiroisp` no nulo.
- 323 filas con fecha y perfil actual = anterior.
- 324 filas con fecha y `idcontrato` NULL.
- 118 con fecha y `finiciopermanencia` NULL; 64 con `finiciopermanencia=1899-12-30`; 6 con retiro anterior a inicio.
- `activo=N` (18 filas en la tabla) nunca coincide con `fecharetiroisp` no nulo.

JSON: `output/analisis_fecharetiroisp.json`
