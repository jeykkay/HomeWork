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
        return f'Name: {self.name}'

    def work(self):
        salary = randint(5, 11)
        self._bank_account += salary

    def buy_car(self, car):
        if self._bank_account >= 40:
            self.car = car
            print('You bought a car')
        else:
            print('You dont have money')

    def buy_home(self, home):
        if self.car is not None and self._bank_account >= 100:
            self.home = home
            print('You purchased a house')
        elif self.car is None:
            print('Buy a car first')
        else:
            print('You dont have money')

    def sell(self, choice):
        if choice == self.car:
            self._bank_account += Car.PRICE
            self.car = None
            print('You sold the car')
        elif choice == self.home:
            self._bank_account += Home.PRICE
            self.home = None
            print('You sold the home')
        else:
            print('Nothing to sell')
