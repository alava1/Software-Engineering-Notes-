# expense_tracker.py

import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        try:
            with open("expenses.json", "r") as f:
                return json.load(f)
        except:
            return []
    
    def save_expenses(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f, indent=2)
    
    def add_expense(self, amount, category, description=""):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": float(amount),
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("✅ Expense recorded!")
    
    def show_summary(self):
        if not self.expenses:
            print("No expenses yet.")
            return
        
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"\nTotal Expenses: ₦{total:.2f}")
        
        # Group by category
        from collections import defaultdict
        categories = defaultdict(float)
        for exp in self.expenses:
            categories[exp["category"]] += exp["amount"]
        
        print("\nBy Category:")
        for cat, amt in categories.items():
            print(f"  {cat}: ₦{amt:.2f}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("=== Expense Tracker ===\n")
    
    tracker.add_expense(2500, "Food", "Lunch at restaurant")
    tracker.add_expense(15000, "Transport", "Fuel")
    tracker.add_expense(5000, "Food", "Groceries")
    tracker.show_summary()
