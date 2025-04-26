class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -{amount}")

    @property
    def balance(self):
        return self._balance

    def get_transactions(self):
        return self._transactions


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)
print(account.get_transactions())