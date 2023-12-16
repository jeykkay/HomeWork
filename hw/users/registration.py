from users_base import add_user, get_emails
from check_data import get_data


def registration():
    while True:
        email, password = get_data()
        users = get_emails()

        if email in users:
            print('This email already exists, try again')
            continue
        else:
            user = {'email': email, 'password': password}
            add_user(user)
            break
    return 'User successfully registered'


