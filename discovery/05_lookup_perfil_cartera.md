# Lookup: `matercerosuc` → `maperfilcartera`

- Schema: `bronze_guajiranet`
- Conexión: read-only
- El texto reportado es el valor almacenado en la columna de etiqueta; no se interpreta

## Tabla origen
- `bronze_guajiranet.matercerosuc`
- Columnas: `idperfilcartera`, `idperfilcartera_anterior`

## Tabla maestra encontrada
- `bronze_guajiranet.maperfilcartera`
- Token de búsqueda: `perfilcartera`
- Tablas cuyo nombre contiene el token: `maperfilcartera`
- Otras tablas con la misma columna (no maestras): `macrmreferencia.idperfilcartera`

## Columnas de unión
- Hijo: `matercerosuc.idperfilcartera`, `matercerosuc.idperfilcartera_anterior`
- Maestro: `maperfilcartera.id`
- Etiqueta textual observada: `maperfilcartera.denominacion`
- `id` único en maestro: **True**
- Filas maestro: **17**

## Cardinalidad
- Hijo → maestro: **N:1**
- Filas hijo por código: min=1, max=5763, avg=837.8235

## Cobertura `idperfilcartera`
- Filas: **15389**
- Nulos: **1146**
- Códigos distintos no nulos: **17**
- Códigos presentes en maestro: **16**
- Códigos ausentes en maestro: **1**
- Filas no nulas con match: **14226**
- Filas no nulas sin match: **17**
- Cobertura códigos: **94.1176%**
- Cobertura filas no nulas: **99.8806%**

### Código y texto (`idperfilcartera`)
| código | texto | filas | en_maestro |
|---|---|---:---|---|
|  |  | 1146 | no |
| 0 |  | 17 | no |
| 1 | Residencial | 4008 | sí |
| 2 | Deshabilitado | 24 | sí |
| 4 | Comercial, Empresarial | 219 | sí |
| 5 | Dedicado | 113 | sí |
| 6 | Cortesia | 32 | sí |
| 7 | Comercial, empresa_espec | 30 | sí |
| 8 | Plazo 15 | 48 | sí |
| 9 | Plazo 30 | 69 | sí |
| 10 | Mintic_Cortesia | 32 | sí |
| 11 | Proyecto Mintic | 5763 | sí |
| 12 | Sucesion | 18 | sí |
| 13 | Gobierno | 1 | sí |
| 16 | Pendiente Construccion | 45 | sí |
| 18 | Proceso Retiro | 2921 | sí |
| 21 | Proceso Retiro Mintic | 822 | sí |
| 22 | No_Quiere_Servicio | 81 | sí |

## Cobertura `idperfilcartera_anterior`
- Filas: **15389**
- Nulos: **13039**
- Códigos distintos no nulos: **7**
- Códigos presentes en maestro: **6**
- Códigos ausentes en maestro: **1**
- Filas no nulas con match: **2349**
- Filas no nulas sin match: **1**
- Cobertura códigos: **85.7143%**
- Cobertura filas no nulas: **99.9574%**

### Código y texto (`idperfilcartera_anterior`)
| código | texto | filas | en_maestro |
|---|---|---:---|---|
|  |  | 13039 | no |
| 0 |  | 1 | no |
| 1 | Residencial | 539 | sí |
| 4 | Comercial, Empresarial | 14 | sí |
| 8 | Plazo 15 | 4 | sí |
| 9 | Plazo 30 | 8 | sí |
| 11 | Proyecto Mintic | 201 | sí |
| 21 | Proceso Retiro Mintic | 1583 | sí |

## Catálogo maestro (código + texto)
| código | texto | usado_en_hijo |
|---|---|---|
| 1 | Residencial | sí |
| 2 | Deshabilitado | sí |
| 4 | Comercial, Empresarial | sí |
| 5 | Dedicado | sí |
| 6 | Cortesia | sí |
| 7 | Comercial, empresa_espec | sí |
| 8 | Plazo 15 | sí |
| 9 | Plazo 30 | sí |
| 10 | Mintic_Cortesia | sí |
| 11 | Proyecto Mintic | sí |
| 12 | Sucesion | sí |
| 13 | Gobierno | sí |
| 16 | Pendiente Construccion | sí |
| 18 | Proceso Retiro | sí |
| 20 | Mintic_Guajiranet | no |
| 21 | Proceso Retiro Mintic | sí |
| 22 | No_Quiere_Servicio | sí |
- Códigos maestro no usados en las columnas hijas: 20=Mintic_Guajiranet

## Evidencia de la relación
- Nombre de tabla maestra coincide con el sufijo de `idperfilcartera` → `perfilcartera`
- Join observado: `matercerosuc.idperfilcartera = maperfilcartera.id`
- La llave `id` es única en el maestro: True
- La columna `denominacion` aporta el texto almacenado por código

## Nota
Solo se reportan valores almacenados y conteos. No se asigna negocio a los textos.
