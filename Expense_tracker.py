import json
from datetime import datetime


class ExpenseTracker:
    def __init__(self, total_budget):
        self.total_budget = total_budget
        self.expenses = []
        self.remaining_money = total_budget

    def add_expense(self, date, description, amount, category="General"):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > self.remaining_money:
            print("Not enough remaining money for this expense.")
            return

        self.expenses.append({"date": date, "description": description, "amount": amount, "category": category})
        self.remaining_money -= amount
        print(f"Expense added: {description} (${amount:.2f}).")

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            self.remaining_money += removed["amount"]
            print(f"Removed expense: {removed['description']} (${removed['amount']:.2f}).")
        else:
            print("Invalid index.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print(f"{'Index':<5} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount':<10}")
        print("-" * 65)
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i:<5} {exp['date']:<12} {exp['description']:<20} {exp['category']:<15} ${exp['amount']:<10.2f}")

    def view_summary(self):
        total_spent = sum(exp["amount"] for exp in self.expenses)
        print("\n--- Budget Summary ---")
        print(f"Total Expenses: ${total_spent:.2f}")
        print(f"Remaining Money: ${self.remaining_money:.2f}")

    def utilize_remaining_money(self):
        print("\n--- Ideas for Remaining Money ---")
        if self.remaining_money > 0:
            print(f"You can still use ${self.remaining_money:.2f} for:")
            print("- Saving for future goals.")
            print("- Treating yourself with something small.")
            print("- Investing in hobbies or education.")
            print("- Donating to a good cause.")
        else:
            print("No remaining money to utilize. Time to review your expenses!")

    def export_expenses(self, filename="expenses.json"):
        with open(filename, "w") as file:
            json.dump(self.expenses, file, indent=4)
        print(f"Expenses exported to {filename}.")

    def import_expenses(self, filename="expenses.json"):
        try:
            with open(filename, "r") as file:
                self.expenses = json.load(file)
                self.remaining_money = self.total_budget - sum(exp["amount"] for exp in self.expenses)
            print(f"Expenses imported from {filename}.")
        except FileNotFoundError:
            print(f"{filename} not found.")


def main():
    try:
        budget = float(input("Enter your total budget: "))
        if budget <= 0:
            print("Budget must be a positive number.")
            return

        tracker = ExpenseTracker(budget)

        while True:
            print("\nMenu:")
            print("1. Add Expense")
            print("2. Remove Expense")
            print("3. View Expenses")
            print("4. View Summary")
            print("5. Utilize Remaining Money")
            print("6. Export Expenses")
            print("7. Import Expenses")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                try:
                    date = input("Enter the date (YYYY-MM-DD): ")
                    description = input("Enter the description: ")
                    amount = float(input("Enter the amount: "))
                    category = input("Enter the category (default: General): ") or "General"

                    try:
                        datetime.strptime(date, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format. Use YYYY-MM-DD.")
                        continue

                    tracker.add_expense(date, description, amount, category)
                except ValueError:
                    print("Invalid input. Please enter valid data.")
            elif choice == "2":
                try:
                    index = int(input("Enter the expense index to remove: ")) - 1
                    tracker.remove_expense(index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == "3":
                tracker.view_expenses()
            elif choice == "4":
                tracker.view_summary()
            elif choice == "5":
                tracker.utilize_remaining_money()
            elif choice == "6":
                tracker.export_expenses()
            elif choice == "7":
                tracker.import_expenses()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    except ValueError:
        print("Invalid budget. Please enter a numeric value.")


if __name__ == "__main__":
    main()



