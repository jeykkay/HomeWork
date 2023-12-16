import json


def add_user(user):
    try:
        with open('my.json', "r") as file:
            users = json.load(file)
            users.append(user)

        with open('my.json',"w") as file_write:
            json.dump(users, file_write)
    except FileNotFoundError:
        with open('my.json', "w") as file:
            json.dump([user], file)


def get_emails():
    try:
        with open('my.json', "r") as file:
            users = json.load(file)

        emails = []
        for user in users:
            emails.append(user['email'])

        return emails
    except FileNotFoundError as err:
        print(f'File not created {err}')
        return []

def get_users():
    try:
        with open('my.json', "r") as file:
            users = json.load(file)
        return users
    except FileNotFoundError as err:
        print(f'File not created {err}')
        return [{}]

