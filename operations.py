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
#Type Selection
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

    #Entering amount money
    try:
        cho_oper = int(input("Enter amount money: "))
        data["amount"] = cho_oper
    except ValueError:
        print("Error! Enter number!")

    #Choosing category
    print("Select category: ")
    for i in range(len(category)):
        print(f"{i} - {category[i]}")
    while True:
        try:
            cho_oper = int(input("Enter number: "))
            if cho_oper not in range(len(category)):
                raise ValueError
            data["category"] = category[cho_oper]
            break
        except ValueError:
            print(f"Error! Enter number below 0 - {len(category) - 1}!")

    #Writing comments
    cho_oper = input("Enter comments: ")
    data["comments"] = cho_oper

    data["date"] = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    print(f'Date - {data["date"]}')

    print(data)


def show_balance():
    all_data = load()
    income = 0
    expense = 0
    for misc in all_data:
        if misc["type"] == "income":
            income += misc["amount"]
        else:
            expense += misc["amount"]
    print(f"\nIncome: {income}"
          f"\nExpense: {expense}"
          f"\nBalance: {income - expense}\n")


def show_history():
    all_data = load()
    story = []
    story = all_data[-5:]
    for i in story: print(i, "\n")


def show_stat():
    pass
def save_oper():
    all_data = load()
    data["id"] = len(all_data)
    all_data.append(data)
    save(all_data)