def apply_filters(df, rules):
    out = {}
    for name, rule in rules.items():
        temp = df
        for col, condition in rule.items():
            if "equals" in condition:
                temp = temp[temp[col] == condition["equals"]]
            if "min" in condition:
                temp = temp[temp[col] >= condition["min"]]
            if "max" in condition:
                temp = temp[temp[col] <= condition["max"]]
        out[name] = temp
    return out
