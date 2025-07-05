 
import modules

def main_menu():
    while True:
        print("\n--- Welcome to Bank Management ---")
        print("1. Account (Login)")
        print("2. Create Account")
        print("3. Settings")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            login_page()
        elif choice == '2':
            create_account_page()
        elif choice == '3':
            settings_page()
        elif choice == '4':
            print("Thank you for using the app!")
            break
        else:
            print("Invalid option. Try again.")

def login_page():
    print("\n--- Login Page ---")
    acc_id = input("Enter Account ID: ")
    password = input("Enter Password: ")
    acc_num = modules.authenticate(acc_id, password)
    if acc_num:
        print("Login successful!")
        account_actions(acc_num)
    else:
        print("Incorrect ID or password. Redirecting to Create Account...")
        create_account_page()

def create_account_page():
    print("\n--- Create Account ---")
    acc_num = input("Enter Account Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    mobile = input("Enter Mobile Number: ")
    password = input("Create Password: ")
    success, result = modules.create_account(acc_num, name, age, mobile, password)
    if success:
        print(f"Account created! Your Account ID is: {result}")
    else:
        print(result)

def account_actions(acc_num):
    while True:
        print("\n--- Account Actions ---")
        print("1. Add Money")
        print("2. Withdraw Money")
        print("3. Show Balance")
        print("4. Logout")
        choice = input("Select an option: ")
        if choice == '1':
            amt = float(input("Enter amount to add: "))
            bal = modules.add_money(acc_num, amt)
            print(f"Money added. New Balance: {bal}")
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            success, bal = modules.withdraw_money(acc_num, amt)
            if success:
                print(f"Withdrawn. New Balance: {bal}")
            else:
                print(f"Insufficient balance. Current Balance: {bal}")
        elif choice == '3':
            bal = modules.show_balance(acc_num)
            print(f"Current Balance: {bal}")
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option.")

def settings_page():
    print("\n--- Settings ---")
    print("1. Forgot ID (Find by Mobile)")
    print("2. Back to Main Menu")
    choice = input("Select an option: ")
    if choice == '1':
        mobile = input("Enter your mobile number: ")
        acc_id = modules.find_id(mobile)
        if acc_id:
            print(f"Your Account ID is: {acc_id}")
        else:
            print("No account found with this mobile number.")
    elif choice == '2':
        return
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main_menu()





