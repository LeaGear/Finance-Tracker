import operations
from storage import load


def main():
    data_list = load()
    while True:
        print("Main Menu:\n"
              "1 - Add operation\n"
              "2 - Show balance\n"
              "3 - Show history\n"
              "4 - Show statistics\n"
              "5 - Save operation\n"
              "6 - Exit")
        choice = int(input("What do you want: "))

        if choice == 1:
            operations.add_oper()
        elif choice == 2:
            temp_balance = operations.show_balance(data_list)
            print(f"\nIncome: {temp_balance["income"]}"
                  f"\nExpense: {temp_balance['expense']}"
                  f"\nBalance: {temp_balance["balance"]}\n")
        elif choice == 3:
            operations.show_history(data_list)
        elif choice == 4:
            operations.show_stat(data_list)
        elif choice == 5:
            operations.save_oper(data_list)
        elif choice == 6:
            print("Exiting...")
            break

main()