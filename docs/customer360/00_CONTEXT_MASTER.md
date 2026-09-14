# GuajiraNet — Customer 360: contexto maestro

## Objetivo y estado

Reconstruir visualmente el Customer 360 sobre `Guajiranet_COMPAT_V2_TEST.pbix`, reutilizando lo existente. Están aprobados el blueprint, las siete decisiones y la especificación visual de tres páginas. La implementación en Power BI y el DAX nuevo aún no han iniciado.

## Arquitectura actual

`Bronze existente → Silver v1 protegido + Silver v2 → Gold analítico/físico validado → Power BI`.

Silver v2 corre de forma independiente después de Bronze/Silver v1. No debe encadenarse ni alterar el proceso productivo sin autorización.

## Silver v2 y modelo dimensional

- Dimensiones: persona, sucursal, contrato, plan, perfil de cartera, geografía v2, producto ERP; tiempo y documento reutilizadas.
- Bridges: `brg_persona_uuid`, `brg_sucursal_contrato`, `brg_contrato_plan`.
- Hechos: facturación v2, cartera v2, pago aplicación y pago pasarela.

La estrella existente conserva las relaciones activas de facturación hacia cliente, servicio, geografía y calendario. Las nuevas facts se filtran mediante cliente/sucursal y los bridges validados. No crear relaciones alternativas por NIT, `sk_persona`, `idcliente` o `plan_id`. No conectar facts nuevas al calendario a ciegas.

Cliente ejecutivo se presenta como persona/NIT y sucursal como detalle operativo, sin modificar físicamente el modelo. En varias capas `sk_cliente` representa operativamente una sucursal.

## Gold

Objetos principales:

- `vw_anl_ciclo_vida_parametros`
- `vw_anl_estado_transaccional_mensual_cliente`
- `vw_anl_episodios_ciclo_vida_cliente`
- `vw_anl_episodios_interrupcion_pago`
- `vw_anl_ciclo_vida_cliente_resumen`
- vistas de estado de actualización

La tabla `gold_guajiranet.tbl_anl_episodios_ciclo_vida_cliente` fue validada contra su vista, sin duplicados ni diferencias en la corrida documentada. Su refresh diario figuraba como propuesto. Cursor debe verificar que corra después de Silver v2, que esté vigente y que conserve igualdad; solo entonces Power BI debe consumirla.

## Medidas existentes

- Facturación: `Clientes Atendidos`, `Clientes Atendidos Mes Anterior`, `Ingresos`, `Venta Mes Actual`, `MoM% de Suma de venta` y otras medidas operativas.
- Customer 360: `Saldo Cartera`, `Cartera Vencida`, `Cartera No Vencida`, `Pago Aplicado`, `Pago Pasarela`, `Contratos`, `Planes ISP`, `Ultima Fecha Pago`.
- Ciclo de vida: clientes con episodio, episodios, deserciones y recuperaciones observadas, días inactivos, inactivos actuales, interrupciones/recuperaciones de pago y medidas mensuales.

Cursor debe auditar el PBIX TEST antes de crear medidas para evitar duplicados.

## Páginas existentes reutilizables

- Capilaridad: enlazar sin rediseñar.
- Cliente 360 Resumen: selector, KPI, evolución, productos e identificación.
- Cliente 360 Detalle: pagos, cartera, plan, aplicaciones y contrato.
- Vinculación/Deserción: base funcional de Comportamiento con terminología corregida.

El rechazo fue visual; los activos técnicos válidos siguen siendo reutilizables.

## Semántica obligatoria

- Primera facturación/vinculación observada no es alta contractual.
- Deserción transaccional observada es ausencia de facturación más allá del umbral; no es churn certificado.
- Recuperación transaccional observada es nueva factura después del episodio; no es reconexión ISP certificada.
- `fecharetiroisp` es evidencia complementaria y no dispara churn.
- Un pago posterior a la última factura no demuestra servicio activo.

## Pagos y cartera

`Pago Aplicado` usa `carteraaplicado` con grano factura × recibo. No usar `SUM(pagorc)`, pues el total del recibo puede repetirse. `Pago Pasarela` representa eventos digitales independientes; no es subconjunto del aplicado y ambos canales no deben sumarse. `codigo_respuesta` identifica el medio registrado.

`fact cartera v2` es snapshot del corte actual. No fabricar PM, PY o YTD de cartera sin snapshots históricos comparables; debe rotularse `Corte actual`.

## Restricciones y archivos protegidos

- Trabajar solo sobre `Guajiranet_COMPAT_V2_TEST.pbix`.
- No tocar `Guajiranet (1).pbix`, Delta, Silver v1, runners/workflows protegidos ni SQL de cutover 05/06/07.
- No rediseñar Silver ni repetir discovery.
- No publicar secretos, credenciales, `.env` ni datos sensibles.
- No inventar NPS, satisfacción, churn certificado, Health Score o Next Best Action.

## Responsabilidades

- Cursor: SQL, M, DAX, scripts, Hop, auditorías, Git y validación técnica.
- Work: blueprint, especificación visual y revisión de resultados.
- Power BI/Rayhan: montaje del PBIX TEST, validación, guardado y publicación autorizada.

## Próximo paso técnico

Auditar en Cursor el PBIX TEST y el refresh Gold sin modificar producción. Después registrar cada cambio en `05_IMPLEMENTATION_LOG.md`.
