-- Cutover Gold: capturar definiciones ANTES de cualquier DROP
-- Plan: discovery/13_cutover_silver_plan.md
-- No ejecuta DROP. Solo lectura.

SELECT n.nspname, c.relname, c.relkind, pg_get_viewdef(c.oid, true) AS viewdef
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'gold_guajiranet'
  AND c.relkind IN ('v', 'm')
ORDER BY 2;

-- Dependencias hacia facts/dims Silver (completar filtros si hace falta)
SELECT DISTINCT
  n.nspname AS src_schema,
  c.relname AS src_object,
  n2.nspname AS dep_schema,
  c2.relname AS dep_object
FROM pg_depend d
JOIN pg_rewrite r ON r.oid = d.objid
JOIN pg_class c ON c.oid = r.ev_class
JOIN pg_namespace n ON n.oid = c.relnamespace
JOIN pg_class c2 ON c2.oid = d.refobjid
JOIN pg_namespace n2 ON n2.oid = c2.relnamespace
WHERE n.nspname = 'gold_guajiranet'
  AND n2.nspname = 'silver_guajiranet'
ORDER BY 1, 2, 4;
