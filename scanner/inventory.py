import os

def get_tables(conn):
    schema = os.environ.get("DB_SCHEMA", "bronze_guajiranet")
    sql = """
    SELECT table_schema, table_name, table_type
    FROM information_schema.tables
    WHERE table_schema=%s AND table_type='BASE TABLE'
    ORDER BY table_name
    """
    with conn.cursor() as cur:
        cur.execute(sql, (schema,))
        return [{"schema":r[0],"table":r[1],"type":r[2]} for r in cur.fetchall()]

def get_columns(conn):
    schema = os.environ.get("DB_SCHEMA", "bronze_guajiranet")
    sql = """
    SELECT table_name,column_name,data_type,is_nullable,ordinal_position
    FROM information_schema.columns
    WHERE table_schema=%s
    ORDER BY table_name,ordinal_position
    """
    with conn.cursor() as cur:
        cur.execute(sql, (schema,))
        return [{"table":r[0],"column":r[1],"data_type":r[2],"nullable":r[3],"position":r[4]} for r in cur.fetchall()]
