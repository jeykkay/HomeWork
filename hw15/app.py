from car import Car
from home import Home
from human import Human


def app():
    alex = Human('Alex')
    car = Car('Porshe', '911')
    home = Home('blvd. Riverside', '2505')
    for _ in range(40):
        alex.work()
    alex.buy_car(car)
    print(alex.car)
    alex.buy_home(home)
    print(alex.home)
    alex.sell(car)
    print(alex.car)
    alex.sell(home)
    print(alex.home)


app()
