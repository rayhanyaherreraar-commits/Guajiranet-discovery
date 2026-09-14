# Customer 360 — DAX requerido

## Regla previa

Antes de crear cualquier medida, Cursor debe auditar las medidas existentes en `Guajiranet_COMPAT_V2_TEST.pbix` para evitar duplicados y documentar equivalencias. Este documento registra pendientes; no contiene fórmulas.

## Auditoría puntual de medidas y campos

**Fecha:** 2026-09-14
**Alcance:** medidas y campos requeridos por el blueprint y la especificación visual. No se modificaron el PBIX, medidas existentes, relaciones ni capas de datos.

### Evidencia y límite de la auditoría

- El repositorio Discovery no contiene `Guajiranet_COMPAT_V2_TEST.pbix` ni una extracción TMDL/BIM del modelo.
- Se contrastaron los inventarios TOM/PBIR y los archivos DAX de preparación existentes. Estos confirman nombres, tabla home y campos, pero no permiten validar todas las fórmulas comprimidas dentro del PBIX.
- Medidas base confirmadas en `fact facturacion`: `[Clientes Atendidos]`, `[Ingresos]`, `[Clientes Atendidos Mes Anterior]`, `[Venta Mes Actual]` y `[MoM% de Suma de venta]`. Las tres últimas tienen cobertura parcial respecto del patrón temporal requerido.
- Columnas confirmadas: `fact facturacion[fecha_factura]`, `[Fecha Inicio Operacion]`, `[Año Mes Inicio Operacion]`; `dim tiempo dax[Fecha]`, `[Año]`, `[Mes]`, `[Año-Mes]`; `dim cliente[nit]`, `[idsuc]`, `[razon social]`.
- Medidas 360 reutilizables como dependencias: `[Saldo Cartera]`, `[Cartera Vencida]`, `[Cartera No Vencida]`, `[Pago Aplicado]`, `[Pago Pasarela]`, `[Ultima Fecha Pago]`, `[Contratos]` y `[Planes ISP]`.
- Medidas Gold reutilizables como dependencias: `[Clientes con Episodio]`, `[Episodios de Inactividad]`, `[Deserciones Transaccionales Observadas]`, `[Recuperaciones Transaccionales]`, `[% Recuperación Transaccional]`, `[Clientes Actualmente Inactivos]` e `[Interrupciones de Pago Abiertas]`.
- Antes de implementar DAX se debe confirmar dentro del PBIX TEST que los nombres anteriores continúan vigentes y que no existen medidas ocultas equivalentes.

### Clasificación

| Necesidad | Estado | Medida existente encontrada | Tabla donde vive | Dependencia | Riesgo / limitación | Siguiente acción |
|---|---|---|---|---|---|---|
| Clientes nuevos observados | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente. `[Fecha Inicio Operacion]` es columna, no medida. | Destino sugerido: tabla de medidas Customer 360 | `fact facturacion[Fecha Inicio Operacion]`, cliente/sucursal y contexto de `dim tiempo dax` | Primera facturación observada no equivale a alta contractual; definir conteo por persona/NIT sin duplicar sucursales | Confirmar grano ejecutivo en el PBIX TEST y diseñar la medida sin escribirla todavía |
| Ingreso promedio por sucursal atendida | **NO EXISTE Y HAY QUE CREAR** | `[Ingresos]` y `[Clientes Atendidos]` existen, pero no su cociente con este significado | Dependencias en `fact facturacion`; destino sugerido: tabla de medidas Customer 360 | `[Ingresos]`, `[Clientes Atendidos]` | `[Clientes Atendidos]` conserva grano sucursal; el título no debe decir ticket por persona | Crear una medida explícita y rotularla `Ingreso promedio por sucursal atendida` |
| Periodo anterior (PM) por KPI temporal aprobado | **EXISTE PERO REQUIERE AJUSTE** | `[Clientes Atendidos Mes Anterior]`; también hay evidencia de `[Venta Mes Actual]` y lógica mensual existente | `fact facturacion` | `[Clientes Atendidos]`, `[Ingresos]`, clientes nuevos y `dim tiempo dax[Fecha]` | Cobertura parcial; no se validó fórmula interna ni existe evidencia de PM para todos los KPI | Auditar fórmulas en el PBIX TEST, reutilizar lo equivalente y completar solo KPI faltantes |
| Mismo periodo del año anterior (PY) | **NO EXISTE Y HAY QUE CREAR** | No se encontró medida equivalente | Destino sugerido: tabla de medidas Customer 360 | KPI base y calendario continuo `dim tiempo dax` | Requiere relación temporal activa y periodos comparables | Validar calendario y crear patrón PY únicamente para KPI temporales aprobados |
| Acumulado del año (YTD) | **NO EXISTE Y HAY QUE CREAR** | No se encontró medida equivalente | Destino sugerido: tabla de medidas Customer 360 | KPI base, `dim tiempo dax[Fecha]` y año fiscal/calendario confirmado | Puede producir resultados incorrectos si el calendario no está marcado o no es continuo | Confirmar calendario natural y crear YTD solo para facturación/conteos compatibles |
| Acumulado equivalente del año anterior (PYTD) | **NO EXISTE Y HAY QUE CREAR** | No se encontró medida equivalente | Destino sugerido: tabla de medidas Customer 360 | Medida YTD, KPI base y calendario | Debe comparar ventanas equivalentes hasta la misma fecha de corte | Crear después de validar YTD y el corte temporal |
| Variaciones porcentuales frente a PM, PY y PYTD | **EXISTE PERO REQUIERE AJUSTE** | `[MoM% de Suma de venta]` cubre solo variación mensual de venta; no cubre PY/PYTD ni todos los KPI | `fact facturacion` | Medidas actuales y comparables PM/PY/PYTD | `venta` es alias de `neto`; denominador cero o vacío debe dar `Sin comparación`, no infinito ni cero inventado | Validar la fórmula MoM existente y crear únicamente variantes faltantes por KPI |
| Texto dinámico de comparación seleccionada | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente | Destino sugerido: tabla de medidas Customer 360 | Selector desconectado PM/PY/YTD y medidas de variación | Requiere una selección única y fallback controlado | Definir parámetro/tabla de selección y luego una medida de texto |
| Semáforo con umbral ±10% | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente | Destino sugerido: tabla de medidas Customer 360 | Variación seleccionada y regla aprobada | Exactamente ±10% pertenece a amarillo; sin comparación debe ser gris | Crear auxiliar de color después de las variaciones |
| Lógica invertida para indicadores de riesgo | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente | Destino sugerido: tabla de medidas Customer 360 | Semáforo base y clasificación de dirección favorable | Cartera vencida, inactividad, deserción e interrupciones no pueden usar la dirección de ingresos | Definir metadato o auxiliares separados para KPI donde subir es desfavorable |
| Auxiliares para selección única de persona/NIT y sucursal | **NO EXISTE Y HAY QUE CREAR** | No se encontró medida equivalente; sí existen `dim cliente[nit]`, `[idsuc]` y `[razon social]` | Campos en `dim cliente`; destino de medidas en tabla Customer 360 | Contexto de persona/NIT y sucursal existente | `sk_cliente` representa sucursal en varias capas; no crear relaciones nuevas ni usar NIT como relación | Crear auxiliares de validación/etiqueta que lean el contexto existente |
| Estados vacíos cuando no exista cliente seleccionado | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente | Destino sugerido: tabla de medidas Customer 360 | Auxiliar de selección única | Sin control, Perfil puede mostrar totales generales como si fueran de un cliente | Crear bandera/mensaje para controlar overlays y visibilidad |
| Mensajes `Sin dato` y `Sin comparación` | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente | Destino sugerido: tabla de medidas Customer 360 | Valores KPI, comparables y auxiliares de selección | No convertir `BLANK()` en cero; distinguir ausencia de valor de ausencia de base comparable | Crear auxiliares de presentación después de validar cada KPI |
| Títulos dinámicos y auxiliares de tooltip | **NO EXISTE Y HAY QUE CREAR** | No se encontró equivalente | Destino sugerido: tabla de medidas Customer 360 | Selector de comparación, cliente seleccionado, definiciones y estado de datos | Terminología sensible: primera facturación y deserción/recuperación observadas | Crear al final, reutilizando las medidas y mensajes anteriores |
| Comparaciones históricas de `fact cartera` | **NO DEBE CREARSE POR LIMITACIÓN DE DATOS** | `[Saldo Cartera]`, `[Cartera Vencida]` y `[Cartera No Vencida]` existen solo para corte actual | Medidas 360 sobre `fact cartera` | Snapshot latest-open y fecha de corte | No hay snapshots históricos mensuales comparables; PM/PY/YTD producirían historia ficticia | Mantener etiqueta `Corte actual`, excluirla del selector temporal y mostrar fecha de corte |

### Conteo por categoría

- **EXISTE Y SE REUTILIZA:** 0 necesidades completas.
- **EXISTE PERO REQUIERE AJUSTE:** 2 necesidades.
- **NO EXISTE Y HAY QUE CREAR:** 12 necesidades.
- **NO DEBE CREARSE POR LIMITACIÓN DE DATOS:** 1 necesidad.

Las medidas base existentes se reutilizan como dependencias, pero ninguna cubre por sí sola una necesidad completa pendiente distinta de los dos patrones parciales identificados.

## Restricciones

- No crear comparaciones históricas de cartera mientras sea solo snapshot.
- No sumar Pago Aplicado y Pago Pasarela.
- No usar `SUM(pagorc)`.
- No convertir primera facturación en vinculación contractual.
- No llamar churn certificado a la deserción observada.
