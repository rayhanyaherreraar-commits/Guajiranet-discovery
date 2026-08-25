-- Auditoría de solo lectura: contrato JSON, UUID cliente, plan tipo P
-- Evidencia: discovery/02_lookup_idcontrato.md, 03_lookup_idcliente.md, 04_lookup_plan_id.md, 08, 09, 10

-- idcontrato sucursal vs tmjsoncontract
WITH suc AS (
  SELECT DISTINCT idcontrato
  FROM bronze_guajiranet.matercerosuc
  WHERE idcontrato IS NOT NULL
)
SELECT
  (SELECT COUNT(*) FROM suc) AS suc_keys,
  (SELECT COUNT(*) FROM bronze_guajiranet.tmjsoncontract) AS json_rows,
  (SELECT COUNT(*) FROM suc s JOIN bronze_guajiranet.tmjsoncontract c USING (idcontrato)) AS ambas,
  (SELECT COUNT(*) FROM suc s LEFT JOIN bronze_guajiranet.tmjsoncontract c USING (idcontrato) WHERE c.idcontrato IS NULL) AS solo_suc,
  (SELECT COUNT(*) FROM bronze_guajiranet.tmjsoncontract c LEFT JOIN suc s USING (idcontrato) WHERE s.idcontrato IS NULL) AS solo_json;

-- idcliente contrato vs tmjsonclient / materceros
SELECT
  (SELECT COUNT(DISTINCT idcliente) FROM bronze_guajiranet.tmjsoncontract) AS contract_clients,
  (SELECT COUNT(DISTINCT c.idcliente)
     FROM bronze_guajiranet.tmjsoncontract c
     JOIN bronze_guajiranet.tmjsonclient j ON j.idcliente = c.idcliente) AS match_jsonclient,
  (SELECT COUNT(DISTINCT c.idcliente)
     FROM bronze_guajiranet.tmjsoncontract c
     JOIN bronze_guajiranet.materceros t ON t.idcliente = c.idcliente) AS match_materceros;

-- 11 filas: UUID contrato vs UUID tercero por nit de sucursal
SELECT s.idcontrato, c.idcliente AS json_idcliente, s.nit, s.idsuc,
       t.idcliente AS terceros_idcliente, t.razonsocial
FROM bronze_guajiranet.matercerosuc s
JOIN bronze_guajiranet.tmjsoncontract c ON c.idcontrato = s.idcontrato
JOIN bronze_guajiranet.materceros t ON t.nit = s.nit
WHERE c.idcliente IS DISTINCT FROM t.idcliente
ORDER BY s.nit, s.idsuc;

-- plan_id → tmjsonplan_server tipo P
WITH plans AS (
  SELECT DISTINCT datajson->>'plan_id' AS plan_id
  FROM bronze_guajiranet.tmjsoncontract
)
SELECT
  (SELECT COUNT(*) FROM plans) AS distinct_plan_id,
  (SELECT COUNT(*) FROM plans p
     JOIN bronze_guajiranet.tmjsonplan_server s
       ON s.tipo = 'P' AND s.datajson->>'id' = p.plan_id) AS matched_tipo_p;

-- claves JSON contrato (muestra de keys en una fila)
SELECT jsonb_object_keys(datajson) AS key
FROM bronze_guajiranet.tmjsoncontract
LIMIT 1;

-- overlap UUID plan vs producto ERP (esperado 0)
SELECT COUNT(*) AS overlap
FROM bronze_guajiranet.trfacturasdet d
JOIN bronze_guajiranet.tmjsonplan_server p
  ON p.tipo = 'P' AND p.datajson->>'id' = d.idproducto::text;
