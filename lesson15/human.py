from car import Car
from home import Home
from random import randint


class Human:
    def __init__(self, name):
        self.name = name
        self.home = None
        self.car = None
        self._bank_account = 0

    @property
    def bank_account(self):
        return self._bank_account

    def __str__(self):
        return f'{self.name}'

    def work(self):
        salary = randint(5, 11)
        self._bank_account += salary

    def buy(self, person):
        if self._bank_account >= 40:
            self._bank_account -= 40
            person.car = Car
        elif person.car == Car and self._bank_account >= 100:
            self._bank_account -= 100
            person.home = Home
        else:
            print('Not enough money')

    def sell(self, choice):
        if choice == self.car:
            self._bank_account += 40
            self.car = None
            print('You sold the car')
        elif choice == self.home:
            self._bank_account += 100
            self.home = None
            print('You sold the home')
        else:
            print('Nothing to sell')
