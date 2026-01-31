import operations
from storage import load, save



def main():
    data_list = load()
    while True:
        print("Main Menu:\n"
              "1 - Add operation\n"
              "2 - Show balance\n"
              "3 - Show history\n"
              "4 - Show statistics\n"
              "5 - Exit")

        while True:
            try:
                choice = int(input("What do you want: "))
                break
            except ValueError:
                print("Enter number below 1 and 5")

        if choice == 1:
            data_list = operations.add_oper(data_list)
        elif choice == 2:
            temp_balance = operations.show_balance(data_list)
            print(f"\nIncome: {temp_balance['income']}"
                  f"\nExpense: {temp_balance['expense']}"
                  f"\nBalance: {temp_balance['balance']}\n")
        elif choice == 3:
            print("Your last 5 entries:\n")
            temp_history = operations.show_history(data_list)
            for i in temp_history: print(i)
        elif choice == 4:
            stat_dict = operations.show_stat(data_list)
            for i in stat_dict:
                print(f"{i} = {stat_dict[i]} UAH")
        elif choice == 5:
            print("Exiting...")
            save(data_list)
            break
        else:
            print("Enter number below 1 and 5")

main()