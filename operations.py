from obj_constructor import constructor
import storage
import stats

def add_oper(): #Function receive data from user and create income or expense object
    global data
    data = constructor()

def show_balance(): #Sum up income, expense and calculating balance
    all_data = storage.load()
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


def show_history(): #Showes tha latest 5 added object
    all_data = storage.load()
    story = all_data[-5:]
    for i in story: print(i, "\n")


def show_stat(): #Showes stats
    while True:
        tm = int(input("Statistics:\n"
              "1 - Income\n"
              "2 - Expense\nEnter: "))
        if tm == 1:
            stats.income_stats()
            break
        elif tm == 2:
            stats.expense_stat()
            break
        else:
            print("Wrong input. Enter 1 or 2!")

def save_oper(): #Function for saving list in JSON file
    all_data = storage.load() #Load JSON file
    data["id"] = len(all_data) #Added an ID to the entry
    all_data.append(data) #Added object to list with all data
    storage.save(all_data) #Saving in JSON file