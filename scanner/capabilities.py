KEYWORDS={
"cliente_360":["cliente","tercero","suscriptor","nit","razon","nombre"],
"vinculacion":["ingreso","alta","vincula","registro","instala","activacion"],
"servicio_plan":["servicio","plan","producto","paquete","tarifa"],
"facturacion":["factura","prefijo","subtotal","iva","neto"],
"pagos":["pago","recaudo","abono","recibo"],
"cartera_mora":["cartera","saldo","mora","vencimiento","deuda"],
"estado_cliente":["estado","activo","suspend","bloque","corte"],
"retiro_desercion":["retiro","cancel","baja","desert","motivo"],
"geografia":["departamento","municipio","ciudad","barrio","direccion"],
"marketing":["campana","promocion","descuento","asesor","vendedor"]
}
def build_capability_map(tables,columns):
    result=[]
    for capability,words in KEYWORDS.items():
        matches=[]
        for t in tables:
            score=sum(w in t["table"].lower() for w in words)
            if score: matches.append({"type":"table","table":t["table"],"name":t["table"],"score":score})
        for c in columns:
            score=sum(w in c["column"].lower() for w in words)
            if score: matches.append({"type":"column","table":c["table"],"name":c["column"],"score":score})
        matches.sort(key=lambda x:(-x["score"],x["table"],x["name"]))
        result.append({"capability":capability,"status":"candidate_data_found" if matches else "no_obvious_data_found","matches":matches[:100]})
    return result
