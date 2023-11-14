checking = 0.00
savings = 0.00
amount = 0.00

print("Welcome to the ATM Simulator!")
print()

while True:
    print("Checking".ljust(12) + f"${checking:.2f}".rjust(15))
    print("Savings".ljust(12) + f"${savings:.2f}".rjust(15))
    print()
    menu_selection = input("(D)eposit, (W)ithdraw, or (Q)uit? ").lower()
    if menu_selection == "d":
        menu_selection = input("(C)hecking or (S)avings? ").lower()
        if menu_selection == "c":
            print()
            amount = float(input("Amount to add to Checking: $"))
            checking += amount
        elif menu_selection == "s":
            print()
            amount = float(input("Amount to add to Savings: $"))
            savings += amount
        else:
            print("Incorrect input detected.")
    elif menu_selection == "w":
        menu_selection = input("(C)hecking or (S)avings? ").lower()
        if menu_selection == "c":
            while True:
                print()
                amount = float(input("Amount to take from Checking: $"))
                if checking - amount >= 0:
                    checking -= amount
                    break
                else:
                    print("Not enough money in account!")
        elif menu_selection == "s":
            while True:
                print()
                amount = float(input("Amount to take from Savings: $"))
                if savings - amount >= 0:
                    savings -= amount
                    break
                else:
                    print("Not enough money in account!")
        else:
            print("Incorrect input detected.")
    elif menu_selection == "q":
        break
    else:
        print("Incorrect input detected.")

print("Thanks for your business!")
