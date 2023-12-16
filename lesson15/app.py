from car import Car
from home import Home
from human import Human


def app():
    alex = ('ALex', '3222323')
    car = ('Porsche', '911')
    home = ('ave. Malvern', '10')
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.work()
    alex.buy(car)
    print(alex.car)
    alex.buy(home)
    print(alex.home)
    alex.sell(car)
    alex.sell(home)


app()