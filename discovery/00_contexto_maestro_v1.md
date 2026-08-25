# CONTEXTO MAESTRO — PROYECTO GUAJIRANET

## 1. Panorama

Proyecto de Data Warehouse y analítica de GuajiraNet con:

**Fuentes/API → Bronze → Silver → Modelo dimensional → Gold → Power BI**

Entorno:
- PostgreSQL / Aurora PostgreSQL AWS
- Apache Hop para pipelines/workflows
- Power BI para dashboards
- Bronze: información transaccional/raw
- Silver: capa analítica y modelo estrella
- Gold: vistas orientadas a negocio

## 2. Estado de Bronze

Esquema:
`bronze_guajiranet`

Discovery automático conectado a Aurora:
- **829 tablas**
- **11.029 columnas**
- **221 relaciones candidatas**

Conexión:
- Host: `cluster-guajiranet-instance-1.cur2img2cxzx.us-east-1.rds.amazonaws.com`
- Puerto: `5432`
- Base: `db_bronze`
- Usuario: `user_guajiranet`
- Esquema: `bronze_guajiranet`

La contraseña NO debe documentarse.

## 3. Scanner de Data Discovery

Proyecto Python:
`guajiranet_data_discovery`

Genera:
- `catalogo_tablas.json`
- `catalogo_columnas.json`
- `perfil_columnas.json`
- `relaciones_candidatas.json`
- `mapa_capacidades.json`
- `resumen_discovery.md`

El primer discovery fue principalmente por nombres de tablas/columnas. Produce falsos positivos y **no debe utilizarse para modelar automáticamente**.

La siguiente fase debe ser semántica y relacional: estructura, PK/FK, nulos, cardinalidad, fechas, muestras reales y relaciones.

## 4. Objetivo actual del proyecto

El jefe quiere ampliar muchísimo el modelo para que los dashboards estén orientados a decisiones de negocio y marketing.

Necesidades que queremos investigar:
- clientes;
- adquisición;
- vinculación;
- instalación;
- activación;
- planes y servicios;
- facturación;
- pagos;
- cartera;
- mora;
- suspensiones;
- retiros/deserción;
- motivos de retiro;
- retención;
- vendedores;
- campañas;
- promociones;
- descuentos;
- geografía;
- comportamiento temporal.

Preguntas objetivo:
- ¿Cuántos clientes se vinculan por mes?
- ¿Cuándo iniciaron?
- ¿Cuándo se instalaron/activaron?
- ¿Cuándo apareció la primera factura?
- ¿Cuándo hicieron el primer pago?
- ¿Cuántos meses pagaron?
- ¿Cuántos meses dejaron de pagar?
- ¿Qué clientes están activos, suspendidos o retirados?
- ¿Cuántos desertan y cuándo?
- ¿Por qué desertan?
- ¿Qué plan tenían?
- ¿Cuál es el plan más vendido?
- ¿Cuál tiene mayor abandono?
- ¿Qué municipios concentran clientes?
- ¿Qué municipios generan ingresos?
- ¿Qué vendedores/campañas generan clientes?
- ¿Qué promociones/descuentos funcionan?
- ¿Qué clientes podrían estar en riesgo?

Todas estas preguntas son hipótesis de negocio. Primero hay que comprobar si los datos existen.

## 5. Modelo dimensional actual

Hecho principal:
`silver_guajiranet.tbl_fact_facturacion`

Campos conocidos:
- `sk_cliente`
- `sk_servicio`
- `sk_geografia`
- `sk_documento`
- `fecha_factura`
- `numero_factura`
- `posicion_factura`
- `cantidad`
- `precio`
- `subtotal`
- `iva`
- `neto`
- `fecha_actualizacion`

Dimensiones principales:
- `silver_guajiranet.tbl_dim_cliente`
- `silver_guajiranet.tbl_dim_servicio`
- `silver_guajiranet.tbl_dim_geografia`
- `silver_guajiranet.tbl_dim_tiempo`
- `silver_guajiranet.tbl_dim_documento`

## 6. DIM_CLIENTE

Usada para relacionar facturación con cliente.

Datos conocidos:
- `sk_cliente`
- `nit`
- `razonsocial`
- `ciudad`
- `idsuc`

Relación usada en la carga:
```sql
CAST(f.nit AS VARCHAR(30)) = dc.nit
AND f.sucursal = dc.idsuc
```

Fuentes Bronze relevantes:
- `materceros`
- `matercerosuc`
- `macrmreferencia`
- `macontacto`

Candidatos importantes de `matercerosuc` encontrados:
- `fecharetiroisp`
- `idperfilcartera`
- `idvendedor`
- `descuento`

Estos campos son candidatos, no datos validados todavía.

## 7. DIM_SERVICIO

Relaciona detalle de facturación con servicio/producto.

Carga actual:
```sql
d.idproducto = ds.id_servicio
```

Facturación viene de:
- `bronze_guajiranet.trfacturas`
- `bronze_guajiranet.trfacturasdet`

Candidatos relacionados con servicios/productos/planes:
- `maafautomotor`
- `maafcomponente`
- `maaiu`
- `maalmacenamiento`
- `maalmproducto`
- `macdatarifa`
- `macomproductovendedor`
- `maconveniopreciosdet`
- `macrmaccion`
- `macrmaccionservicio`
- `macrmlinea`
- `maproductos`

No asumir que todos son planes ISP; validar.

## 8. DIM_GEOGRAFIA

`silver_guajiranet.tbl_dim_geografia`

Contiene/analiza:
- departamento
- municipio
- barrio

Carga de facturación usa:
`bronze_guajiranet.matercerosuc`

Relación:
```sql
LEFT JOIN bronze_guajiranet.matercerosuc ms
ON f.nit = ms.nit
AND f.sucursal = ms.idsuc

LEFT JOIN silver_guajiranet.tbl_dim_geografia dg
ON COALESCE(CAST(ms.idbarrio AS VARCHAR(20)), '0') = dg.id_barrio
```

En Power BI aparece `SIN MUNICIPIO`. Debe validarse si la fuente realmente no tiene ubicación o si hay un problema de integración.

## 9. DIM_TIEMPO

Usada para:
- `fecha`
- `anio`
- `mes`
- `nombre_mes`

Relación:
`ff.fecha_factura = dt.fecha`

## 10. DIM_DOCUMENTO

Carga actual relaciona:
```sql
f.idsuc = dd.idsuc
AND f.prefijo = dd.prefijo
```

## 11. FACT_FACTURACION

Origen:
- `bronze_guajiranet.trfacturas`
- `bronze_guajiranet.trfacturasdet`

Relación:
```sql
f.idsuc = d.idsuc
AND f.prefijo = d.prefijo
AND f.numero = d.numero
```

Campos:
- fecha
- numero
- pos
- cantidad
- precio
- subtotal
- iva
- neto

Validación histórica:
```sql
SELECT MAX(f.fecha)
FROM bronze_guajiranet.trfacturas f
INNER JOIN bronze_guajiranet.trfacturasdet d
 ON f.idsuc=d.idsuc
AND f.prefijo=d.prefijo
AND f.numero=d.numero;
```

En una etapa anterior devolvía 22 de junio porque Bronze no estaba actualizado; posteriormente Bronze fue actualizado y el problema fue solucionado.

## 12. Gold actual

### `gold_guajiranet.vw_capilaridad_servicios`
Analiza:
- categoría
- nombre_plan
- clientes atendidos
- municipios con cobertura
- barrios con cobertura
- total facturas
- ingresos

### `gold_guajiranet.vw_cobertura_geografica`
Analiza:
- departamento
- municipio
- barrio
- clientes
- facturas
- servicios
- valor facturado

### `gold_guajiranet.vw_comportamientos_atipicos`
Analiza:
- NIT
- razón social
- ciudad
- cantidad facturas
- total facturado
- promedio
- máximo
- mínimo
- clasificación

Regla actual:
`MAX(ff.neto) > AVG(ff.neto) * 2`
→ `FACTURACION ATIPICA`
de lo contrario → `COMPORTAMIENTO NORMAL`

La regla debe validarse con negocio.

### `gold_guajiranet.vw_operacion_facturacion`
Analiza:
- año
- mes
- nombre_mes
- departamento
- municipio
- barrio
- categoría
- plan
- facturas
- cantidad
- subtotal
- IVA
- neto

### `gold_guajiranet.vw_transaccionalidad_clientes`
Analiza:
- NIT
- razón social
- ciudad
- transacciones
- valor total
- ticket promedio
- primera transacción
- última transacción

## 13. Dashboard Capilaridad actual

KPIs:
- Clientes atendidos
- Ingresos
- Municipios con cobertura
- Barrios con cobertura

4 visuales:
1. Mapa de cobertura geográfica
2. Clientes por municipio
3. Clientes por plan
4. Ingresos por municipio

Se usa Top 10 en los gráficos.

Objetivo:
- ¿Dónde tenemos presencia?
- ¿Cuántos clientes?
- ¿Qué municipios concentran clientes?
- ¿Qué planes concentran clientes?
- ¿Dónde se generan ingresos?
- ¿Cuál es la cobertura?

Regla de diseño:
- máximo 4 gráficos principales por página
- KPIs arriba
- filtros visibles
- diseño limpio
- no llenar páginas con gráficos innecesarios

## 14. Plan preliminar de libros/dashboards

### Capilaridad
Presencia y distribución de clientes.

### Cobertura geográfica
Distribución territorial, municipios, barrios, servicios y oportunidades.

### Operación de facturación
Evolución y composición de facturación.

### Clientes / Transaccionalidad
Comportamiento transaccional, ticket, facturación y actividad.

### Comportamientos atípicos
Clientes con facturación fuera de patrones.

Estos nombres y páginas son preliminares y deben validarse con el jefe.

## 15. Nueva arquitectura analítica que se quiere investigar

No crear automáticamente; primero comprobar datos.

Posible evolución:
```text
DIM_CLIENTE
DIM_SERVICIO / DIM_PLAN
DIM_GEOGRAFIA
DIM_TIEMPO
DIM_DOCUMENTO
DIM_ESTADO_CLIENTE
DIM_MOTIVO
DIM_VENDEDOR
DIM_CAMPANA
DIM_PROMOCION
DIM_CONTRATO
        |
        +-- FACT_FACTURACION
        +-- FACT_CLIENTE_MES
        +-- FACT_PAGOS
        +-- FACT_CARTERA
        +-- FACT_ESTADO_CLIENTE
        +-- FACT_DESERCION
```

## 16. FACT_CLIENTE_MES — hipótesis importante

Posible granularidad:
**Cliente + Mes**

Ejemplo:
```text
cliente
mes
activo
facturado
pagado
plan
dias_sin_pago
estado_cliente
nuevo_cliente
cliente_retirado
cliente_recuperado
```

Esto permitiría:
- cohortes
- retención
- churn
- clientes en riesgo
- meses activos
- meses pagados
- meses sin pago

Solo es viable si Bronze contiene las fechas/estados/pagos necesarios.

## 17. Candidatos de Data Discovery que requieren investigación

### Cliente
- `materceros`
- `matercerosuc`
- `macrmreferencia`
- `macontacto`

### Retiro / deserción
- `maipsmotivocancelo`
- `matercerosuc.fecharetiroisp`
- `materceropausar`
- `materceroprorroga`

Campos encontrados:
- `maipsmotivocancelo.idcancelo`
- `maipsmotivocancelo.maipsmotivocancelo`
- `materceropausar.activar_motivo`
- `materceroprorroga.cancelado`
- `materceroprorroga.fcancela`
- `materceroprorroga.user_cancela`

### Marketing / comercial
- `macrmcampana`
- `macrmreferencia.codvendedor`
- `mafacturasperiodiconit.idcampana`
- `mafacturasperiodiconit.campana_inicio`
- `matercerosuc.idvendedor`
- `matercerosuc.descuento`
- `maproductos.porcdescuento`
- `matipovendedor`

### Pagos
- `maformasdepago`
- `mafacturasperiodico`
- `mafacturasperiodiconit`
- `machequera`
- `macomrangosrecaudo`

### Cartera / mora
- `vcarterasaldonit`
- `vsaldoscartera`
- `maedadescartera`
- `maperfilcartera`
- `matercerosuc.idperfilcartera`
- `main_interesmora`

## 18. Próximo paso exacto

No analizar manualmente las 829 tablas.

Primero investigar profundamente:
1. `bronze_guajiranet.matercerosuc`
2. `bronze_guajiranet.materceros`
3. `bronze_guajiranet.macrmreferencia`
4. `bronze_guajiranet.maipsmotivocancelo`
5. `bronze_guajiranet.materceroprorroga`
6. `bronze_guajiranet.materceropausar`
7. `bronze_guajiranet.mafacturasperiodiconit`

Para cada una:
- todas las columnas
- tipos
- PK candidata
- FK candidatas
- cantidad de filas
- nulos
- cardinalidad
- fechas min/max
- muestras reales
- relaciones con otras tablas
- significado de negocio

Primera prioridad:
`matercerosuc`

Especial atención a:
- `fecharetiroisp`
- `idperfilcartera`
- `idvendedor`
- `descuento`
- `nit`
- `idsuc`
- cualquier campo de estado/fecha/servicio.

## 19. Faltantes de información

El proyecto debe documentar explícitamente qué necesidades no pueden responderse si el dato no existe.

Ejemplos:
- fecha de vinculación
- fecha instalación
- fecha activación
- fecha retiro
- motivo retiro
- primer pago
- campaña
- vendedor
- descuento
- estado histórico

No inventar indicadores.

Si no existe una fecha de retiro real, no llamar a un cliente “desertor” solo porque dejó de facturar. Puede ser mora, suspensión, falta de datos u otro evento.

## 20. Principio maestro

**Primero descubrimos el dato.  
Después validamos el significado.  
Luego diseñamos el modelo.  
Finalmente construimos el dashboard.**

El objetivo final es un modelo dimensional robusto y extensible que permita construir dashboards orientados a decisiones empresariales sin volver a descubrir la base cada vez.
