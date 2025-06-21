import json
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(data['account_number'], data['name'], data['balance'])


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = self.next_account_number
        self.next_account_number += 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"\nAccount Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}\n")
        else:
            print("Error: Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"Deposited ${amount:.2f} successfully.")
            else:
                print("Error: Deposit amount must be positive.")
        else:
            print("Error: Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew ${amount:.2f} successfully.")
            else:
                print("Error: Insufficient balance or invalid amount.")
        else:
            print("Error: Account not found.")

    def save_to_file(self):
        data = {
            'accounts': {str(k): v.to_dict() for k, v in self.accounts.items()},
            'next_account_number': self.next_account_number
        }
        with open('accounts.txt', 'w') as f:
            json.dump(data, f)

    def load_from_file(self):
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as f:
                data = json.load(f)
                self.accounts = {int(k): Account.from_dict(v) for k, v in data['accounts'].items()}
                self.next_account_number = data.get('next_account_number', 1001)


def main():
    bank = Bank()

    while True:
        print("\n==== Bank Menu ====")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter your name: ")
            try:
                deposit = float(input("Enter initial deposit: "))
                if deposit < 0:
                    raise ValueError
                bank.create_account(name, deposit)
            except ValueError:
                print("Invalid deposit amount.")

        elif choice == '2':
            try:
                acc_no = int(input("Enter account number: "))
                bank.view_account(acc_no)
            except ValueError:
                print("Invalid account number.")

        elif choice == '3':
            try:
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(acc_no, amount)
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            try:
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(acc_no, amount)
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            print("Thank you for using the bank system!")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()
