from collections import defaultdict

DATE_TYPES={"date","timestamp without time zone","timestamp with time zone"}

def qi(x): return '"' + x.replace('"','""') + '"'

def profile_schema(conn,tables,columns):
    grouped=defaultdict(list)
    for c in columns: grouped[c["table"]].append(c)
    results=[]
    for i,t in enumerate(tables,1):
        schema,table=t["schema"],t["table"]
        full=f"{qi(schema)}.{qi(table)}"
        print(f"[{i}/{len(tables)}] {schema}.{table}")
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {full}")
            rows=cur.fetchone()[0]
        entry={"table":table,"row_count":rows,"columns":[]}
        for col in grouped[table]:
            c,dtype=col["column"],col["data_type"]
            qc=qi(c)
            with conn.cursor() as cur:
                cur.execute(f"SELECT COUNT(*) FILTER (WHERE {qc} IS NULL), COUNT(DISTINCT {qc}) FROM {full}")
                nulls,distinct=cur.fetchone()
            item={"column":c,"data_type":dtype,"null_count":nulls,"distinct_count":distinct}
            if dtype in DATE_TYPES:
                with conn.cursor() as cur:
                    cur.execute(f"SELECT MIN({qc}),MAX({qc}) FROM {full}")
                    item["min"],item["max"]=cur.fetchone()
            with conn.cursor() as cur:
                cur.execute(f"SELECT DISTINCT {qc} FROM {full} WHERE {qc} IS NOT NULL LIMIT 5")
                item["sample"]=[r[0] for r in cur.fetchall()]
            entry["columns"].append(item)
        results.append(entry)
    return results
