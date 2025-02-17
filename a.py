class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: ${self.balance:.2f}")

def main():
    print("Welcome to Simple Bank!")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Thank you for using Simple Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
