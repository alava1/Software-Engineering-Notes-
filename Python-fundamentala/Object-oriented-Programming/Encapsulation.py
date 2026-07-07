# encapsulation.py
# Topic: Encapsulation - Protecting data using private attributes

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance        # Private attribute (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₦{amount}. New balance: ₦{self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₦{amount}. Remaining: ₦{self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    # Getter method
    def get_balance(self):
        return self.__balance


print("=== Encapsulation Example ===\n")

account = BankAccount("Oluwaseun", 5000)
account.deposit(2000)
account.withdraw(1500)
print("Current balance:", account.get_balance())

# Direct access to private attribute won't work easily
# print(account.__balance)   # This will cause AttributeError
