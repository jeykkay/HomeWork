class Home:
    PRICE = 100

    def __init__(self, street, num_home):
        self.street = street
        self.num_home = num_home

    def __str__(self):
        return f'{self.street}, {self.num_home}'
