# Cruce: `matercerosuc.idperfilcartera` x `fecharetiroisp`

- Tabla: `bronze_guajiranet.matercerosuc`
- Filas: **15389**
- Texto de código: valor almacenado en `maperfilcartera.denominacion` (join por `id`)
- No se infiere significado adicional

## Por idperfilcartera

| idperfilcartera | denominacion | filas | fecharetiroisp NULL | fecharetiroisp NO NULL |
|---:|---|---:|---:|---:|
|  |  | 1146 | 1146 | 0 |
| 0 |  | 17 | 17 | 0 |
| 1 | Residencial | 4008 | 3802 | 206 |
| 2 | Deshabilitado | 24 | 21 | 3 |
| 4 | Comercial, Empresarial | 219 | 213 | 6 |
| 5 | Dedicado | 113 | 113 | 0 |
| 6 | Cortesia | 32 | 28 | 4 |
| 7 | Comercial, empresa_espec | 30 | 29 | 1 |
| 8 | Plazo 15 | 48 | 42 | 6 |
| 9 | Plazo 30 | 69 | 62 | 7 |
| 10 | Mintic_Cortesia | 32 | 32 | 0 |
| 11 | Proyecto Mintic | 5763 | 4930 | 833 |
| 12 | Sucesion | 18 | 14 | 4 |
| 13 | Gobierno | 1 | 1 | 0 |
| 16 | Pendiente Construccion | 45 | 45 | 0 |
| 18 | Proceso Retiro | 2921 | 1832 | 1089 |
| 21 | Proceso Retiro Mintic | 822 | 632 | 190 |
| 22 | No_Quiere_Servicio | 81 | 81 | 0 |

## Foco 18 / 21 / 22

| idperfilcartera | denominacion | filas | fecharetiroisp NULL | fecharetiroisp NO NULL |
|---:|---|---:|---:|---:|
| 18 | Proceso Retiro | 2921 | 1832 | 1089 |
| 21 | Proceso Retiro Mintic | 822 | 632 | 190 |
| 22 | No_Quiere_Servicio | 81 | 81 | 0 |

## Comparación con `activo` (totales)

| activo | filas | fecharetiroisp NULL | fecharetiroisp NO NULL |
|---|---:|---:|---:|
| N | 18 | 18 | 0 |
| S | 15371 | 13022 | 2349 |

## Foco 18 / 21 / 22 x `activo`

| idperfilcartera | denominacion | activo | filas | fecharetiroisp NULL | fecharetiroisp NO NULL |
|---:|---|---|---:|---:|---:|
| 18 | Proceso Retiro | N | 1 | 1 | 0 |
| 18 | Proceso Retiro | S | 2920 | 1831 | 1089 |
| 21 | Proceso Retiro Mintic | S | 822 | 632 | 190 |
| 22 | No_Quiere_Servicio | S | 81 | 81 | 0 |

## Todas las combinaciones `idperfilcartera` x `activo`

| idperfilcartera | denominacion | activo | filas | fecharetiroisp NULL | fecharetiroisp NO NULL |
|---:|---|---|---:|---:|---:|
|  |  | N | 11 | 11 | 0 |
|  |  | S | 1135 | 1135 | 0 |
| 0 |  | S | 17 | 17 | 0 |
| 1 | Residencial | N | 4 | 4 | 0 |
| 1 | Residencial | S | 4004 | 3798 | 206 |
| 2 | Deshabilitado | S | 24 | 21 | 3 |
| 4 | Comercial, Empresarial | S | 219 | 213 | 6 |
| 5 | Dedicado | N | 1 | 1 | 0 |
| 5 | Dedicado | S | 112 | 112 | 0 |
| 6 | Cortesia | S | 32 | 28 | 4 |
| 7 | Comercial, empresa_espec | S | 30 | 29 | 1 |
| 8 | Plazo 15 | S | 48 | 42 | 6 |
| 9 | Plazo 30 | S | 69 | 62 | 7 |
| 10 | Mintic_Cortesia | S | 32 | 32 | 0 |
| 11 | Proyecto Mintic | N | 1 | 1 | 0 |
| 11 | Proyecto Mintic | S | 5762 | 4929 | 833 |
| 12 | Sucesion | S | 18 | 14 | 4 |
| 13 | Gobierno | S | 1 | 1 | 0 |
| 16 | Pendiente Construccion | S | 45 | 45 | 0 |
| 18 | Proceso Retiro | N | 1 | 1 | 0 |
| 18 | Proceso Retiro | S | 2920 | 1831 | 1089 |
| 21 | Proceso Retiro Mintic | S | 822 | 632 | 190 |
| 22 | No_Quiere_Servicio | S | 81 | 81 | 0 |

## Nota

Solo conteos observados. El texto de `denominacion` no se interpreta.
