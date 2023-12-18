class Home:
    PRICE = 100

    def __init__(self, street, home_num):
        self.street = street
        self.home_num = home_num

    def __str__(self):
        return f'{self.street} - {self.home_num}'
