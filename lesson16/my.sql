create database food_base

create table users
(
    id integer NOT NULL UNIQUE, --unique id
    name CHAR(50) NOT NULL --no more than 50 characters

);

create table product
(
    product_id integer NOT NULL UNIQUE, --unique id
    name CHAR(50) NOT NULL, --no more than 50 characters
);

create table meal
(
    meal_id integer NOT NULL UNIQUE, --unique id
    user_id integer references users(id),--a foreign key linking an user_id from the meal table to an id from the users table
    product_id integer references product(product_id),--a foreign key linking an product_id from the meal table to an product_id from the product table
);