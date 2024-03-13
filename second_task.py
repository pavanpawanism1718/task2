from collections import defaultdict

class BudgetTracker:
    def __init__(self, file_path='budget.txt'):
        self.file_path = file_path
        self.budget = self.load_budget()

    def load_budget(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                income = float(lines[0].strip())
                expenses = [{'category': line.split(',')[0], 'amount': float(line.split(',')[2])} for line in lines[1:]]
                return {'income': income, 'expenses': expenses}
        except (FileNotFoundError, IndexError, ValueError):
            return {'income': 0, 'expenses': []}

    def save_budget(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.budget['income']) + '\n')
            for expense in self.budget['expenses']:
                file.write(f"{expense['category']},{expense['amount']}\n")

    def add_income(self, amount):
        self.budget['income'] += amount
        self.save_budget()
        print("Income added successfully!")

    def add_expense(self, category, amount):
        self.budget['expenses'].append({'category': category, 'amount': amount})
        self.save_budget()
        print("Expense added successfully!")

    def view_balance(self):
        balance = self.get_balance()
        print(f"Your current balance is ${balance:.2f}")

    def expense_analysis(self):
        self.analyze_expenses()

    def get_balance(self):
        total_expenses = sum(expense['amount'] for expense in self.budget['expenses'])
        return self.budget['income'] - total_expenses

    def get_expense_by_category(self):
        expenses_by_category = defaultdict(float)
        for expense in self.budget['expenses']:
            expenses_by_category[expense['category']] += expense['amount']
        return dict(expenses_by_category)

    def analyze_expenses(self):
        expenses_by_category = self.get_expense_by_category()
        total_expenses = sum(expenses_by_category.values())
        print("Expense Analysis:")
        for category, amount in expenses_by_category.items():
            percentage = (amount / total_expenses) * 100
            print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")

if __name__ == "__main__":
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Balance\n4. Expense Analysis\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            budget_tracker.add_income(amount)

        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_expense(category, amount)

        elif choice == '3':
            budget_tracker.view_balance()

        elif choice == '4':
            budget_tracker.expense_analysis()

        elif choice == '5':
            break
