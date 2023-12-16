from check_data import get_data
from users_base import get_users


def authentication():
    email, password = get_data()
    users = get_users()
    try:
        for user in users:
            if user['email'] == email and user['password'] == password:
                return f'Hello {email}'
    except KeyError:
        ...
    return 'Authentication wrong'