-- Validación final del modelo (5 puntos) — solo SELECT
-- Evidencia: discovery/12_final_model_validation.md

-- 1) seller_id / neighborhood_id vs catálogos ERP
SELECT
  COUNT(*) AS filas,
  COUNT(*) FILTER (WHERE datajson->>'seller_id' IS NULL) AS seller_null,
  COUNT(DISTINCT datajson->>'seller_id') FILTER (WHERE COALESCE(datajson->>'seller_id','') <> '') AS seller_distinct,
  COUNT(*) FILTER (WHERE datajson->>'neighborhood_id' IS NULL) AS neigh_null,
  COUNT(DISTINCT datajson->>'neighborhood_id') FILTER (WHERE datajson->>'neighborhood_id' IS NOT NULL) AS neigh_distinct
FROM bronze_guajiranet.tmjsonclient;

SELECT COUNT(*) AS vendedores FROM bronze_guajiranet.mavendedores;
SELECT COUNT(*) AS barrios FROM bronze_guajiranet.mabarrio;

-- 2) idgenero
SELECT COUNT(*) AS filas,
       COUNT(*) FILTER (WHERE idgenero IS NULL) AS nulos,
       COUNT(*) FILTER (WHERE idgenero = '') AS vacios,
       COUNT(DISTINCT idgenero) FILTER (WHERE idgenero IS NOT NULL) AS distinct_no_nulos
FROM bronze_guajiranet.materceros;

-- 3) geografía canónica
SELECT COUNT(*) AS mabarrio FROM bronze_guajiranet.mabarrio;
SELECT COUNT(*) AS departamentos FROM bronze_guajiranet.madepartamentos;
SELECT
  COUNT(*) FILTER (WHERE s.idbarrio IS NOT NULL) AS suc_barrio_nn,
  COUNT(*) FILTER (WHERE s.idbarrio IS NOT NULL AND b.idbarrio IS NULL) AS suc_barrio_huerfano
FROM bronze_guajiranet.matercerosuc s
LEFT JOIN bronze_guajiranet.mabarrio b ON b.idbarrio = s.idbarrio;

-- 4) CRM no es vinculación ISP
SELECT MIN(fecha) AS min_fecha, MAX(fecha) AS max_fecha, COUNT(*) AS filas,
       COUNT(DISTINCT nit) AS nits
FROM bronze_guajiranet.trcrmoportunidad;

SELECT MIN((datajson->>'start_date')::date) AS min_start,
       MAX((datajson->>'start_date')::date) AS max_start
FROM bronze_guajiranet.tmjsoncontract;

-- 5) factura no tiene FK a contrato/plan ISP
SELECT COUNT(*) AS facturas,
       COUNT(*) FILTER (WHERE COALESCE(doccontrato, '') <> '') AS doccontrato_lleno
FROM bronze_guajiranet.trfacturas;
