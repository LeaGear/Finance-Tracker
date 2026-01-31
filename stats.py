from storage import load, category


def create_bible():
    bibl = {}
    for i in category: bibl[i] = 0
    #print(bibl)
    return bibl

def degree_lists(data_list, trigger):
    income = []
    expense = []
    for i in data_list:
        if i["type"] == "income":
            income.append(i)
        else:
            expense.append(i)
    #print(income, "\n", expense)
    if trigger == "income":
        return income
    else:
        return expense

def output(bibl):
    for i in bibl:
        print(f"{i} = {bibl[i]} UAH")

def income_stats(data_list):
    bibl = create_bible()
    all_income = degree_lists(data_list, "income")
    for i in all_income:
        bibl[i["category"]] += i["amount"]
    output(bibl)

def expense_stat(data_list):
    bibl = create_bible()
    all_expense = degree_lists(data_list, "expense")
    for i in all_expense:
        bibl[i["category"]] += i["amount"]
    output(bibl)