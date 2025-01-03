balance = 1000.0
pin = 1234
pin_count = 0

def debit():
    global pin_count  # Only needed if debit also checks pin_count
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        amount = float(input("Enter the amount to withdraw: "))
        global balance  # Only needed if modifying balance
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is: {balance}")
            pin_count = 0 # Reset pin_count on successful transaction
        else:
            print("Insufficient funds.")
    else:
        print("Incorrect PIN.")
        pin_count += 1

def credit():
    global pin_count # Needed to modify global pin_count
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        amount = float(input("Enter the amount to deposit: "))
        global balance
        balance += amount
        print(f"Deposit successful. Your new balance is: {balance}")
        pin_count = 0 # Reset pin_count on successful transaction
    else:
        print("Incorrect PIN.")
        pin_count += 1


def main():
    global pin_count # Needed to access global pin_count

    while True:
        if pin_count >= 3:
            print("Too many incorrect PIN attempts. Account locked.")
            break

        print("\n1. Debit\n2. Credit\n3. Check Balance\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            debit()
        elif choice == 2:
            credit()
        elif choice == 3:
            print(f"Your current balance is: {balance}")
        elif choice == 4:
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice.")


main()