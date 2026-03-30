"""
Name: Jay Genao
Date: February 30, 2026

Program Description:
This program creates a BankAcct class that stores account details and allows
depositing, withdrawing, adjusting interest rates, and calculating interest
based on days. It also includes a test function to demonstrate all features.
"""


class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        # Simple interest formula
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate}%"
        )


def test_bank_account():
    print("=== Creating Account ===")
    account = BankAcct("Jay Genao", "123456", 1000.00, 5)

    print("\n--- Initial Account ---")
    print(account)

    print("\n--- Deposit $500 ---")
    account.deposit(500)
    print(f"New Balance: ${account.get_balance():.2f}")

    print("\n--- Withdraw $200 ---")
    account.withdraw(200)
    print(f"New Balance: ${account.get_balance():.2f}")

    print("\n--- Adjust Interest Rate to 6% ---")
    account.adjust_interest_rate(6)
    print(account)

    print("\n--- Calculate Interest for 30 days ---")
    interest = account.calculate_interest(30)
    print(f"Interest earned in 30 days: ${interest:.2f}")


if __name__ == "__main__":
    test_bank_account()