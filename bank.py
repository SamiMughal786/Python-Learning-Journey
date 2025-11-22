class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Hello, how would you like to proceed?
1. Enter 1 to create the pin.
2. Enter 2 to Deposit.
3. Enter 3 for Withdrawal.
4. Enter 4 to check the balance.
5. Enter 5 to exit.

Your choice: """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Exit")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin Set Successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            self.balance += amount
            print("Deposit Successfully!")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Your Balance is:", self.balance)
        else:
            print("Invalid Pin")
class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        while True:   # LOOP UNTIL USER CHOOSES EXIT
            user_input = input("""
Hello, how would you like to proceed?
1. Enter 1 to create the pin.
2. Enter 2 to Deposit.
3. Enter 3 for Withdrawal.
4. Enter 4 to check the balance.
5. Enter 5 to exit.

Your choice: """)

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exiting... Thank you!")
                break   # STOP THE LOOP
            else:
                print("Invalid input. Try again.")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin Set Successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            self.balance += amount
            print("Deposit Successfully!")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Your Balance is:", self.balance)
        else:
            print("Invalid Pin")


# Create separate ATM objects for different users
user1 = Atm()
user2 = Atm()

# Call the menu for each user separately
print("=== User 1 ===")
user1.menu()
 
print("=== User 2 ===")
user2.menu()

# Run the ATM program
Atm()
