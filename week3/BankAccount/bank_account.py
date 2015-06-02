class BankAccount:
    
    def __init__(self, name, balance, currency):
        self._name = name
        self.__balance = balance
        self._currency = currency

    def __str__(self):
        return 'Bank account for {} with balance of {}{}'.format(self._name, self.__balance, self._currency)

    def __int__(self):
        return self.__balance

    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return True
        return False

    def transfer_to(self, account, amount):
        if self._currency == account._currency:
            self.__balance -= amount
            account.__balance += amount
            return True
        return False
