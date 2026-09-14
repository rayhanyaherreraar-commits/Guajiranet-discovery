# Customer 360 — Registro de implementación

## Inicialización

- **Fecha:** 2026-09-14
- **Estado:** blueprint, decisiones y especificación visual aprobados; implementación Power BI no iniciada.
- **PBIX autorizado:** `Guajiranet_COMPAT_V2_TEST.pbix`
- **Próximo paso:** auditoría puntual en Cursor del PBIX TEST y del refresh Gold, sin cambios productivos.

## Regla

Cada cambio posterior debe registrar fecha, archivo/modificación, responsable, motivo, validación y resultado.

| Fecha | Archivo/modificación | Responsable | Motivo | Validación | Resultado |
|---|---|---|---|---|---|
| 2026-09-14 | Inicialización de documentación Customer 360 | Work | Preservar el trabajo aprobado y trasladar la ejecución a Cursor | Revisión de estructura y restricciones | Listo para copiar al repositorio Discovery |
| 2026-09-14 | Modelo semántico del PBIX TEST: tabla desconectada `KPI Customer360` y 15 medidas en `_medidas clientes 360` | Cursor | Implementar la V1 DAX reducida para KPI temporales, selector PM/PY/YTD, semáforos y estados vacíos | 16 escenarios mediante XMLA local: periodos con/sin comparables, PY, YTD/PYTD, NIT simple/multisucursal, estado vacío, división por cero, fecha directa, selector y semáforos | 16 aprobados, 0 fallos finales. Se aplicó `Calculate` únicamente a la tabla desconectada para materializar sus 9 filas. El PBIX quedó abierto y modificado correctamente; sin cambios en visuales, relaciones, Power Query ni capas de datos |
