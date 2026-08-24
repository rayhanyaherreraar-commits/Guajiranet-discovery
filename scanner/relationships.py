from collections import defaultdict
def norm(x): return x.lower().replace("_","").replace("-","")
def detect_candidate_relationships(columns):
    groups=defaultdict(list)
    for c in columns:
        n=norm(c["column"])
        if n=="nit" or n=="id" or n.startswith("id") or n.endswith("id"):
            groups[n].append({"table":c["table"],"column":c["column"],"data_type":c["data_type"]})
    return [{"normalized_key":k,"references":v} for k,v in groups.items() if len(v)>1]
