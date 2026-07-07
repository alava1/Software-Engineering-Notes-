# custom_exception.py
# Topic: Creating Custom Exceptions

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

class InsufficientFundsError(Exception):
    """Custom exception for bank transactions"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds! Balance: ₦{balance}, Tried to withdraw: ₦{amount}")

print("=== Custom Exceptions ===\n")

def check_age(age):
    if age < 0:
        raise NegativeNumberError("Age cannot be negative!")
    elif age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


# Testing
try:
    check_age(-5)
except NegativeNumberError as e:
    print(f"Caught: {e}")

print("\n--- Bank Example ---")
try:
    new_balance = withdraw_money(5000, 7000)
    print("Withdrawal successful. New balance:", new_balance)
except InsufficientFundsError as e:
    print("Transaction failed:", e)
