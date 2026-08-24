import os
from itertools import combinations

DATE_TYPES = {
    "date",
    "timestamp without time zone",
    "timestamp with time zone",
}


def qi(value):
    return '"' + value.replace('"', '""') + '"'


def analyze_table(conn, table_name, sample_limit=10, low_cardinality_limit=20):
    schema = os.environ.get("DB_SCHEMA", "bronze_guajiranet")
    full = f"{qi(schema)}.{qi(table_name)}"

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT column_name, data_type, is_nullable, ordinal_position
            FROM information_schema.columns
            WHERE table_schema=%s AND table_name=%s
            ORDER BY ordinal_position
            """,
            (schema, table_name),
        )
        columns = [
            {"column": r[0], "data_type": r[1], "nullable": r[2], "position": r[3]}
            for r in cur.fetchall()
        ]

    if not columns:
        raise ValueError(f"Tabla no encontrada en {schema}: {table_name}")

    with conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {full}")
        row_count = cur.fetchone()[0]

    result = {
        "schema": schema,
        "table": table_name,
        "row_count": row_count,
        "columns": [],
        "candidate_unique_columns": [],
        "candidate_composite_keys": [],
    }

    with conn.cursor() as cur:
        for col in columns:
            name = col["column"]
            qc = qi(name)
            item = dict(col)

            cur.execute(f"SELECT COUNT(*) FROM {full} WHERE {qc} IS NULL")
            item["null_count"] = cur.fetchone()[0]

            cur.execute(f"SELECT COUNT(DISTINCT {qc}) FROM {full}")
            item["distinct_count"] = cur.fetchone()[0]

            cur.execute(
                f"SELECT {qc} FROM {full} WHERE {qc} IS NOT NULL LIMIT %s",
                (sample_limit,),
            )
            item["sample"] = [r[0] for r in cur.fetchall()]

            if col["data_type"] in DATE_TYPES:
                cur.execute(f"SELECT MIN({qc}), MAX({qc}) FROM {full}")
                item["min"], item["max"] = cur.fetchone()

            if row_count > 0 and item["distinct_count"] <= low_cardinality_limit:
                cur.execute(
                    f"""
                    SELECT {qc}, COUNT(*)
                    FROM {full}
                    WHERE {qc} IS NOT NULL
                    GROUP BY {qc}
                    ORDER BY COUNT(*) DESC
                    LIMIT %s
                    """,
                    (low_cardinality_limit,),
                )
                item["distribution"] = [
                    {"value": r[0], "count": r[1]} for r in cur.fetchall()
                ]

            if row_count > 0 and item["distinct_count"] == row_count:
                result["candidate_unique_columns"].append(name)

            result["columns"].append(item)

        id_cols = [
            c["column"]
            for c in columns
            if (
                c["column"].lower() in {"nit", "id", "idsuc"}
                or c["column"].lower().startswith("id")
                or c["column"].lower().endswith("id")
            )
        ][:8]

        for combo in combinations(id_cols, 2):
            a, b = map(qi, combo)
            cur.execute(
                f"SELECT COUNT(*) FROM (SELECT DISTINCT {a}, {b} FROM {full}) q"
            )
            if row_count > 0 and cur.fetchone()[0] == row_count:
                result["candidate_composite_keys"].append(list(combo))

    return result
