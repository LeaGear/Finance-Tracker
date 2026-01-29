from storage import data_all_time


global all_income
global all_expense
all_income = data_all_time["income"]
all_expense = data_all_time["expense"]

def calc(data):
    now = data["type"]
    if now == "income":
        all_income += data["amount"]
    elif now == "expense":
        all_expense += data["amount"]