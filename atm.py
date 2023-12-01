def transfer_money(account, transaction, balance):
    while True:
        print()
        try:
            amount = float(input(f"Amount to {transaction} {account}: $"))
        except ValueError:
            print("Value must be a number!")
            continue
        else:
            if balance > 0 > balance - amount:
                print("Not enough money in account!")
                continue
            elif amount < 0:
                print("Amount must be a positive number.")
                continue
            else:
                balance -= amount
                break
    return balance


checking = 0.00
savings = 0.00

print("Welcome to the ATM Simulator!")

while True:
    print()
    print("Checking".ljust(12) + f"${checking:.2f}".rjust(15))
    print("Savings".ljust(12) + f"${savings:.2f}".rjust(15))
    print()
    menu_selection = input("(D)eposit, (W)ithdraw, or (Q)uit? ").lower()
    if menu_selection == "d":
        menu_selection = input("(C)hecking or (S)avings? ").lower()
        if menu_selection == "c":
            checking = -1 * transfer_money("Checking", "deposit to", -1 * checking)
        elif menu_selection == "s":
            savings = -1 * transfer_money("Savings", "deposit to", -1 * savings)
        else:
            print("Incorrect input detected.")
    elif menu_selection == "w":
        menu_selection = input("(C)hecking or (S)avings? ").lower()
        if menu_selection == "c":
            if checking == 0:
                print("No money in Checking.")
                continue
            checking = transfer_money("Checking", "withdraw from", checking)
        elif menu_selection == "s":
            if savings == 0:
                print("No money in Savings.")
                continue
            savings = transfer_money("Savings", "withdraw from", savings)
        else:
            print("Incorrect input detected.")
    elif menu_selection == "q":
        break
    else:
        print("Incorrect input detected.")

print("Thanks for your business!")
