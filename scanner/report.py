def build_report(tables,columns,profiles,relationships,capabilities):
    lines=["# Resumen automático — GuajiraNet Data Discovery","",
           "## Inventario",f"- Tablas detectadas: **{len(tables)}**",f"- Columnas detectadas: **{len(columns)}**",f"- Relaciones candidatas: **{len(relationships)}**","",
           "## Capacidades analíticas candidatas",""]
    for cap in capabilities:
        icon="🟢" if cap["status"]=="candidate_data_found" else "🔴"
        lines.append(f"### {icon} {cap['capability']}")
        if cap["matches"]:
            for m in cap["matches"][:15]: lines.append(f"- `{m['table']}.{m['name']}`")
        else: lines.append("- No se encontraron coincidencias evidentes por nombre.")
        lines.append("")
    lines += ["## Nota","Las coincidencias son candidatas. La calidad y significado del dato deben validarse antes de modelarlo."]
    return "\n".join(lines)
