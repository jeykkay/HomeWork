class BankAccount:
    bank_accounts = set()

    def __init__(self, num):
        self.acc_num = f'{num}__bank_account'
        if self.acc_num in self.bank_accounts:
            raise ValueError(f'This bank account already exists')

        self.__amount = 0

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f'{self.amount}'

    def increase_money(self, amount):
        self.__amount += amount

    def decrease_money(self, amount):
        self.__amount -= amount
