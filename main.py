from operations import *

choice = 10

while choice != 6:
    print("Main Menu:\n"
          "1 - Add operation\n"
          "2 - Show balance\n"
          "3 - Show history\n"
          "4 - Show statistics\n"
          "5 - Save operation\n"
          "6 - Exit")
    choice = int(input("What do you want: "))
    if choice == 1:
        add_oper()
    elif choice == 2:
        show_balance()
    elif choice == 3:
        show_history()
    elif choice == 4:
        show_stat()
    elif choice == 5:
        save_oper()
    elif choice == 6:
        print("Exiting...")
        break