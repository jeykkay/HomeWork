from car import Car
from home import Home


def home_condition_purchase(person, bank_account, car, home):
    if car:
        if bank_account >= 100:
            bank_account.decrease_money(Home.PRICE)
            person.home = home
        else:
            print(f'You have not money')
    else:
        print('Buy a car first')


def car_condition_purchase(person, bank_account, car):
    if bank_account >= 40:
        bank_account.decrease_money(Car.PRICE)
        person.car = car
    else:
        print(f'You have not money')
