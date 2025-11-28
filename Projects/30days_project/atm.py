class ATM: #defining the class called ATM--blueprint of objects
    def __init__(self, balance=1000):
        self.balance = balance
    #creating function as pin
    def pin(self,pin_num):
        self.pin=pin_num
        return f"Enter your pin: {self.pin}" 
    def check_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."


# Create an instance of the ATM
atm = ATM()
while True:
    print("0. enter Pinnumber")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    

    choice = input("Enter your choice: ")

    if choice =='0':
        pin_num = int(input("Enter the pin number: "))
        print(atm.pin(pin_num))

    elif choice == '1':
        print(atm.check_balance())
    elif choice == '2':
        amount = float(input("Enter the deposit amount: "))
        print(atm.deposit(amount))
    elif choice == '3':
        amount = float(input("Enter the withdrawal amount: "))
        print(atm.withdraw(amount))
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")