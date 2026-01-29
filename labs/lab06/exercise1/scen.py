def merge_sales_data(region1_sales, region2_sales):
    merged = {}
    for i in region1_sales :
        merged[i["transaction_id"]] = i
    for i in region2_sales :
        ID = i["transaction"]
        if ID not in merged :
            merged[ID] = i
        else:
            if i["amount"] > merged[ID]["amount"]:
                merged[ID] = result
    return list(merged.values())