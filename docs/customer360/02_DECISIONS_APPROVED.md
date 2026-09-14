# Customer 360 — Decisiones aprobadas

**Estado:** cerradas para implementación.

1. Canvas 1366 × 768 px, formato 16:9.
2. Cliente ejecutivo = persona/NIT; sucursal = detalle operativo. No modificar físicamente el modelo.
3. Semáforos con umbral ±10%; invertir la lógica para indicadores donde subir es desfavorable.
4. Comparación seleccionable PM/PY/YTD en tarjeta; comparaciones adicionales mediante tooltip.
5. Capilaridad como cuarta página enlazada, sin rediseño.
6. Verificar el refresh de `gold_guajiranet.tbl_anl_episodios_ciclo_vida_cliente`; si está vigente, actualizada y validada, Power BI debe consumirla.
7. Entrega principal = `Guajiranet_COMPAT_V2_TEST.pbix` validado. Power BI Service es opcional.

Cualquier cambio posterior debe registrarse en `05_IMPLEMENTATION_LOG.md`.
