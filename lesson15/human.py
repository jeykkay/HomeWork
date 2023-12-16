from random import randint
from bank_account import BankAccount
from car import Car
from home import Home


class Human:
    created_passport_number = set()

    def __init__(self, name, passport_num):
        if passport_num in self.created_passport_number:
            raise ValueError("This passport number is already taken")
        self.name = name
        self.passport_num = passport_num
        bank_acc = BankAccount(self.passport_num)
        self.__bank_account = bank_acc
        self.car = None
        self.house = None

    def __str__(self):
        return f'Name: {self.name}\nPassport Number: {self.passport_num}'

    def work(self):
        salary = randint(5, 11)
        self.__bank_account.increase_money(salary)

    def buy(self, choice):
        ...

    def sell(self, choice):
        ...
