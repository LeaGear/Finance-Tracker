from obj_constructor import constructor
from uuid import uuid4

import optimization
import stats


def add_oper(data_list): #Function receive data from user and create income or expense object
    data = constructor()
    data["id"] = str(uuid4())#Added an ID to the entry
    data_list.append(data)
    return data_list

def show_balance(data_list): #Sum up income, expense and calculating balance
    bal = {"income": 0, "expense": 0, "balance": 0}
    for misc in data_list:
        if misc["type"] == "income":
            bal["income"] += misc["amount"]
        else:
            bal["expense"] += misc["amount"]
    bal["balance"] = bal["income"] - bal["expense"]
    return bal


def show_history(data_list): #Showes tha latest 5 added object
    story = data_list[-5:]
    return story


def show_stat(data_list): #Showes stats
    while True:
        tm = optimization.get_verified_int("Statistics:\n"
                                           "1 - Income\n"
                                           "2 - Expense\nEnter: ",
                                           "Error! Enter number!")
        if tm == 1:
            temp_stat = stats.type_stats(data_list, "income")
            break
        elif tm == 2:
            temp_stat = stats.type_stats(data_list, "expense")
            break
        else:
            print("Wrong input. Enter 1 or 2!")
    return temp_stat