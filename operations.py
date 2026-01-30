from datetime import datetime
from storage import *


data = {
    "id": 0,
    "type": "",
    "amount": 0,
    "category": "",
    "comments": "",
    "date": ""
}

def add_oper():
    while True:
        cho_oper = input("Income or Expense? ")
        try:
            if cho_oper.lower() == "income" or cho_oper.lower() == "expense":
                data["type"] = cho_oper
                break
            else:
                raise ValueError
        except ValueError:
            print("Error! Enter: Income or Expense!")
    cho_oper = int(input("Enter amount money: "))
    data["amount"] = cho_oper
    cho_oper = input("Enter category: ")
    data["category"] = cho_oper
    cho_oper = input("Enter comments: ")
    data["comments"] = cho_oper
    data["date"] = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    print(f'Date - {data["date"]}')
    print(data)
def show_balance():
    pass
def show_history():
    pass
def show_stat():
    pass
def save_oper():
    all_data = load()
    data["id"] = len(all_data)
    all_data.append(data)
    save(all_data)