from storage import category



def type_stats(data_list, op_type):
    stats = {category_dict: 0 for category_dict in category}
    for item in data_list:
        if item["type"] == op_type:
            stats[item["category"]] += item["amount"]
    return stats