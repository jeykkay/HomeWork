def users(cursor):
    name = input('Entering name: ')
    cursor.execute(
        f"INSERT INTO users (name) VALUES ('{name}')"
    )
    return cursor.fetchone()


def product(cursor):
    name = input('Entering product: ')
    proteins = float(input('Entering proteins: '))
    fats = float(input('Entering proteins: '))
    carbs = float(input('Entering proteins: '))
    cursor.execute(
        f"INSERT INTO product (name, proteins, fats, carbs) VALUES ('{name}', {proteins}, {fats}, {carbs})"
    )
    return cursor.fetchone()


def meal(cursor, users_id, product_id):
    cursor.execute(
        f"INSERT INTO meal (user_id, product_id) VALUES ({users_id}, {product_id})"
    )
