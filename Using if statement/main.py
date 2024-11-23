# Simple Bank Transaction System

balance = 1000.0
pin = 1234
pin_count = 0

def debit():
    print("Enter your PIN:")
    user_pin = int(input())
    if user_pin == pin:
        amount = float(input("Enter the amount to withdraw: "))
        global balance
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is: {balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Incorrect PIN.")

def credit():
    print("Enter your PIN:")
    user_pin = int(input())
    while True:
        global pin_count
        pin_count += 1
        if pin_count <= 3:
            if user_pin == pin:
                amount = float(input("Enter the amount to deposit: "))
                global balance
                balance += amount
                print(f"Deposit successful. Your new balance is: {balance}")
            elif pin_count == 3 and user_pin != pin:
                print("Incorrect PIN.")
                break
            else:
                break
        else:
            break

#Main function to control the program flow
def main():
    while True:
        print("")
        print("1. Debit\n2. Credit\n3. Check Balance\n4. Exit")
        choice = int(input("Enter your choice: "))
        global balance
        if choice == 1:
            debit()
        elif choice == 2:
            credit()
        elif choice == 3:
            print(f"Your current balance is: {balance}");
        elif choice == 4:
            print("Thank you for using our banking system.")       
            break;
        else:
            print("Incorrect PIN.")

main()