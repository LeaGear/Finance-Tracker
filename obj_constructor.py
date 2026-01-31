from datetime import datetime
from storage import category
import optimization


def constructor():
    data = {
        "id": 0,
        "type": "",
        "amount": 0,
        "category": "",
        "comments": "",
        "date": ""
    }
    # Type Selection
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

    # Entering amount money
    cho_oper = optimization.get_verified_int("Enter amount money: ",
                                             "Error! Enter number!")
    data["amount"] = cho_oper

    # Choosing category
    print("Select category: ")
    while True:
        for i in range(len(category)):
            print(f"{i} - {category[i]}")
        cho_oper = optimization.get_verified_int("Enter number: ",
                                                 f"Error! Enter number below 0 - {len(category) - 1}!")
        if 0 <= cho_oper < len(category):
            data["category"] = category[cho_oper]
            break
        else:
            print(f"Error! Enter number below 0 - {len(category) - 1}!")

    # Writing comments
    cho_oper = input("Enter comments: ")
    data["comments"] = cho_oper

    #Adding date
    data["date"] = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    print(f'Date - {data["date"]}')

    print(data)
    return data