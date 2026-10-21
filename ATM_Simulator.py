

def login():
    correct_pin = "1234"
    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("\nLogin successful!")
            return True
        else:
            attempts -= 1
            print("Incorrect PIN.")
            print("Attempts remaining:", attempts)

    print("Too many incorrect attempts. Exiting...")
    return False


def check_balance(balance):
    print(f"\nYour current balance is: ₹{balance:.2f}")
    return balance


def deposit(balance):
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Updated balance: ₹{balance:.2f}")
    else:
        print("Please enter a valid amount.")

    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Please collect your cash: ₹{amount:.2f}")
        print(f"Remaining balance: ₹{balance:.2f}")

    return balance


def atm_menu():
    balance = 5000.00

    if not login():
        return

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


atm_menu()
