from random import randint


def game():
    def get_random():
        while True:
            print('Hello,entering range!')
            start = int(input('Entering start range: '))
            end = int(input('Entering end range: '))
            if 1 <= len(range(start, end)) <= 3:
                l = set()
                while len(l) < 3:
                    l.add(randint(start, end))
                break
        return list(l)

    def input_user():
        get_list = set()
        while len(get_list) < 3:
            a = input('Entering number: ')
            if a == 'exit':
                print('Bye')
                quit()
            else:
                get_list.add(int(a))
        return list(get_list)

    def count(numbers, random_numbers):
        user_numbers = []
        for i in numbers:
            if i in random_numbers:
                user_numbers.append(i)
        return len(user_numbers)

    def get_check():
        range_numbers = get_random()
        while True:
            user_numbers = input_user()
            quantity = count(user_numbers, range_numbers)
            print(f'You guess {quantity} of 3 numbers')
            if quantity == 3:
                print('You win')
            else:
                print('Try again')

    get_check()


game()
