import argparse, json
from pathlib import Path
from scanner.db import get_connection
from scanner.inventory import get_tables, get_columns
from scanner.profiler import profile_schema
from scanner.relationships import detect_candidate_relationships
from scanner.capabilities import build_capability_map
from scanner.report import build_report

OUT = Path("output"); OUT.mkdir(exist_ok=True)

def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["inventory", "profile"], default="inventory")
args = parser.parse_args()

with get_connection() as conn:
    tables = get_tables(conn)
    columns = get_columns(conn)
    save("catalogo_tablas.json", tables)
    save("catalogo_columnas.json", columns)
    print(f"Tablas: {len(tables)} | Columnas: {len(columns)}")

    if args.mode == "profile":
        profiles = profile_schema(conn, tables, columns)
        save("perfil_columnas.json", profiles)

        relationships = detect_candidate_relationships(columns)
        save("relaciones_candidatas.json", relationships)

        capabilities = build_capability_map(tables, columns)
        save("mapa_capacidades.json", capabilities)

        report = build_report(tables, columns, profiles, relationships, capabilities)
        (OUT / "resumen_discovery.md").write_text(report, encoding="utf-8")
        print("Discovery completo.")
