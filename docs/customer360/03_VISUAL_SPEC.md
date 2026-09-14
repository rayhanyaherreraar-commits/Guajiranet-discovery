# GuajiraNet — Customer 360

## Prototipo visual detallado de las tres páginas nuevas

**Estado:** especificación de montaje; no contiene DAX ni modifica Power BI.  
**Canvas aprobado:** 1366 × 768 px, 16:9.  
**Unidad:** coordenadas y tamaños aproximados en píxeles de Power BI.

## 1. Sistema común de las tres páginas

### 1.1 Grid maestro

| Zona | X | Y | Ancho | Alto | Uso |
|---|---:|---:|---:|---:|---|
| Navegación lateral | 0 | 0 | 184 | 768 | Logo, navegación, filtros permanentes y reset |
| Área de contenido | 184 | 0 | 1182 | 768 | Encabezado, KPI y visuales |
| Margen izquierdo de contenido | 204 | — | 16 | — | Inicio real de objetos |
| Margen derecho | — | — | 20 | — | Separación del borde |
| Encabezado | 204 | 16 | 1142 | 56 | Título, subtítulo, periodo y actualización |
| Banda KPI | 204 | 84 | 1142 | 104 | Tarjetas principales |
| Área analítica | 204 | 204 | 1142 | 544 | Visuales y detalle |

- Grid interno de **12 columnas** dentro de los 1142 px.
- Separación horizontal y vertical estándar: **12 px**.
- Radio de contenedor: **8 px**. Padding interno: **12 px**.
- Ningún objeto debe entrar en los márgenes ni quedar a menos de 12 px de otro.

### 1.2 Navegación lateral fija

| Elemento | Posición aproximada | Comportamiento |
|---|---|---|
| Logo GuajiraNet | x 20, y 20, 144×48 | Decorativo, sin interacción |
| Botón `Resumen ejecutivo` | x 12, y 92, 160×40 | Navega a Página 1 |
| Botón `Perfil del cliente` | x 12, y 140, 160×40 | Navega a Página 2 |
| Botón `Comportamiento` | x 12, y 188, 160×40 | Navega a Página 3 |
| Botón `Capilaridad` | x 12, y 236, 160×40 | Navega a página existente; no rediseñar |
| Separador | x 20, y 292, 144×1 | Visual |
| Área de filtros | x 12, y 312, 160×320 | Cambia según página |
| `Restablecer filtros` | x 12, y 684, 160×36 | Marcador que devuelve la página a su estado aprobado |
| Leyenda de actualización | x 20, y 732, 144×20 | Texto corto: “Datos actualizados”/estado |

- Botón activo: fondo azul brillante, texto blanco e icono blanco.
- Botones inactivos: fondo transparente, texto blanco al 85%; hover azul medio.
- El botón Capilaridad mantiene navegación, pero no sincroniza filtros automáticamente salvo que ya esté probado.

### 1.3 Estilo común

| Uso | Regla |
|---|---|
| Fondo lateral | Azul marino corporativo aproximado `#062E4F` |
| Fondo página | Gris azulado muy claro `#F4F7FB` |
| Contenedores | Blanco `#FFFFFF`, borde `#DFE7F0`, 1 px |
| Azul principal | `#0878D1` para serie primaria y selección |
| Azul secundario | `#5AA8F5` para comparación o segunda serie |
| Texto principal | `#102A43` |
| Texto secundario | `#66788A` |
| Positivo | Verde `#1FA463` |
| Neutral | Amarillo `#F4B740` |
| Negativo | Rojo `#D94A4A` |
| Sin dato | Gris `#98A6B5`; mostrar “Sin dato”, nunca cero inventado |

- Título de página: 24–26 pt, semibold.
- Subtítulo: 10–11 pt.
- Título de visual: 11–12 pt, semibold.
- Valor de KPI: 22–26 pt; etiqueta: 9–10 pt; comparación: 8–9 pt.
- Máximo seis colores categóricos en un mismo visual.
- Verde/amarillo/rojo se reservan para semáforo y riesgo, no para decorar series.
- Tooltips con fondo blanco, encabezado azul marino y máximo 8 indicadores.

### 1.4 Encabezado común

- Izquierda: título de página y una frase que responda la pregunta ejecutiva.
- Derecha: selector de comparación `PM | PY | YTD`, selector de periodo cuando corresponda y estado de actualización.
- La comparación seleccionada cambia el dato comparativo y semáforo de las tarjetas; PM, PY y YTD permanecen disponibles en el tooltip.
- Estado de actualización: punto verde/amarillo/rojo más texto. No convertir Bronze en alarma visible.

## 2. Página 1 — Resumen ejecutivo

**Pregunta:** ¿Cómo está la base de clientes, cómo evoluciona y dónde están los principales resultados y riesgos?

### 2.1 Distribución general

- Encabezado: y 16–72.
- KPI: y 84–188, siete tarjetas.
- Fila analítica 1: y 204–434, tres visuales.
- Fila analítica 2: y 446–748, tres visuales.

### 2.2 Bloques y coordenadas

| ID | X | Y | Ancho | Alto | Visual y título | Alimentación |
|---|---:|---:|---:|---:|---|---|
| R-H1 | 204 | 16 | 500 | 56 | Texto: `Customer 360 — Resumen ejecutivo` | Subtítulo: “Panorama de clientes, ingresos, cartera y actividad” |
| R-H2 | 718 | 16 | 180 | 56 | Segmentador: `Comparar con` | Parámetro futuro PM/PY/YTD; no escribir DAX en esta fase |
| R-H3 | 910 | 16 | 240 | 56 | Segmentador: `Periodo` | `dim tiempo dax[Fecha]` o jerarquía Año-Mes existente |
| R-H4 | 1162 | 16 | 184 | 56 | Tarjeta compacta: `Actualización` | Vista Gold de estado/resumen y fecha disponible |
| R-K1 | 204 | 84 | 153 | 104 | KPI `Clientes atendidos` | `[Clientes Atendidos]` |
| R-K2 | 369 | 84 | 153 | 104 | KPI `Clientes nuevos` | Medida pendiente basada en primera facturación observada |
| R-K3 | 534 | 84 | 153 | 104 | KPI `Ingresos` | `[Ingresos]` |
| R-K4 | 699 | 84 | 153 | 104 | KPI `Ingreso promedio` | Medida pendiente: ingreso por sucursal atendida |
| R-K5 | 864 | 84 | 153 | 104 | KPI `Saldo de cartera` | `[Saldo Cartera]` |
| R-K6 | 1029 | 84 | 153 | 104 | KPI `Cartera vencida` | `[Cartera Vencida]` |
| R-K7 | 1194 | 84 | 152 | 104 | KPI `Clientes inactivos` | `[Clientes Actualmente Inactivos]` |
| R-V1 | 204 | 204 | 456 | 230 | Línea/columnas: `Evolución de clientes` | Eje temporal + `[Clientes Atendidos]`; clientes nuevos como segunda serie opcional |
| R-V2 | 672 | 204 | 386 | 230 | Línea: `Ingresos mensuales` | Eje temporal + `[Ingresos]`; comparación seleccionada como línea secundaria |
| R-V3 | 1070 | 204 | 276 | 230 | Donut: `Estado de cartera` | `[Cartera No Vencida]`, `[Cartera Vencida]` |
| R-V4 | 204 | 446 | 360 | 302 | Barras horizontales: `Ingresos por producto` | `dim servicio[nombre plan]` + `[Ingresos]`, Top 8 + “Otros” |
| R-V5 | 576 | 446 | 470 | 302 | Tabla/ranking: `Principales clientes por ingresos` | `dim cliente[razon social]`, NIT validado, `[Ingresos]`, variación seleccionada |
| R-V6 | 1058 | 446 | 288 | 302 | Barras compactas: `Señales transaccionales` | Deserciones observadas, recuperaciones e inactivos actuales |

### 2.3 Configuración de tarjetas

Cada tarjeta contiene, de arriba abajo:

1. icono de 18–20 px y título;
2. valor principal;
3. flecha, porcentaje y texto `vs. PM`, `vs. PY` o `vs. YTD anterior`;
4. línea inferior fina del color del semáforo.

- K1–K4: subir es favorable.
- K5–K7: subir es desfavorable; invertir colores.
- Si la base comparable es cero o no existe: mostrar `Sin comparación`, color gris.
- La tarjeta completa no debe filtrar la página al hacer clic; funciona como lectura y tooltip.

### 2.4 Visuales exactos

#### R-V1 — Evolución de clientes

- Visual: gráfico combinado de columnas y línea.
- Columnas: clientes atendidos por mes.
- Línea: clientes nuevos observados, solo si la escala sigue siendo legible; si no, usar small multiple o tooltip.
- Selección de un mes filtra R-V4, R-V5 y KPI con contexto temporal; R-V3 solo se filtra si existe historia temporal válida de cartera. Si cartera es snapshot, ignorará el clic temporal.
- Tooltip: periodo, clientes atendidos, PM, PY, YTD, nuevos observados y variaciones.

#### R-V2 — Ingresos mensuales

- Visual: línea principal azul con marcadores; comparación en azul claro y trazo fino.
- No usar área rellena intensa.
- Tooltip: ingresos del mes, PM, PY, YTD/PYTD, variación y clientes atendidos.

#### R-V3 — Estado de cartera

- Visual: donut de dos segmentos, hueco 62%; valor central `[Saldo Cartera]`.
- Verde para no vencida y rojo para vencida; etiqueta directa con porcentaje y valor.
- No responde al periodo si la tabla es snapshot. Sí responde a filtros de cliente/geografía cuando las relaciones lo permitan.
- Tooltip: saldo total, vencido, no vencido y porcentaje vencido.

#### R-V4 — Ingresos por producto

- Visual: barras horizontales ordenadas de mayor a menor.
- Azul principal; la barra seleccionada usa azul oscuro, no semáforo.
- Título debe decir “producto”, no “plan”.
- Clic filtra R-V5 y resalta tendencias.
- Tooltip: producto ERP, ingresos, clientes atendidos y participación.

#### R-V5 — Principales clientes por ingresos

- Visual: tabla ejecutiva de máximo 10 filas visibles.
- Columnas: Cliente, NIT, Ingresos, Var. seleccionada, semáforo.
- Una fila seleccionada habilita drillthrough a `Perfil del cliente`.
- Barras de datos solo en Ingresos; no saturar todas las columnas.

#### R-V6 — Señales transaccionales

- Visual: tres barras horizontales o tres KPI apilados, sin score combinado.
- Categorías: clientes actualmente inactivos, deserciones transaccionales observadas y recuperaciones transaccionales.
- Rojo para riesgo, verde para recuperación, gris/azul neutro para contexto.
- Tooltip incluye definiciones y advierte que la deserción es observada, no contractual.

### 2.5 Filtros

**Visibles en barra lateral:**

- región/departamento;
- municipio/ciudad;
- producto ERP `dim servicio[nombre plan]`;
- tipo de persona;
- estado del cliente, si el campo exacto está validado.

Orden: geografía → producto → tipo/estado. Usar dropdown con búsqueda y encabezado corto.

**Ocultos o sincronizados:**

- periodo y comparación viven en encabezado;
- filtro de exclusión de blancos/desconocidos solo cuando esté documentado y no cambie totales indebidamente;
- no sincronizar cliente individual desde Perfil hacia Resumen: Resumen debe abrir general.

### 2.6 Navegación e interacciones

- Botones laterales comunes.
- Drillthrough desde R-V5 a Perfil preservando persona/NIT y, si aplica, sucursal.
- Clic en producto cruza ranking y tendencias.
- Clic en mes no debe producir cero falso en cartera snapshot.
- `Restablecer filtros` devuelve periodo aprobado, comparación PM y todos los filtros laterales a `Todos`.

## 3. Página 2 — Perfil del cliente

**Pregunta:** ¿Quién es el cliente, dónde opera, qué tiene contratado, cuánto factura, qué debe y cómo paga?

### 3.1 Distribución general

- Encabezado: y 16–72.
- Banda de selección/ficha: y 84–160.
- KPI: y 172–264, ocho tarjetas.
- Área analítica superior: y 276–488.
- Área detalle inferior: y 500–748.

### 3.2 Bloques y coordenadas

| ID | X | Y | Ancho | Alto | Visual y título | Alimentación |
|---|---:|---:|---:|---:|---|---|
| P-H1 | 204 | 16 | 570 | 56 | Texto: `Customer 360 — Perfil del cliente` | Nombre del cliente seleccionado como subtítulo dinámico si es posible |
| P-H2 | 786 | 16 | 180 | 56 | Segmentador `Comparar con` | PM/PY/YTD para ingresos y actividad; no para snapshot de cartera |
| P-H3 | 978 | 16 | 168 | 56 | Botón/estado `Selección` | Muestra “1 cliente” o aviso de selección |
| P-H4 | 1158 | 16 | 188 | 56 | Tarjeta `Actualización` | Estado Gold |
| P-S1 | 204 | 84 | 430 | 76 | Segmentador principal: `Cliente / razón social` | `dim cliente[razon social]`, búsqueda, selección única recomendada |
| P-S2 | 646 | 84 | 220 | 76 | Segmentador: `NIT` | Campo NIT validado de `dim cliente`; no crea relación |
| P-S3 | 878 | 84 | 180 | 76 | Segmentador: `Sucursal` | `dim cliente[idsuc]` |
| P-S4 | 1070 | 84 | 276 | 76 | Ficha compacta: `Estado y perfil` | Estado, tipo persona, `dim perfil cartera[denominacion]` |
| P-K1 | 204 | 172 | 131 | 92 | KPI `Ingresos` | `[Ingresos]` |
| P-K2 | 347 | 172 | 131 | 92 | KPI `Primera facturación` | `[Fecha Inicio Operacion]` |
| P-K3 | 490 | 172 | 131 | 92 | KPI `Saldo cartera` | `[Saldo Cartera]` |
| P-K4 | 633 | 172 | 131 | 92 | KPI `Cartera vencida` | `[Cartera Vencida]` |
| P-K5 | 776 | 172 | 131 | 92 | KPI `Pago caja aplicado` | `[Pago Aplicado]` |
| P-K6 | 919 | 172 | 131 | 92 | KPI `Pago pasarela` | `[Pago Pasarela]` |
| P-K7 | 1062 | 172 | 131 | 92 | KPI `Contratos` | `[Contratos]` |
| P-K8 | 1205 | 172 | 141 | 92 | KPI `Planes ISP` | `[Planes ISP]` |
| P-V1 | 204 | 276 | 388 | 212 | Línea: `Evolución de ingresos del cliente` | Fecha/mes existente + `[Ingresos]` |
| P-V2 | 604 | 276 | 300 | 212 | Barras: `Productos facturados` | `dim servicio[nombre plan]` + `[Ingresos]` |
| P-V3 | 916 | 276 | 430 | 212 | Ficha: `Identificación y ubicación` | Razón social, NIT, tipo, estado, idsuc, ciudad, municipio, departamento, barrio/dirección disponibles |
| P-T1 | 204 | 500 | 276 | 248 | Tabla: `Contratos` | Campos documentados de `dim contrato` |
| P-T2 | 492 | 500 | 278 | 248 | Tabla: `Planes ISP` | Campos documentados de `dim plan` |
| P-T3 | 782 | 500 | 276 | 248 | Tabla: `Cartera pendiente` | Campos documentados de `fact cartera` |
| P-T4 | 1070 | 500 | 276 | 248 | Contenedor alternable: `Pagos` | Marcador alterna Pago caja / Pago pasarela, manteniéndolos separados |

### 3.3 Estado obligatorio de selección

- La página debe abrir con mensaje: `Selecciona un cliente para ver su perfil` si no llega por drillthrough.
- Sin selección única, ocultar o atenuar ficha y tablas mediante overlay/marcador; no mostrar sumas generales como si fueran de un cliente.
- Si el NIT tiene varias sucursales, mostrar `Todas las sucursales` y permitir elegir `idsuc`.
- Persona/NIT es el encabezado ejecutivo; sucursal es el nivel operativo. No modificar el modelo físico para imponerlo.

### 3.4 Tarjetas

- P-K1 puede usar comparación seleccionada y tooltip PM/PY/YTD.
- P-K2 muestra fecha, sin semáforo.
- P-K3–P-K4 son snapshot: mostrar valor actual y etiqueta `Corte actual`; no simular PM/PY/YTD.
- P-K5–P-K6 deben permanecer separados y usar periodos propios disponibles en sus facts.
- P-K7–P-K8 son conteos actuales; sin semáforo salvo definición futura.
- `Última fecha de pago` debe aparecer en tooltip conjunto de P-K5/P-K6 o en P-S4, no como novena tarjeta.

### 3.5 Visuales exactos

#### P-V1 — Evolución de ingresos del cliente

- Línea azul principal, comparación seleccionada azul claro.
- Tooltip: ingresos, PM, PY, YTD/PYTD, variación y productos facturados.
- Selección de mes resalta P-V2, pero no debe filtrar P-T1/P-T3 si no hay relación temporal válida.

#### P-V2 — Productos facturados

- Barras horizontales Top 6.
- Usa producto ERP, no plan ISP.
- Clic filtra únicamente visuales de facturación compatibles; no debe vaciar contratos/planes por relaciones indirectas no probadas.

#### P-V3 — Identificación y ubicación

- Visual recomendado: tabla/matriz de dos columnas sin encabezados visibles o tarjetas de texto agrupadas.
- Orden: NIT → tipo de persona → estado → sucursal → ciudad/municipio → departamento → dirección/barrio.
- Campos no disponibles se omiten; no dejar etiquetas vacías.
- Sin mapa en esta página: priorizar legibilidad del perfil.

#### P-T1 — Contratos

- Columnas visibles: `public_id`, `state`, `start_date`, `address_city`; `idcontrato` en tooltip o detalle.
- Seleccionar contrato puede filtrar Planes ISP solo mediante bridges validados.
- `state` no se transforma en churn.

#### P-T2 — Planes ISP

- Columnas: `nombre`, velocidad bajada, velocidad subida, `precio`, frecuencia.
- Formatear velocidades en Mbps en presentación solo si la conversión está validada; fuente permanece en kbps.
- `precio` no se titula ingreso.

#### P-T3 — Cartera pendiente

- Columnas: documento (`prefijo` + `numero`), vencimiento, días, saldo.
- Formato condicional en días/saldo: rojo vencido, amarillo próximo, gris/verde no vencido según regla aprobada.
- Tooltip: perfil de cartera y detalle de vencimiento.

#### P-T4 — Pagos

- Dos estados mediante botones/marcadores: `Caja aplicado` y `Pasarela`.
- Caja: documento, recibo, fecha y `carteraaplicado`; nunca `SUM(pagorc)`.
- Pasarela: fecha, medio (`codigo_respuesta`), total, referencia y autorización.
- No existe pestaña “Total pagos” que sume ambos canales.

### 3.6 Filtros

**Visibles:** cliente/razón social, NIT y sucursal en la franja superior. En la barra lateral, tipo de persona y estado pueden mostrarse solo como filtros auxiliares si aportan a la búsqueda.

**Ocultos/sincronizados:**

- cliente y sucursal sincronizados con Comportamiento;
- comparación sincronizada con Resumen, pero solo afecta métricas compatibles;
- no usar `dim tiempo dax` como filtro global de cartera/pagos;
- drillthrough conserva NIT/persona y sucursal cuando venga del ranking.

### 3.7 Navegación e interacciones

- Botones laterales comunes.
- Botón `Ver comportamiento` contextual junto al encabezado o dentro de P-S4.
- Seleccionar contrato filtra Planes; seleccionar producto ERP no filtra contratos.
- Seleccionar documento de cartera puede resaltar aplicaciones asociadas solo si la relación/clave está validada; de lo contrario, sin interacción.
- Reset conserva la página, limpia cliente/NIT/sucursal y vuelve al estado instructivo.

## 4. Página 3 — Comportamiento y riesgo observado

**Pregunta:** ¿Cómo cambia la actividad del cliente, qué episodios aparecen y qué señales observables requieren atención?

### 4.1 Distribución general

- Encabezado: y 16–72.
- Selección contextual: y 84–148.
- KPI: y 160–252, seis tarjetas.
- Área analítica superior: y 264–496, tres visuales.
- Área inferior: y 508–748, dos visuales.

### 4.2 Bloques y coordenadas

| ID | X | Y | Ancho | Alto | Visual y título | Alimentación |
|---|---:|---:|---:|---:|---|---|
| C-H1 | 204 | 16 | 570 | 56 | Texto: `Customer 360 — Comportamiento` | Subtítulo: “Actividad, inactividad, recuperación y pagos observados” |
| C-H2 | 786 | 16 | 180 | 56 | Segmentador `Comparar con` | PM/PY/YTD para series mensuales compatibles |
| C-H3 | 978 | 16 | 168 | 56 | Segmentador `Periodo` | Campo `mes` de Gold mensual o selector compatible |
| C-H4 | 1158 | 16 | 188 | 56 | Tarjeta `Actualización` | Estado Gold; indicar fuente física si está validada |
| C-S1 | 204 | 84 | 500 | 64 | Segmentador `Cliente / razón social` | Sincronizado con Perfil |
| C-S2 | 716 | 84 | 190 | 64 | Segmentador `Sucursal` | `dim cliente[idsuc]` o equivalente conectado |
| C-S3 | 918 | 84 | 220 | 64 | Segmentador `Estado transaccional` | Gold mensual `[estado_transaccional]` |
| C-S4 | 1150 | 84 | 196 | 64 | Segmentador `Confianza` | Gold episodios `[nivel_confianza]` |
| C-K1 | 204 | 160 | 180 | 92 | KPI `Clientes con episodio` | `[Clientes con Episodio]` |
| C-K2 | 396 | 160 | 180 | 92 | KPI `Episodios de inactividad` | `[Episodios de Inactividad]` |
| C-K3 | 588 | 160 | 180 | 92 | KPI `Deserciones observadas` | `[Deserciones Transaccionales Observadas]` |
| C-K4 | 780 | 160 | 180 | 92 | KPI `Recuperaciones observadas` | `[Recuperaciones Transaccionales]` |
| C-K5 | 972 | 160 | 180 | 92 | KPI `% recuperación` | `[% Recuperación Transaccional]` |
| C-K6 | 1164 | 160 | 182 | 92 | KPI `Interrupciones abiertas` | `[Interrupciones de Pago Abiertas]` |
| C-V1 | 204 | 264 | 456 | 232 | Línea/columnas: `Estado transaccional por mes` | Gold mensual: `mes`, estado y conteo distinto/medidas existentes |
| C-V2 | 672 | 264 | 386 | 232 | Líneas: `Deserción y recuperación observadas` | Medidas mensuales existentes |
| C-V3 | 1070 | 264 | 276 | 232 | Línea/columnas: `Interrupción de pago` | `[Clientes en Interrupción de Pago Mes]` |
| C-V4 | 204 | 508 | 360 | 240 | Histograma/barras: `Duración de los episodios` | `dias_inactivo` agrupado + `reconecto` |
| C-V5 | 576 | 508 | 770 | 240 | Tabla: `Detalle de episodios y señales` | Fechas, duración, reconecto, motivo inferido, confianza y señales |

### 4.3 Tarjetas

- C-K1–C-K3 y C-K6 son riesgo/contexto: incrementos se colorean como desfavorables cuando la comparación sea válida.
- C-K4–C-K5: incrementos son favorables.
- C-K2 no implica cantidad de clientes; el tooltip debe aclarar que un cliente puede tener varios episodios.
- C-K3 debe llevar subtítulo `Transaccional, no contractual`.
- Para cliente único, cambiar automáticamente el lenguaje a singular cuando sea viable; si no, mantener títulos neutros.

### 4.4 Visuales exactos

#### C-V1 — Estado transaccional por mes

- Visual: columnas apiladas 100% si el objetivo es composición; columnas apiladas normales si interesa volumen. Recomendación: normales con total visible.
- Categorías permitidas: recuperación observada, activo con facturación, silencio dentro de umbral, deserción observada y sin evidencia suficiente.
- Colores: activo azul, recuperación verde, silencio amarillo suave, deserción rojo, insuficiente gris.
- Tooltip: facturas, ingresos, pagos aplicados, pagos pasarela, meses sin facturación y meses sin pago.

#### C-V2 — Deserción y recuperación observadas

- Visual: dos líneas, rojo para deserción y verde para recuperación.
- Eje compartido mensual; evitar área acumulada porque puede sugerir stock.
- Tooltip: ambas medidas, PM/PY/YTD, días inactivos promedio y porcentaje de recuperación.
- Nota visible pequeña: `Señal basada en ausencia y retorno de facturación`.

#### C-V3 — Interrupción de pago

- Columnas naranjas/rojas por mes; línea opcional para recuperaciones de pago si existe escala compatible.
- Tooltip: episodios de interrupción, recuperaciones de pago, abiertos, días sin pago promedio/máximo.
- No interpretar ausencia de pago como desconexión de servicio.

#### C-V4 — Duración de los episodios

- Visual: barras por rangos `61–90`, `91–180`, `181–365`, `365+` días, sujetos al umbral vigente de 60 días.
- Series apiladas: recuperado (verde) y abierto (rojo/gris oscuro).
- Clic en rango filtra C-V5.
- Tooltip: cantidad, porcentaje, promedio, máximo y umbral vigente.

#### C-V5 — Detalle de episodios y señales

- Columnas visibles: cliente/sucursal, inicio inactividad, fin/actividad posterior, días inactivo, estado abierto/recuperado, motivo inferido, confianza.
- Columnas en tooltip o detalle expandido: última factura previa, actividad previa/posterior, pagos previos/posteriores y retiro registrado.
- Formato condicional: confianza alta azul oscuro, media azul medio, baja gris; estado abierto rojo, recuperado verde.
- `motivo_inferido` es evidencia, no causalidad comercial.

### 4.5 Filtros

**Visibles:** cliente, sucursal, estado transaccional, nivel de confianza y periodo Gold.

**Ocultos/sincronizados:**

- cliente y sucursal sincronizados con Perfil;
- comparación sincronizada con Resumen;
- umbral de 60 días proviene de Gold/parametrización y se muestra en tooltip, no como filtro editable;
- el filtro `reconecto` se controla desde la leyenda/selección de C-V4;
- retiro registrado no se utiliza como filtro predeterminado de deserción.

### 4.6 Navegación e interacciones

- Desde Perfil, botón `Ver comportamiento` conserva cliente y sucursal.
- Clic en mes de C-V1 filtra C-V2/C-V3 y C-V5 cuando comparten el contexto Gold correcto.
- Clic en rango de duración filtra detalle.
- Seleccionar una fila de C-V5 muestra tooltip de episodio; no navega automáticamente fuera de la página.
- Reset mantiene el periodo aprobado, elimina cliente/sucursal/estado/confianza y devuelve vista general.

## 5. Tooltips requeridos

Crear páginas tooltip ocultas con tamaño aproximado 360×260. No incluirlas en navegación.

| Tooltip | Usado en | Contenido obligatorio |
|---|---|---|
| `TT_KPI_Comparaciones` | KPI temporales | Valor actual, PM, PY, YTD, PYTD, tres variaciones y definición corta |
| `TT_Cartera` | Saldo/vencida/donut | Total, vencida, no vencida, porcentaje vencido, fecha de corte, nota `snapshot actual` |
| `TT_Pagos` | Pago aplicado/pasarela | Valor y última fecha por canal; advertencia de no sumar canales |
| `TT_Cliente` | Ranking/encabezado perfil | Razón social, NIT, sucursales, ingresos, cartera, contratos y última actividad |
| `TT_Episodio` | Series y tabla de comportamiento | Umbral, fechas, duración, abierto/recuperado, motivo inferido, confianza y definición transaccional |
| `TT_Definiciones` | Iconos de ayuda | Primera facturación, deserción observada, recuperación observada e interrupción de pago |

## 6. Capas, nombres y orden de objetos

- Usar prefijos por página: `R_`, `P_`, `C_`, y `NAV_` para elementos comunes.
- Orden de capas: fondo → contenedores → títulos → visuales → botones → overlays de ayuda/selección.
- Agrupar navegación, encabezado, KPI y cada fila analítica.
- Bloquear fondos y contenedores una vez aprobados.
- Mantener ocultos en vista los overlays, tooltips y estados alternos que no correspondan al marcador activo.

## 7. Reglas de interacción global

1. Los slicers filtran; los KPI no se usan como filtros.
2. Un clic temporal solo afecta facts con relación temporal válida.
3. Cartera snapshot no responde a comparaciones PM/PY/YTD ni a meses históricos sin fuente comparable.
4. Producto ERP no filtra plan ISP/contrato salvo relación validada; visualmente siguen separados.
5. Cliente/NIT filtra el conjunto; sucursal baja el detalle sin redefinir físicamente el modelo.
6. Pago aplicado y pasarela nunca se suman ni se presentan como un único recaudo.
7. Drillthrough principal: Resumen → Perfil. Navegación contextual: Perfil → Comportamiento.
8. Los filtros sincronizados deben probarse página por página; si producen ambigüedad, se mantienen locales.

## 8. Orden de montaje posterior

Cuando se autorice la construcción:

1. crear tema visual y plantilla común;
2. montar navegación y encabezado en tres páginas;
3. montar contenedores y grid sin datos;
4. montar Resumen y validar interacción temporal/snapshot;
5. montar Perfil y validar persona/NIT → sucursal;
6. montar Comportamiento y validar Gold físico/refresco;
7. crear tooltips y marcadores;
8. validar estados vacío, selección única y multisucursal;
9. pulir formatos, accesibilidad y rendimiento.

## 9. Criterio de prototipo aprobado

El prototipo visual queda listo para montaje cuando:

- las coordenadas caben en 1366×768 sin solapamientos;
- cada visual tiene título, fuente y comportamiento definido;
- las siete decisiones aprobadas están reflejadas;
- ninguna comparación temporal se asigna a cartera snapshot;
- persona/NIT es la lectura ejecutiva y sucursal el detalle;
- Capilaridad está enlazada y no rediseñada;
- no aparecen NPS, churn certificado, Health Score o Next Best Action;
- los tres recorridos funcionan conceptualmente: general → cliente → comportamiento;
- no queda ninguna zona cuyo contenido deba improvisarse durante el montaje.
