from datetime import datetime
import json

all_data = []

data = {
    "type": "",
    "amount": 0,
    "category": "",
    "comments": "",
    "date": ""
}

try:
    with open("data.json", "r", encoding="utf-8") as file1:
        all_data = json.load(file1)
except FileNotFoundError:
    pass



def add_oper():
    while True:
        cho_oper = input("Income or Expense? ")
        try:
            #print(cho_oper)
            if cho_oper.lower() == "income" or cho_oper.lower() == "expense":
                data["type"] = cho_oper
                break
            else:
                raise ValueError
        except ValueError:
            print("Error! Enter: Income or Expense!")
        '''if cho_oper.lower() == "income":
            data["type"] = cho_oper
            break
        elif cho_oper.lower() == "expense":
            data["type"] = cho_oper
            break'''
    #print(data["type"])
    cho_oper = int(input("Enter amount money: "))
    data["amount"] = cho_oper
    cho_oper = input("Enter category: ")
    data["category"] = cho_oper
    cho_oper = input("Enter comments: ")
    data["comments"] = cho_oper
    data["date"] = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    print(f'Date - {data["date"]}')
    all_data.append(data)
    print(data)
def show_balance():
    pass
def show_history():
    pass
def show_stat():
    pass
def save_oper():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(all_data, file, ensure_ascii=False, indent=2)
    print("Operation saved successfully!")
    print(all_data)
