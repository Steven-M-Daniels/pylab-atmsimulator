def deposit_money(account, balance):
    while True:
        print()
        try:
            amount = float(input(f"Amount to add to {account}: $"))
        except ValueError:
            print("Value must be a number!")
            continue
        else:
            if amount < 0:
                print("Amount must be a positive number.")
                continue
            else:
                balance += amount
                break
            break
    return balance


def withdraw_money(account, balance):
    while True:
        print()
        try:
            amount = float(input(f"Amount to take from {account}: $"))
        except ValueError:
            print("Value must be a number!")
            continue
        else:
            if balance - amount < 0:
                print("Not enough money in account!")
                continue
            elif amount < 0:
                print("Amount must be a positive number.")
                continue
            else:
                balance -= amount
                break
            break
    return balance


checking = 0.00
savings = 0.00

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
            checking = deposit_money("Checking", checking)
        elif menu_selection == "s":
            savings = deposit_money("Savings", savings)
        else:
            print("Incorrect input detected.")
    elif menu_selection == "w":
        menu_selection = input("(C)hecking or (S)avings? ").lower()
        if menu_selection == "c":
            checking = withdraw_money("Checking", checking)
        elif menu_selection == "s":
            savings = withdraw_money("Savings", savings)
        else:
            print("Incorrect input detected.")
    elif menu_selection == "q":
        break
    else:
        print("Incorrect input detected.")

print("Thanks for your business!")
