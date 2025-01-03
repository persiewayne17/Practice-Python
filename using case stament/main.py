balance = 1000.0
pin = 1234
pin_count = 0

def debit():
    global balance, pin_count
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is: {balance}")
            pin_count = 0
        else:
            print("Insufficient funds.")
    else:
        print("Incorrect PIN.")
        pin_count += 1

def credit():
    global balance, pin_count
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Deposit successful. Your new balance is: {balance}")
        pin_count = 0
    else:
        print("Incorrect PIN.")
        pin_count += 1

def main():
    global pin_count

    while True:
        if pin_count >= 3:
            print("Too many incorrect PIN attempts. Account locked.")
            break

        print("\n1. Debit\n2. Credit\n3. Check Balance\n4. Exit")
        try:  # Handle potential ValueError if input is not an integer
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Go to the next iteration of the loop

        match choice:  # Use match-case (Python 3.10+)
            case 1:
                debit()
            case 2:
                credit()
            case 3:
                print(f"Your current balance is: {balance}")
            case 4:
                print("Thank you for using our banking system.")
                break
            case _:  # Default case for invalid choices
                print("Invalid choice.")

main()