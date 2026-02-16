"""
Name: Jay Genao
Date: February 16, 2026
Program Description:
This program asks the user to enter their monthly expenses by category.
It uses the reduce function to calculate the total expenses and determines
the highest and lowest expense entered. The program then displays the
total expense, highest expense, and lowest expense with proper labels.
"""

from functools import reduce


def collect_expenses():
    """
    Collects expense categories and amounts from the user.

    Parameters:
        None

    Variables:
        expenses (list): Stores tuples of (expense_name, amount)
        name (str): The expense category entered by the user
        amount (float): The expense amount entered by the user
        more (str): Controls loop continuation

    Logic:
        1. Ask user for expense name.
        2. Ask user for expense amount.
        3. Store as tuple in list.
        4. Ask if user wants to enter another expense.
        5. Repeat until user stops.

    Return:
        list: List of (expense_name, amount) tuples
    """

    expenses = []

    while True:
        name = input("Enter expense category (example: Rent, Food, Utilities): ")
        amount = float(input("Enter the amount for this expense: $"))

        expenses.append((name, amount))

        more = input("Do you want to enter another expense? (yes/no): ").lower()
        if more != "yes":
            break

    return expenses


def analyze_expenses(expenses):
    """
    Analyzes the list of expenses.

    Parameters:
        expenses (list): List of (expense_name, amount) tuples

    Variables:
        total (float): Total monthly expenses
        highest (tuple): Highest expense tuple
        lowest (tuple): Lowest expense tuple

    Logic:
        1. Use reduce to calculate total expense.
        2. Use max to find highest expense.
        3. Use min to find lowest expense.

    Return:
        tuple: (total, highest, lowest)
    """

    total = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    highest = max(expenses, key=lambda x: x[1])
    lowest = min(expenses, key=lambda x: x[1])

    return total, highest, lowest


def main():
    """
    Main program function.

    Parameters:
        None

    Variables:
        expenses (list): User-entered expenses
        total (float): Total expenses
        highest (tuple): Highest expense
        lowest (tuple): Lowest expense

    Logic:
        1. Call collect_expenses.
        2. Call analyze_expenses.
        3. Display results clearly.

    Return:
        None
    """

    print("---- Monthly Expense Tracker ----")

    expenses = collect_expenses()

    total, highest, lowest = analyze_expenses(expenses)

    print("\n--- Expense Summary ---")
    print(f"Total Monthly Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()
