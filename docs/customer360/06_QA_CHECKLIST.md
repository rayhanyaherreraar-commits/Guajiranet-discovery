# Customer 360 — Checklist de QA

## DAX V1 — ejecución 2026-09-14

- [x] Tabla desconectada `KPI Customer360` creada con 9 filas, 3 KPI, PM/PY/YTD, dirección favorable y orden.
- [x] 15 medidas creadas en `_medidas clientes 360`.
- [x] 16 escenarios de prueba ejecutados mediante XMLA local.
- [x] Resultado final: 16 aprobados y 0 fallos.
- [x] Periodo con datos y periodo sin PM comparable probados.
- [x] PY, YTD y PYTD probados para los tres KPI.
- [x] NIT de una sucursal y NIT multisucursal probados.
- [x] `Clientes Nuevos Observados` cuenta una vez el NIT multisucursal.
- [x] Ausencia de cliente seleccionado y mensaje de Perfil probados.
- [x] División por cero conserva `BLANK()` sin error.
- [x] Filtros directos sobre `dim tiempo dax[Fecha]` no producen errores.
- [x] Selector PM/PY/YTD devuelve valor y texto coherentes.
- [x] Semáforo probado con dirección favorable, dirección inversa y límites exactos ±10%.
- [x] Sin comparativo devuelve texto `Sin comparación` y color gris.
- [x] Tabla calculada materializada mediante `Calculate` exclusivo después de detectar 9 filas sin procesar.
- [x] Sin relaciones desde `KPI Customer360`.
- [x] Sin medidas temporales de cartera ni KPI Total Pagos.
- [x] PBIX abierto en Power BI Desktop con el modelo modificado correctamente.

## Visual

- [ ] Tres páginas nuevas en 1366 × 768, 16:9.
- [ ] Sin solapamientos, cortes de texto ni objetos fuera del canvas.
- [ ] Navegación, encabezados, márgenes y tipografía consistentes.
- [ ] Jerarquía KPI → tendencia → composición/ranking → detalle.
- [ ] Semáforos ±10% con inversión para riesgos.
- [ ] Estados sin dato no aparecen como cero inventado.
- [ ] Información comprensible sin depender solo del color.
- [ ] Sin NPS, churn certificado, Health Score ni Next Best Action.

## Datos

- [ ] Medidas existentes auditadas antes de crear nuevas.
- [ ] Ingresos y clientes contrastados con controles existentes.
- [ ] Primera facturación no se presenta como vinculación contractual.
- [ ] Producto ERP y plan ISP están separados.
- [ ] Conteos distinguen persona/NIT de sucursal.
- [ ] Formatos COP, porcentaje, fecha y cantidades son consistentes.

## Interacciones y filtros

- [ ] Cliente/NIT filtra Perfil y Comportamiento.
- [ ] Sucursal reduce detalle sin alterar el modelo físico.
- [ ] Un mes solo afecta facts con relación temporal válida.
- [ ] Producto ERP no filtra contratos/planes con relación no validada.
- [ ] Contrato filtra plan únicamente mediante bridges validados.
- [ ] Drillthrough Resumen → Perfil conserva el contexto correcto.
- [ ] Perfil → Comportamiento conserva cliente/sucursal.
- [ ] Resumen abre sin cliente individual seleccionado.
- [ ] Perfil muestra instrucción sin selección única.
- [ ] Comparación PM/PY/YTD afecta solo KPI compatibles.
- [ ] Restablecer filtros devuelve el estado aprobado.
- [ ] `dim tiempo dax` no vacía cartera ni pagos.

## Navegación

- [ ] Botones Resumen, Perfil, Comportamiento y Capilaridad funcionan.
- [ ] Página activa claramente resaltada.
- [ ] Capilaridad enlazada sin rediseño.
- [ ] Tooltips ocultos de la navegación.
- [ ] Marcadores de Pagos y Restablecer preservan filtros pertinentes.

## Rendimiento

- [ ] Apertura y cambios de filtro tienen tiempos aceptables.
- [ ] Episodios usan la tabla Gold solo si refresh e igualdad están validados.
- [ ] No se consulta innecesariamente la vista lenta de episodios.
- [ ] Top N y columnas visibles respetan la especificación.
- [ ] Sin relaciones ambiguas o bidireccionales adicionales.

## Multisucursal

- [ ] Probado cliente de una sucursal.
- [ ] Probado cliente multisucursal.
- [ ] Total por persona/NIT no duplica valores.
- [ ] Selector ofrece todas las sucursales cuando aplica.
- [ ] Drillthrough conserva el grano correcto.
- [ ] Probado cliente sin cartera, pagos o contrato.

## Snapshots

- [ ] Cartera rotulada `Corte actual`.
- [ ] Sin PM/PY/YTD de cartera sin snapshots comparables.
- [ ] Un clic temporal no genera cartera cero falsa.
- [ ] Tooltip muestra fecha de corte y condición snapshot.

## Pagos

- [ ] Pago aplicado usa `carteraaplicado`.
- [ ] No existe `SUM(pagorc)`.
- [ ] Pago Aplicado y Pago Pasarela permanecen separados.
- [ ] No existe KPI que sume ambos canales.
- [ ] `codigo_respuesta` se presenta como medio registrado.
- [ ] Última fecha de pago explica/distingue canales.

## Gold

- [ ] Refresh de `tbl_anl_episodios_ciclo_vida_cliente` verificado.
- [ ] Tabla actualizada después de Silver v2 exitoso.
- [ ] Conteos, duplicados y diferencias contra la vista validados.
- [ ] Power BI consume la tabla solo tras validar.
- [ ] Estado de actualización no convierte Bronze en alarma ejecutiva.
- [ ] Semántica transaccional observada preservada.

## Seguridad y no regresión

- [ ] Solo se modificó `Guajiranet_COMPAT_V2_TEST.pbix`.
- [ ] `Guajiranet (1).pbix` intacto.
- [ ] Delta, Silver v1, runners, workflows y SQL productivos intactos.
- [ ] No se ejecutaron cutovers 05/06/07.
- [ ] Sin relaciones por NIT, `sk_persona`, `idcliente` o `plan_id`.
- [ ] Cuatro consultas originales intactas.
- [ ] Capilaridad sin regresiones.
- [ ] Sin secretos, credenciales, `.env` o datos sensibles.
- [ ] Service publicado solo con autorización y sin comprometer entrega.
