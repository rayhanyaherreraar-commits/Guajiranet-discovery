-- Auditoría de solo lectura: fecharetiroisp × perfil × activo
-- Evidencia: discovery/06_fecharetiroisp.md, 07_cruce_perfil_retiro.md

SELECT
  COUNT(*) AS total,
  COUNT(*) FILTER (WHERE fecharetiroisp IS NULL) AS fecha_null,
  COUNT(*) FILTER (WHERE fecharetiroisp IS NOT NULL) AS fecha_not_null,
  MIN(fecharetiroisp) AS min_fecha,
  MAX(fecharetiroisp) AS max_fecha
FROM bronze_guajiranet.matercerosuc;

SELECT fecharetiroisp, COUNT(*) AS filas
FROM bronze_guajiranet.matercerosuc
WHERE fecharetiroisp IS NOT NULL
GROUP BY 1
ORDER BY 1;

SELECT
  s.idperfilcartera,
  p.denominacion,
  COUNT(*) AS filas,
  COUNT(*) FILTER (WHERE s.fecharetiroisp IS NULL) AS fecha_null,
  COUNT(*) FILTER (WHERE s.fecharetiroisp IS NOT NULL) AS fecha_not_null
FROM bronze_guajiranet.matercerosuc s
LEFT JOIN bronze_guajiranet.maperfilcartera p ON p.id = s.idperfilcartera
GROUP BY 1, 2
ORDER BY 1 NULLS FIRST;

SELECT activo,
       COUNT(*) FILTER (WHERE fecharetiroisp IS NULL) AS fecha_null,
       COUNT(*) FILTER (WHERE fecharetiroisp IS NOT NULL) AS fecha_not_null
FROM bronze_guajiranet.matercerosuc
GROUP BY activo;

-- Otras columnas fecharetiroisp en el schema (esperado: solo matercerosuc)
SELECT table_name, column_name
FROM information_schema.columns
WHERE table_schema = 'bronze_guajiranet'
  AND (column_name ILIKE '%fecharetiroisp%' OR column_name ILIKE '%retiroisp%');
