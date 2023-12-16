from authentication import authentication
from registration import registration


data={
    'reg':registration,
    'auth':authentication
}


def app():
    try:
        string = input(f'Select: {[k for k in data.keys()]}')
        func = data[string]
        print(func())
    except KeyError as err:
        print(f'Wrong {err}')


app()