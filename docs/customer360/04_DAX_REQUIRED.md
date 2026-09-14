# Customer 360 — DAX requerido

## Regla previa

Antes de crear cualquier medida, Cursor debe auditar las medidas existentes en `Guajiranet_COMPAT_V2_TEST.pbix` para evitar duplicados y documentar equivalencias. Este documento registra pendientes; no contiene fórmulas.

## Pendientes

- [ ] Clientes nuevos observados.
- [ ] Ingreso promedio por sucursal atendida.
- [ ] Periodo anterior (PM) por KPI temporal aprobado.
- [ ] Mismo periodo del año anterior (PY).
- [ ] Acumulado del año (YTD).
- [ ] Acumulado equivalente del año anterior (PYTD).
- [ ] Variaciones porcentuales frente a PM, PY y PYTD.
- [ ] Texto dinámico de comparación seleccionada.
- [ ] Semáforo con umbral ±10%.
- [ ] Lógica invertida para indicadores de riesgo.
- [ ] Auxiliares para selección única de persona/NIT y sucursal.
- [ ] Estados vacíos cuando no exista cliente seleccionado.
- [ ] Mensajes `Sin dato` y `Sin comparación`.
- [ ] Títulos dinámicos y auxiliares de tooltip.

## Restricciones

- No crear comparaciones históricas de cartera mientras sea solo snapshot.
- No sumar Pago Aplicado y Pago Pasarela.
- No usar `SUM(pagorc)`.
- No convertir primera facturación en vinculación contractual.
- No llamar churn certificado a la deserción observada.
