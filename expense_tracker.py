import csv
import os

# Global variable for the CSV file path
CSV_FILE = 'expenses.csv'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_expenses():
    """Load expenses from the CSV file."""
    expenses = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    """Save expenses to the CSV file."""
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense():
    """Add a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))

    # Create a dictionary for the new expense
    new_expense = {'date': date, 'category': category, 'description': description, 'amount': amount}

    # Append the new expense to the expenses list
    expenses.append(new_expense)

def edit_expense():
    """Edit an existing expense."""
    display_expenses()
    index = int(input("Enter the index of the expense to edit: ")) - 1
    if 0 <= index < len(expenses):
        expense = expenses[index]
        print("Editing Expense:")
        print("1. Date:", expense['date'])
        print("2. Category:", expense['category'])
        print("3. Description:", expense['description'])
        print("4. Amount:", expense['amount'])
        field = input("Enter the field to edit (1-4): ")
        if field == '1':
            expense['date'] = input("Enter new date (YYYY-MM-DD): ")
        elif field == '2':
            expense['category'] = input("Enter new category: ")
        elif field == '3':
            expense['description'] = input("Enter new description: ")
        elif field == '4':
            expense['amount'] = float(input("Enter new amount: "))
        else:
            print("Invalid field.")
    else:
        print("Invalid index.")

def delete_expense():
    """Delete an existing expense."""
    display_expenses()
    index = int(input("Enter the index of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        del expenses[index]
        print("Expense deleted successfully.")
    else:
        print("Invalid index.")

def display_expenses():
    """Display all expenses."""
    if expenses:
        print("All Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")
    else:
        print("No expenses to display.")

def main():
    """Main function to run the Expense Tracker."""
    clear_screen()
    expenses = load_expenses()
    while True:
        # Display menu options
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. Display Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            edit_expense()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            display_expenses()
        elif choice == '5':
            save_expenses(expenses)
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
