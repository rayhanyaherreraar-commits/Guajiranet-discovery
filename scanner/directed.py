"""Auditorías dirigidas de solo lectura (reproducen el discovery semántico)."""
import os
from scanner.targeted import qi

SCHEMA_DEFAULT = "bronze_guajiranet"


def schema_name():
    return os.environ.get("DB_SCHEMA", SCHEMA_DEFAULT)


def qident(schema, table):
    return f"{qi(schema)}.{qi(table)}"


def fetchall_dicts(cur):
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def relate_matercerosuc_materceros(conn):
    schema = schema_name()
    suc, ter = qident(schema, "matercerosuc"), qident(schema, "materceros")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
              (SELECT COUNT(*) FROM {suc}) AS suc_rows,
              (SELECT COUNT(DISTINCT nit) FROM {suc}) AS suc_nits,
              (SELECT COUNT(*) FROM {ter}) AS ter_rows,
              (SELECT COUNT(DISTINCT nit) FROM {ter}) AS ter_nits,
              (SELECT COUNT(*) FROM {suc} s
                 LEFT JOIN {ter} t ON s.nit = t.nit
               WHERE t.nit IS NULL) AS suc_orphan_rows,
              (SELECT COUNT(*) FROM {ter} t
                 LEFT JOIN {suc} s ON t.nit = s.nit
               WHERE s.nit IS NULL) AS ter_without_suc
            """
        )
        coverage = fetchall_dicts(cur)[0]
        cur.execute(
            f"""
            SELECT COUNT(*) = COUNT(DISTINCT nit) AS nit_unique
            FROM {ter}
            """
        )
        coverage["parent_nit_unique"] = cur.fetchone()[0]
        cur.execute(
            f"""
            SELECT COUNT(*) = COUNT(DISTINCT (nit, idsuc)) AS nk_unique
            FROM {suc}
            """
        )
        coverage["child_nit_idsuc_unique"] = cur.fetchone()[0]
    return {"audit": "relate_matercerosuc_materceros", "schema": schema, **coverage}


def lookup_idcontrato(conn):
    schema = schema_name()
    suc, ctt = qident(schema, "matercerosuc"), qident(schema, "tmjsoncontract")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            WITH suc AS (
              SELECT idcontrato FROM {suc} WHERE idcontrato IS NOT NULL
            ),
            suc_keys AS (SELECT DISTINCT idcontrato FROM suc)
            SELECT
              (SELECT COUNT(*) FROM suc) AS suc_non_null,
              (SELECT COUNT(*) FROM suc_keys) AS suc_distinct,
              (SELECT COUNT(*) FROM {ctt}) AS contract_rows,
              (SELECT COUNT(*) FROM suc_keys k
                 JOIN {ctt} c ON c.idcontrato = k.idcontrato) AS both_keys,
              (SELECT COUNT(*) FROM suc_keys k
                 LEFT JOIN {ctt} c ON c.idcontrato = k.idcontrato
               WHERE c.idcontrato IS NULL) AS only_suc,
              (SELECT COUNT(*) FROM {ctt} c
                 LEFT JOIN suc_keys k ON c.idcontrato = k.idcontrato
               WHERE k.idcontrato IS NULL) AS only_json
            """
        )
        return {"audit": "lookup_idcontrato", "schema": schema, **fetchall_dicts(cur)[0]}


def lookup_idcliente(conn):
    schema = schema_name()
    ctt = qident(schema, "tmjsoncontract")
    cli = qident(schema, "tmjsonclient")
    ter = qident(schema, "materceros")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
              (SELECT COUNT(DISTINCT idcliente) FROM {ctt}) AS contract_clients,
              (SELECT COUNT(*) FROM (
                 SELECT DISTINCT c.idcliente
                 FROM {ctt} c
                 JOIN {cli} j ON j.idcliente = c.idcliente
               ) q) AS match_jsonclient,
              (SELECT COUNT(*) FROM (
                 SELECT DISTINCT c.idcliente
                 FROM {ctt} c
                 JOIN {ter} t ON t.idcliente = c.idcliente
               ) q) AS match_materceros,
              (SELECT COUNT(*) FROM (
                 SELECT DISTINCT c.idcliente
                 FROM {ctt} c
                 LEFT JOIN {ter} t ON t.idcliente = c.idcliente
                 WHERE t.idcliente IS NULL
               ) q) AS missing_in_materceros
            """
        )
        return {"audit": "lookup_idcliente", "schema": schema, **fetchall_dicts(cur)[0]}


def lookup_plan_id(conn):
    schema = schema_name()
    ctt = qident(schema, "tmjsoncontract")
    pln = qident(schema, "tmjsonplan_server")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            WITH plans AS (
              SELECT DISTINCT datajson->>'plan_id' AS plan_id
              FROM {ctt}
            )
            SELECT
              (SELECT COUNT(*) FROM plans) AS distinct_plan_id,
              (SELECT COUNT(*) FROM plans p
                 JOIN {pln} s
                   ON s.tipo = 'P'
                  AND s.datajson->>'id' = p.plan_id) AS matched_tipo_p,
              (SELECT COUNT(*) FROM {pln} WHERE tipo = 'P') AS plans_tipo_p
            """
        )
        return {"audit": "lookup_plan_id", "schema": schema, **fetchall_dicts(cur)[0]}


def lookup_perfil_cartera(conn):
    schema = schema_name()
    suc = qident(schema, "matercerosuc")
    per = qident(schema, "maperfilcartera")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT s.idperfilcartera, p.denominacion, COUNT(*) AS filas
            FROM {suc} s
            LEFT JOIN {per} p ON p.id = s.idperfilcartera
            GROUP BY s.idperfilcartera, p.denominacion
            ORDER BY filas DESC
            """
        )
        return {
            "audit": "lookup_perfil_cartera",
            "schema": schema,
            "distribution": fetchall_dicts(cur),
        }


def analisis_fecharetiroisp(conn):
    schema = schema_name()
    suc = qident(schema, "matercerosuc")
    per = qident(schema, "maperfilcartera")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
              COUNT(*) AS total,
              COUNT(*) FILTER (WHERE fecharetiroisp IS NULL) AS nulls,
              COUNT(*) FILTER (WHERE fecharetiroisp IS NOT NULL) AS not_null,
              MIN(fecharetiroisp) AS min_fecha,
              MAX(fecharetiroisp) AS max_fecha,
              COUNT(*) FILTER (WHERE fecharetiroisp IS NOT NULL AND activo = 'S') AS not_null_activo_s,
              COUNT(*) FILTER (WHERE fecharetiroisp IS NOT NULL AND activo = 'N') AS not_null_activo_n
            FROM {suc}
            """
        )
        summary = fetchall_dicts(cur)[0]
        cur.execute(
            f"""
            SELECT s.idperfilcartera, p.denominacion, COUNT(*) AS filas
            FROM {suc} s
            LEFT JOIN {per} p ON p.id = s.idperfilcartera
            WHERE s.fecharetiroisp IS NOT NULL
            GROUP BY s.idperfilcartera, p.denominacion
            ORDER BY filas DESC
            """
        )
        summary["by_perfil"] = fetchall_dicts(cur)
    return {"audit": "analisis_fecharetiroisp", "schema": schema, **summary}


def cruce_perfil_retiro(conn):
    schema = schema_name()
    suc = qident(schema, "matercerosuc")
    per = qident(schema, "maperfilcartera")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
              s.idperfilcartera,
              p.denominacion,
              COUNT(*) AS filas,
              COUNT(*) FILTER (WHERE s.fecharetiroisp IS NULL) AS fecha_null,
              COUNT(*) FILTER (WHERE s.fecharetiroisp IS NOT NULL) AS fecha_not_null
            FROM {suc} s
            LEFT JOIN {per} p ON p.id = s.idperfilcartera
            GROUP BY s.idperfilcartera, p.denominacion
            ORDER BY s.idperfilcartera NULLS FIRST
            """
        )
        return {
            "audit": "cruce_perfil_retiro",
            "schema": schema,
            "rows": fetchall_dicts(cur),
        }


def mismatch_idcliente(conn):
    schema = schema_name()
    suc = qident(schema, "matercerosuc")
    ter = qident(schema, "materceros")
    ctt = qident(schema, "tmjsoncontract")
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
              s.idcontrato,
              c.idcliente AS json_idcliente,
              s.nit,
              s.idsuc,
              t.idcliente AS terceros_idcliente,
              t.razonsocial
            FROM {suc} s
            JOIN {ctt} c ON c.idcontrato = s.idcontrato
            JOIN {ter} t ON t.nit = s.nit
            WHERE c.idcliente IS DISTINCT FROM t.idcliente
            ORDER BY s.nit, s.idsuc
            """
        )
        return {
            "audit": "mismatch_idcliente",
            "schema": schema,
            "rows": fetchall_dicts(cur),
        }


AUDITS = {
    "relate_matercerosuc_materceros": relate_matercerosuc_materceros,
    "lookup_idcontrato": lookup_idcontrato,
    "lookup_idcliente": lookup_idcliente,
    "lookup_plan_id": lookup_plan_id,
    "lookup_perfil_cartera": lookup_perfil_cartera,
    "analisis_fecharetiroisp": analisis_fecharetiroisp,
    "cruce_perfil_retiro": cruce_perfil_retiro,
    "mismatch_idcliente": mismatch_idcliente,
}


def run_audit(conn, name):
    if name == "all":
        return {key: fn(conn) for key, fn in AUDITS.items()}
    if name not in AUDITS:
        raise ValueError(f"Auditoría desconocida: {name}. Opciones: {', '.join(AUDITS)} , all")
    return AUDITS[name](conn)
