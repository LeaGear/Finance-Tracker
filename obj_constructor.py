from datetime import datetime
from storage import category



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
    try:
        cho_oper = int(input("Enter amount money: "))
        data["amount"] = cho_oper
    except ValueError:
        print("Error! Enter number!")

    # Choosing category
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

    # Writing comments
    cho_oper = input("Enter comments: ")
    data["comments"] = cho_oper

    data["date"] = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    print(f'Date - {data["date"]}')

    print(data)
    return data