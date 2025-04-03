
menu = """
           ========== MENU ==========

     Welcome to the financial management system! 
           What would you like to do?**

           [1] Withdraw
           [2] Deposit
           [3] Transaction history
           [4] Exit

           ========================="""
balance = 1000
LIMIT = 500.00
transaction_history = []
withdraw = 1
WITHDRAW_LIMIT = 3

print(menu)

while True:
    option = int(input("Please select the desired option: "))
    if option == 1:
        withdraw_value = float(
            input("Enter the amount you wish to withdraw: "))
        if withdraw_value > balance or withdraw_value > LIMIT:
            print("Insufficient funds :(")

        elif withdraw_value <= balance and withdraw <= WITHDRAW_LIMIT:
            print("Transaction completed.")
            withdraw = withdraw + 1
            balance = balance - withdraw_value
            transaction_history.append(
                f"Withdraw £{withdraw_value:.2f}. Balance £{balance:.2f}")
            print(f"Your current balance: £{balance:.2f}")

        elif withdraw >= WITHDRAW_LIMIT:
            print("Daily withdrawal limit reached, please try again tomorrow.")

    elif option == 2:
        deposit = float(input("Enter the amount you wish to deposit: "))
        balance = deposit + balance
        transaction_history.append(
            f"Deposit £{deposit:.2f}. Balance £{balance:.2f}")
        print(f"Your current balance: £{balance:.2f} ")

    elif option == 3:
        print("\n".join(transaction_history))
        print(f"Your current balance: £{balance:.2f}")

    elif option == 4:
        break

    else:
        print("Invalid option")
        continue
