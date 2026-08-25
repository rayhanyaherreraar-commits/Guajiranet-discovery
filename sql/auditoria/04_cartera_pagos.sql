-- Auditoría de solo lectura: L.1 cartera y L.2 pagos
-- Evidencia: discovery/evidencia/fact_cartera_pagos_audit.json
-- Grano acordado (2026-08-24):
--   FACT_CARTERA = latest tmcartera por ítem WHERE saldo <> 0
--   FACT_PAGO_APLICACION = DISTINCT vpagodiasfactura (factura, recibo), medida carteraaplicado
--   FACT_PAGO_PASARELA = trpagodigital.id
--   vfacturas_abono NO es fact de pagos; trformaspago NO se trata como recaudo

-- L.1 volúmenes
SELECT 'tmcartera' AS src, COUNT(*) FROM bronze_guajiranet.tmcartera
UNION ALL SELECT 'tmcartera_saldo_nz', COUNT(*) FROM bronze_guajiranet.tmcartera WHERE saldo <> 0
UNION ALL SELECT 'stg_fact_cartera', COUNT(*) FROM silver_guajiranet.stg_fact_cartera
UNION ALL SELECT 'tbl_fact_cartera', COUNT(*) FROM silver_guajiranet.tbl_fact_cartera;

-- Latest-open snapshot propuesto
SELECT COUNT(*) AS latest_open
FROM (
  SELECT DISTINCT ON (idsuc, prefijo, numero, cuenta, nit, sucursal, ref_doc, ref_num)
         saldo
  FROM bronze_guajiranet.tmcartera
  ORDER BY idsuc, prefijo, numero, cuenta, nit, sucursal, ref_doc, ref_num, fecha DESC
) q
WHERE saldo <> 0;

-- L.2 volúmenes
SELECT 'vpagodiasfactura' AS src, COUNT(*) FROM bronze_guajiranet.vpagodiasfactura
UNION ALL SELECT 'trpagodigital', COUNT(*) FROM bronze_guajiranet.trpagodigital
UNION ALL SELECT 'vfacturas_abono', COUNT(*) FROM bronze_guajiranet.vfacturas_abono
UNION ALL SELECT 'trformaspago', COUNT(*) FROM bronze_guajiranet.trformaspago
UNION ALL SELECT 'trfacturas', COUNT(*) FROM bronze_guajiranet.trfacturas;
