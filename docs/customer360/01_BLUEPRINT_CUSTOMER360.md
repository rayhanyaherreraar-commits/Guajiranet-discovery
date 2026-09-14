# GuajiraNet — Customer 360 ejecutivo

## Blueprint funcional y plan de ejecución

**Fecha de análisis:** 14 de septiembre de 2026  
**Archivo autorizado:** `Guajiranet_COMPAT_V2_TEST.pbix`  
**Archivo protegido:** `Guajiranet (1).pbix`  
**Estado:** diseño previo; no se ha modificado Power BI, Silver, Delta ni Gold.

## 1. Resumen ejecutivo

El proyecto no parte de cero. Silver v2, el modelo dimensional, las vistas de compatibilidad, la capa Gold de ciclo de vida, varias medidas DAX y cuatro páginas funcionales ya existen. El problema que motiva este ciclo es principalmente de presentación, jerarquía y narrativa ejecutiva, aunque la reunión añadió requisitos funcionales nuevos: tres páginas, comparaciones temporales, semaforización, navegación y validación diaria.

La nueva entrega debe convertir los activos existentes en un Customer 360 con tres niveles de lectura:

1. visión general de la base de clientes;
2. perfil individual de un cliente o sucursal;
3. comportamiento histórico, riesgo y recuperación.

La imagen de referencia define el estándar visual: formato panorámico, barra lateral, tarjetas superiores con iconos, fondo blanco, gráficos limpios, filtros jerarquizados y lectura de arriba hacia abajo. No define los KPI. NPS, satisfacción, churn certificado, Health Score predictivo, propensión de compra y Next Best Action quedan fuera porque no están soportados por las fuentes actuales.

## 2. Requisitos prioritarios de la reunión

- Entrega mínima de tres hojas: generalidades, selección individual y comportamiento analítico.
- Vista general de GuajiraNet y consulta detallada por cliente/documento.
- Todos los objetos de una página deben responder de manera coherente al filtro de cliente.
- Todo visual temporal debe permitir tres referencias: periodo anterior, mismo periodo del año anterior y YTD frente a YTD del año anterior.
- Los KPI deben incorporar variación y semáforo.
- Diseño panorámico horizontal, fondo claro, tarjetas superiores con iconos, gráficos horizontales limpios e hipervínculos/botones de navegación.
- Prototipo visual validado antes de completar el montaje.
- Capturas o archivo de avance diario y control explícito de cambios.
- Fecha límite indicada en las notas: jueves 17 de septiembre de 2026; presentación el viernes 18.

### Regla de semáforo corregida

La nota de Gemini expresa la regla de forma incompleta. Se propone formalizarla así, sujeta a confirmación del jefe:

| Variación | KPI donde subir es favorable | KPI donde bajar es favorable |
|---|---|---|
| Mayor que +10% | Verde | Rojo |
| Entre -10% y +10%, inclusive | Amarillo | Amarillo |
| Menor que -10% | Rojo | Verde |

El segundo criterio aplica, por ejemplo, a cartera vencida, días de mora, inactividad e interrupciones abiertas. Un crecimiento de estas métricas no debe mostrarse en verde.

## 3. Estado verificado del proyecto

### Terminado y validado

- Discovery Bronze priorizado y documentado.
- Modelo Silver v2 con dimensiones de persona, sucursal, contrato, plan, perfil de cartera, geografía y producto ERP.
- Hechos de facturación v2, cartera v2, pago aplicado y pago pasarela.
- Bridges persona-UUID, sucursal-contrato y contrato-plan.
- Vistas de compatibilidad para las consultas principales del PBIX.
- Relaciones base de facturación con cliente, servicio, geografía y calendario.
- Gold analítico de estado mensual, episodios, interrupción de pago y resumen de ciclo de vida.
- Tabla física de episodios validada contra la vista (7.735 filas en la corrida documentada, sin diferencias ni duplicados).
- Ejecución diaria de Silver v2 independiente del flujo productivo v1.
- Vistas Gold para informar frescura de Silver v1, Silver v2 y Gold.
- Medidas existentes de ingresos, clientes atendidos, mes anterior y Customer 360.
- Página Capilaridad funcional.
- Páginas Cliente 360 Resumen, Cliente 360 Detalle y Vinculación/Deserción funcionales.

### Parcial o pendiente

- La tabla física de episodios existe, pero su refresh diario estaba propuesto y no conectado al cron en la evidencia revisada.
- Power BI todavía debe validarse contra la fuente física antes de sustituir la vista Gold de episodios.
- Las comparaciones temporales completas (PM, PY y YTD contra PYTD) no están documentadas como terminadas para todos los KPI del nuevo alcance.
- La detección formal de anomalías no existe.
- El diseño visual ejecutivo de las tres hojas no existe.
- La navegación y los tooltips ejecutivos deben verificarse o construirse.
- La regla de semáforo debe aprobarse, especialmente para KPI de dirección inversa.

## 4. Activos reutilizables de las páginas actuales

| Activo | Estado | Uso en la nueva versión |
|---|---|---|
| Página Capilaridad | Funcional; no rediseñar | Mantener como activo separado y enlazar desde navegación si se aprueba. |
| Selector `dim cliente[razon social]` | Probado | Reutilizar/sincronizar en Perfil y Comportamiento. |
| `Clientes Atendidos` | Existente | KPI de base general; en perfil nombrar “Sucursales facturadas” solo si el contexto lo justifica. |
| `Ingresos` | Existente | KPI principal, serie temporal y ranking. |
| `Fecha Inicio Operacion` | Existente | Mostrar como “Primera facturación”, nunca como fecha contractual de vinculación. |
| Evolución de ingresos | Funcional | Reusar configuración/campos y añadir comparaciones. |
| Ingresos por producto ERP | Funcional | Reusar con `dim servicio[nombre plan]`; no sustituir por plan ISP. |
| Tabla de identificación | Funcional | Reorganizar como ficha ejecutiva. |
| Tarjetas de cartera/pagos/contratos/planes | Existentes | Reutilizar sus medidas en Perfil. |
| Tablas de contrato, plan, cartera y pagos | Funcionales | Reusar en Perfil/Detalle, reduciendo columnas visibles y usando tooltip/drillthrough. |
| Página Vinculación/Deserción | Funcional | Fuente principal para Comportamiento; renombrar visualmente con terminología transaccional aprobada. |
| Medidas Gold de episodios y recuperación | Existentes | KPI y series de Comportamiento. |

El rechazo visual no invalida medidas, relaciones, campos, consultas ni pruebas de filtrado ya realizadas.

## 5. Análisis de la referencia visual

### Patrones que sí se adoptan

- lienzo 16:9 panorámico;
- navegación vertical consistente;
- encabezado con título, subtítulo, periodo y estado de actualización;
- primera fila de tarjetas compactas con icono, valor, variación y texto comparativo;
- cuadrícula de contenedores blancos con bordes suaves;
- predominio de azul corporativo con verde, amarillo y rojo solo para estado;
- gráficos con poco ruido visual, etiquetas directas y máximo una pregunta por visual;
- filtros secundarios agrupados en la barra lateral;
- orden de lectura: resumen, tendencia, composición/ranking y detalle/riesgo.

### Elementos que se adaptan

- “Clientes activos” se define con actividad/facturación observada, no con churn contractual.
- “Clientes nuevos” se basa en primera facturación observada dentro del periodo.
- “Churn” se reemplaza por deserción transaccional observada.
- “Salud del cliente” se reemplaza por señales observables de cartera/inactividad; no se crea un score único sin definición aprobada.
- “Próximas mejores acciones” se reemplaza, si se incluye, por una lista descriptiva de alertas operativas basadas en reglas, no por recomendaciones predictivas.

### Elementos descartados

- NPS y satisfacción;
- propensión de compra y cross-selling inferido;
- Health Score predictivo;
- churn o reconexión certificados;
- PQR, call center, WhatsApp y web.

## 6. Blueprint de páginas

### Página 1 — Resumen ejecutivo

**Pregunta:** ¿Cómo está evolucionando la base de clientes y dónde están los principales resultados y riesgos?

#### Encabezado y filtros

- Título: `Customer 360 — Resumen ejecutivo`.
- Estado de actualización: `gold_guajiranet.vw_anl_estado_actualizacion_resumen[estado_general]` y fecha/hora disponible en esa vista.
- Periodo: `dim tiempo dax[Fecha]`, presentado como selector de rango o Año-Mes.
- Filtros laterales: región/departamento/municipio/ciudad desde `dim geografia`; producto ERP desde `dim servicio[nombre plan]`; estado y tipo de persona desde `dim cliente` cuando esos nombres exactos estén confirmados en el PBIX.
- No colocar filtros de plan ISP como si fueran productos facturados.

#### KPI superiores

| KPI | Campo/medida | Estado |
|---|---|---|
| Clientes atendidos | `[Clientes Atendidos]` | Existente |
| Clientes nuevos observados | Distinct count de `sk_cliente` cuya `[Fecha Inicio Operacion]` cae en el periodo | Medida nueva; validar implementación |
| Ingresos | `[Ingresos]` | Existente |
| Ticket promedio | `[Ingresos] / [Clientes Atendidos]` | Medida nueva; titular “Ingreso promedio por sucursal atendida” para evitar ambigüedad |
| Cartera total | `[Saldo Cartera]` | Existente |
| Cartera vencida | `[Cartera Vencida]` | Existente |
| Clientes actualmente inactivos | `[Clientes Actualmente Inactivos]` | Existente Gold |

Cada tarjeta debe mostrar valor, comparación seleccionada, porcentaje de variación y semáforo consciente de la dirección del KPI. No debe llenarse la fila con más de siete KPI.

#### Visuales

1. **Evolución de clientes:** eje `dim tiempo dax[Año-Mes]` (nombre exacto a confirmar); valores `[Clientes Atendidos]` y clientes nuevos observados. Comparación PM/PY seleccionable mediante parámetro o botones.
2. **Ingresos mensuales:** eje temporal; `[Ingresos]`; línea del periodo comparable o tooltip con PM, PY y acumulados.
3. **Ingresos por producto ERP:** `dim servicio[nombre plan]` + `[Ingresos]`; barras horizontales Top N.
4. **Distribución geográfica:** usar el visual ya probado en Capilaridad o enlazar esa página; no duplicar un mapa sin valor adicional.
5. **Top clientes por ingresos:** `dim cliente[razon social]`, identificador/NIT y `[Ingresos]`; Top 10.
6. **Estado de cartera:** `[Cartera No Vencida]` y `[Cartera Vencida]`; barra apilada o donut pequeño.
7. **Señales transaccionales:** `[Clientes Actualmente Inactivos]`, `[Deserciones Transaccionales Observadas]`, `[Recuperaciones Transaccionales]`; tarjetas secundarias o barras, nunca “Health Score”.

#### Interacciones

- Periodo, geografía, producto y atributos de cliente filtran KPI, tendencias y rankings.
- Seleccionar un cliente en Top clientes debe permitir drillthrough a Perfil del cliente.
- Seleccionar una región/producto cruza las visualizaciones sin afectar la navegación.
- Debe existir botón “Restablecer filtros”.

### Página 2 — Perfil del cliente

**Pregunta:** ¿Quién es el cliente seleccionado, qué tiene contratado, cuánto factura, qué debe y cómo paga?

#### Selectores

- Principal: `dim cliente[razon social]` con selección única recomendada.
- Alternativo: NIT/documento desde el campo validado de `dim cliente`; no crear relación por NIT.
- Sucursal: `dim cliente[idsuc]` si un NIT posee varias sucursales.
- No usar `dim tiempo dax` como filtro global de cartera/pagos porque esas facts nuevas no están relacionadas al calendario existente.

#### Encabezado/ficha

- `dim cliente[razon social]`
- NIT/documento de `dim cliente`
- tipo de persona, estado e `idsuc`
- ubicación disponible: ciudad, municipio, departamento, barrio y dirección desde cliente/geografía según el campo realmente expuesto en el modelo
- `dim perfil cartera[denominacion]`
- `[Fecha Inicio Operacion]` titulada “Primera facturación”
- `[Ultima Fecha Pago]`

#### KPI

- `[Ingresos]`
- `[Clientes Atendidos]` titulada “Sucursales facturadas” solo en contexto de persona; omitir si siempre vale 1.
- `[Saldo Cartera]`
- `[Cartera Vencida]`
- `[Cartera No Vencida]`
- `[Pago Aplicado]` titulado “Pago caja aplicado”
- `[Pago Pasarela]`
- `[Contratos]`
- `[Planes ISP]`

#### Visuales y campos exactos documentados

| Visual | Campos |
|---|---|
| Evolución de ingresos | fecha/mes de `fact facturacion` o calendario existente + `[Ingresos]` |
| Productos facturados | `dim servicio[nombre plan]` + `[Ingresos]` o suma de venta validada |
| Contratos | `dim contrato[public_id]`, `[state]`, `[start_date]`, `[address_city]`, `[idcontrato]` |
| Planes ISP | `dim plan[nombre]`, `[ceil_down_kbps]`, `[ceil_up_kbps]`, `[precio]`, `[frequency_in_months]` |
| Cartera | `fact cartera[prefijo]`, `[numero]`, `[fecha_vencimiento]`, `[dias]`, `[saldo]` |
| Pagos aplicados | `fact pago aplicacion[prefijo]`, `[numero]`, `[rc_prefijo]`, `[rc_numero]`, `[fecha_recibo]`, `[carteraaplicado]` |
| Pagos pasarela | `fact pago pasarela[fecha_operacion]`, `[codigo_respuesta]`, `[total]`, `[referencia]`, `[numero_autorizacion]` |
| Medio pasarela | `fact pago pasarela[codigo_respuesta]` + `[Pago Pasarela]` |

`codigo_respuesta` representa el medio registrado (PSE, NEQUI, CARD, etc.), no un código HTTP. `dim servicio[nombre plan]` es producto ERP; `dim plan[nombre]` es plan ISP. Deben mantenerse separados.

#### Interacciones

- Cliente y sucursal deben filtrar todos los KPI y tablas 360.
- Una fila de contrato filtra o resalta el plan solo mediante los bridges validados.
- Las tablas largas deben usar drillthrough/tooltip o desplazamiento, no ocupar toda la página.
- Botones: Resumen, Comportamiento, Volver y Restablecer selección.

### Página 3 — Comportamiento y riesgo observado

**Pregunta:** ¿Cómo ha cambiado el comportamiento del cliente y qué señales observables requieren atención?

#### Filtros

- Cliente sincronizado con Página 2.
- Sucursal cuando aplique.
- Rango/mes de análisis proveniente de la tabla Gold mensual, no forzado desde `dim tiempo dax` si no existe relación válida.
- Estado transaccional y nivel de confianza.

#### KPI

- `[Clientes con Episodio]`
- `[Episodios de Inactividad]`
- `[Deserciones Transaccionales Observadas]`
- `[Recuperaciones Transaccionales]`
- `[% Recuperación Transaccional]`
- `[Días Inactivos Promedio]`
- `[Clientes Actualmente Inactivos]`
- `[Episodios de Interrupción de Pago]`
- `[Interrupciones de Pago Abiertas]`
- `[Días Sin Pago Promedio]`

Usar como máximo seis KPI principales visibles y llevar el resto a una banda secundaria o tooltip.

#### Visuales

1. **Estado transaccional mensual:** `vw_anl_estado_transaccional_mensual_cliente[mes]` por `[estado_transaccional]`, usando conteo distinto de `sk_cliente` o medidas mensuales ya existentes.
2. **Deserción y recuperación observadas:** mes + `[Clientes en Deserción Transaccional Observada Mes]` y `[Clientes en Recuperación Transaccional Observada Mes]`.
3. **Interrupción de pago:** mes + `[Clientes en Interrupción de Pago Mes]`.
4. **Duración de episodios:** distribución de `dias_inactivo` o `meses_inactivo`; segmentar abierto/recuperado con `reconecto`.
5. **Detalle de episodios:** `fecha_ultima_factura_previa`, `fecha_inicio_inactividad`, `fecha_primera_actividad_posterior`, `dias_inactivo`, `reconecto`, `motivo_inferido`, `nivel_confianza`.
6. **Actividad y pagos:** `facturas_mes`, `ingresos_mes`, `valor_pago_aplicado`, `valor_pago_pasarela`; señales separadas, sin sumar los dos canales.

#### Terminología obligatoria

- “Vinculación observada” o “primera facturación”, no alta contractual.
- “Deserción transaccional observada”, no churn certificado.
- “Recuperación transaccional observada”, no reconexión ISP.
- `fecharetiroisp` es evidencia complementaria, no detonante automático de churn.
- Un pago posterior a la última factura no prueba que el servicio esté activo.

## 7. Medidas temporales nuevas necesarias

Antes de crearlas se debe auditar nuevamente el PBIX TEST para evitar duplicados. Para cada KPI aditivo o de conteo aprobado se requiere el siguiente patrón de medidas:

- `[KPI Periodo Actual]`
- `[KPI Periodo Anterior]`
- `[KPI Mismo Periodo Año Anterior]`
- `[KPI YTD]`
- `[KPI YTD Año Anterior]`
- `[KPI Var % vs Periodo Anterior]`
- `[KPI Var % vs Año Anterior]`
- `[KPI Var % YTD]`
- `[KPI Color Semáforo]`
- `[KPI Texto Comparación]`

Aplicar inicialmente a `[Ingresos]`, `[Clientes Atendidos]` y clientes nuevos observados. Para cartera, pagos y ciclo de vida, primero se debe verificar si el modelo conserva histórico por periodo. `fact cartera` es snapshot: no debe fingirse una comparación histórica de cartera si no existe snapshot mensual comparable.

## 8. Filtros y navegación global

- Barra lateral fija en las tres páginas con botones Resumen, Perfil y Comportamiento.
- Resaltar la página activa.
- Botón de Capilaridad únicamente como enlace al activo existente.
- Botón Restablecer filtros mediante marcador.
- Sincronizar solo los slicers cuya semántica y relaciones funcionen en todas las páginas.
- Cliente se sincroniza entre Perfil y Comportamiento; en Resumen puede permanecer sin selección para conservar la visión general.
- Incluir tooltip de definición en KPI sensibles: clientes nuevos, ticket/ingreso promedio, cartera vencida y deserción observada.
- Mantener accesibilidad: contraste suficiente, orden de tabulación, texto alternativo y no depender exclusivamente del color.

## 9. Layout y sistema visual

- Lienzo recomendado: 16:9; confirmar 1280×720 o 1366×768 según estándar corporativo.
- Barra lateral: aproximadamente 15% del ancho.
- Encabezado: 10–12% de la altura.
- Tarjetas: una banda superior de 5–7 KPI.
- Zona analítica: cuadrícula de 12 columnas con márgenes y separaciones constantes.
- Fondo general gris azulado muy claro; contenedores blancos.
- Azul GuajiraNet para navegación y series principales.
- Verde/amarillo/rojo reservados para estado y semáforo.
- Máximo dos familias tipográficas y tres tamaños jerárquicos principales.
- Evitar sombras fuertes, degradados excesivos, bordes gruesos y gráficos 3D.
- Formatos: COP abreviado y consistente; porcentajes con una decimal; fechas `dd MMM yyyy`; cantidades con separador de miles.

## 10. Reparto realista del trabajo

| Actor | Puede hacer | No debe asumirse |
|---|---|---|
| ChatGPT Work/IA | Analizar requisitos, definir blueprint, redactar DAX/M/SQL, revisar capturas, diseñar fondos/prototipos y QA semántico | No prueba por sí solo que un visual local quedó bien ni accede mágicamente al PBIX |
| Cursor Pro | Ingeniería principal: SQL, DAX, M, Python, Hop, repo, auditorías, scripts y documentación | No editar visuales de un PBIX binario tradicional como si fueran archivos de código |
| Codex en este entorno | Leer/escribir archivos locales disponibles, generar artefactos, ejecutar validaciones y preparar recursos | En esta sesión no hay acceso al escritorio Windows, Computer Use ni herramienta Power BI; no puede abrir o modificar físicamente el PBIX local |
| Rayhan | Abrir el PBIX TEST, ejecutar los clics de Power Query/modelo/visuales cuando no haya vía automatizada, validar con credenciales, guardar/publicar y presentar avances | No debe reconstruir manualmente lógica que ya puede prepararse como DAX/M/SQL |

### Capacidades verificadas en esta sesión

- Hay ejecución local de archivos y generación de artefactos.
- No está expuesto un conector de Microsoft Power BI.
- No está expuesta una sesión de navegador autenticada ni control del escritorio Windows.
- No está disponible el archivo `Guajiranet_COMPAT_V2_TEST.pbix` en los adjuntos actuales.
- Por tanto, esta sesión puede planificar y preparar recursos, pero no editar visuales físicamente ni verificar el modelo interno del PBIX.

Si posteriormente se habilita Power BI en navegador, Computer Use o se aporta un proyecto PBIP/PBIR editable, se vuelve a evaluar la automatización antes de asignar trabajo manual.

## 11. Plan de ejecución estimado

La referencia histórica aprobada es 14 horas. Con el alcance concreto de la reunión, 14 horas sigue siendo una meta realista pero ajustada, siempre que no aparezcan problemas de relaciones/datos y que la validación diaria sea rápida.

| Fase | Trabajo | Responsable principal | Horas |
|---|---|---|---:|
| 1 | Confirmación del blueprint, canvas y semáforos | Work + Rayhan + jefe | 1,0 |
| 2 | Auditoría puntual del PBIX TEST: páginas, medidas y campos reales | Rayhan + Cursor/IA | 1,5 |
| 3 | DAX temporal, textos y colores; validación de snapshots | Cursor + IA | 2,0 |
| 4 | Prototipo/fondo de las tres páginas y aprobación visual | Work/IA + Rayhan | 1,5 |
| 5 | Montaje de Resumen ejecutivo | Rayhan; automatización si aparece | 2,0 |
| 6 | Reorganización de Perfil del cliente | Rayhan; reutilización de visuales | 1,5 |
| 7 | Reorganización de Comportamiento y riesgo | Rayhan; Gold existente | 1,5 |
| 8 | Navegación, slicers, interacciones y tooltips | Rayhan | 1,0 |
| 9 | QA funcional, visual, rendimiento y no regresión | Rayhan + IA/Cursor | 1,5 |
| 10 | Correcciones finales, captura y versión de entrega | Rayhan | 0,5 |
|  | **Total meta** |  | **14,0** |

### Escenarios

- **Optimista:** 11–12 horas, si las comparaciones existentes cubren gran parte del trabajo y no hay errores de modelo.
- **Realista:** 14–16 horas, incluyendo una ronda normal de comentarios.
- **Conservador:** 18–20 horas, si hay que corregir relaciones, construir varias medidas temporales o responder a cambios de alcance.

Los cambios posteriores a la aprobación del blueprint deben registrarse aparte para no absorberlos dentro de las 14 horas.

## 12. Secuencia de trabajo hasta la entrega

1. Aprobar este blueprint y resolver las decisiones abiertas.
2. Abrir únicamente `Guajiranet_COMPAT_V2_TEST.pbix` y cancelar actualizaciones automáticas no previstas.
3. Inventariar medidas, nombres reales de campos y páginas; no modificar todavía.
4. Construir/validar únicamente el DAX faltante.
5. Crear prototipo visual limpio de las tres páginas y enviar primera captura.
6. Montar primero Resumen, luego Perfil y finalmente Comportamiento.
7. Configurar navegación, marcadores, tooltips e interacciones.
8. Probar casos generales, cliente de una sucursal y cliente multisucursal.
9. Verificar resultados con y sin filtros, ausencia de dobles conteos y rendimiento.
10. Enviar avance diario, registrar observaciones y cerrar solo cambios aprobados.
11. Guardar y publicar únicamente conforme al flujo autorizado.

## 13. Decisiones abiertas antes de tocar Power BI

1. Confirmar canvas corporativo: 1280×720 o 1366×768.
2. Confirmar si “cliente” ejecutivo significa persona/NIT o sucursal facturada; el `sk_cliente` actual equivale a sucursal en varias capas.
3. Confirmar la regla de semáforo propuesta y el tratamiento de exactamente ±10%.
4. Confirmar si el jefe quiere selector de comparación o las tres comparaciones simultáneas.
5. Confirmar si Capilaridad se mantiene como cuarta página enlazada o fuera del entregable Customer 360.
6. Confirmar si el refresh de la tabla Gold materializada ya fue conectado después de Silver v2.
7. Confirmar si la entrega del jueves incluye publicación en Power BI Service o solo PBIX validado.

## 14. Criterios de aceptación

### Funcionales

- Existen las tres páginas mínimas solicitadas.
- El filtro de cliente/documento actualiza coherentemente Perfil y Comportamiento.
- Resumen abre sin cliente seleccionado y conserva la vista general.
- Cada visual temporal aprobado ofrece PM, PY y YTD/PYTD de manera verificable.
- No se crean relaciones por NIT, `sk_persona`, `idcliente` o `plan_id`.
- No se relacionan las facts nuevas al calendario si ello vacía cartera/pagos.
- No se usa `SUM(pagorc)` ni se suman Pago Aplicado y Pago Pasarela.
- Producto ERP y plan ISP están claramente diferenciados.
- Los estados y fechas de retiro no se presentan como churn certificado.

### Visuales

- Diseño 16:9 coherente en las tres páginas.
- Navegación consistente, página activa visible y botón de restablecer.
- Jerarquía ejecutiva clara: KPI, tendencia, composición y detalle.
- No hay objetos superpuestos, textos cortados ni tablas ilegibles.
- Colores de semáforo respetan la dirección favorable de cada KPI.
- La página sigue siendo comprensible sin depender solo del color.

### Datos y rendimiento

- Conteos y valores se contrastan con visuales/páginas existentes y consultas de control.
- Se prueba al menos un cliente conocido, uno multisucursal y un caso sin cartera o sin pagos.
- Capilaridad y las cuatro consultas originales permanecen sin regresión.
- El refresh y la navegación tienen tiempos aceptables; episodios no debe consumir la vista lenta si se autorizó y validó la tabla física.
- Se muestra el estado de actualización sin convertir Bronze en alarma ejecutiva.

### Seguridad

- Solo se modifica `Guajiranet_COMPAT_V2_TEST.pbix`.
- No se toca Delta, Silver v1, scripts productivos protegidos ni el PBIX original.
- No se publican secretos ni credenciales.
- No se ejecutan los SQL de cutover 05/06/07.

## 15. Veredicto

La arquitectura y las métricas base son suficientes para construir un Customer 360 ejecutivo sólido. El mayor trabajo pendiente está en comparaciones temporales, diseño, navegación, interacción y QA. La ruta recomendada es aprobar primero el prototipo de las tres páginas y después montar sobre los activos actuales. No se justifica rehacer el modelo ni inventar métricas para imitar la referencia.
