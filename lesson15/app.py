from car import Car
from home import Home
from human import Human


def app():
    alex = Human('Alex')
    car = Car('Porsche', '911')
    home = Home('blvd. Riverside', '2505')
    for _ in range(40):
        alex.work()
    alex.buy(car)
    print(alex.car)
    alex.buy(home)
    print(alex.home)
    alex.sell(car)
    alex.sell(home)


app()
