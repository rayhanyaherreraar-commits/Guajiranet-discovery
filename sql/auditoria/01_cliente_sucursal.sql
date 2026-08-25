-- Auditoría de solo lectura: persona ↔ sucursal ISP
-- Schema: bronze_guajiranet
-- Medición de referencia: 2026-08-24 (ver discovery/01_relacion_matercerosuc_materceros.md)

-- NK sucursal
SELECT COUNT(*) AS filas,
       COUNT(DISTINCT (nit, idsuc)) AS nk,
       COUNT(DISTINCT nit) AS nits
FROM bronze_guajiranet.matercerosuc;

-- NK persona
SELECT COUNT(*) AS filas,
       COUNT(DISTINCT nit) AS nits
FROM bronze_guajiranet.materceros;

-- Cobertura nit hijo → padre (esperada 100%)
SELECT
  COUNT(*) FILTER (WHERE t.nit IS NULL) AS suc_sin_tercero,
  COUNT(*) FILTER (WHERE t.nit IS NOT NULL) AS suc_con_tercero
FROM bronze_guajiranet.matercerosuc s
LEFT JOIN bronze_guajiranet.materceros t ON t.nit = s.nit;

-- Perfil cartera
SELECT s.idperfilcartera, p.denominacion, COUNT(*) AS filas
FROM bronze_guajiranet.matercerosuc s
LEFT JOIN bronze_guajiranet.maperfilcartera p ON p.id = s.idperfilcartera
GROUP BY 1, 2
ORDER BY filas DESC;
