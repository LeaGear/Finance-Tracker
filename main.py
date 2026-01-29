from operations import *

choose = 10

while choose != 6:
    print("Main Menu:\n"
          "1 - Add operation\n"
          "2 - Show balance\n"
          "3 - Show history\n"
          "4 - Show statistics\n"
          "5 - Save operation\n"
          "6 - Exit")
    choose = int(input("What do you want: "))
    if choose == 1:
        add_oper()
    elif choose == 2:
        pass
    elif choose == 3:
        pass
    elif choose == 4:
        pass
    elif choose == 5:
        save_oper()
    elif choose == 6:
        print("Exiting...")
        break