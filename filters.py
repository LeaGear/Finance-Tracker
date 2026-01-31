

def month_filter(data_list, month, year=None):
    monthly_list = []
    for item in data_list:
        if int(item["date"][3:5]) == month:
            monthly_list.append(item)
    return monthly_list