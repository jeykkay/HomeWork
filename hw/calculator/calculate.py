def get_sum(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_pow(a, b):
    return a ** b


def calculate():
    while True:
        try:
            a = float(input('Entering the number: '))
            b = float(input('Entering the number: '))
            operation = input('Entering the operation: ')
            operations = {
                '+': get_sum,
                '-': minus,
                '*': multiply,
                '/': divide,
                '**': get_pow
            }
            get_math = operations[operation]
            print(get_math(a, b))
        except ValueError as err:
            print(f'a or b is not a number {err}')
        except ZeroDivisionError as err:
            print(f'Operation is not possible {err}')
            continue


calculate()