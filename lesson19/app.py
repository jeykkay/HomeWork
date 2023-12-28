from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sympy import Product

app = Flask(__name__)

client = app.test_client()
engine = create_engine('postgresql+psycopg2://esmr:qwerty@localhost/esmr_db')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from table import *

Base.metadata.create_all(bind=engine)


@app.route('/', method=['GET'])
def get_list():
    products = Product.query.all()
    serialized = []
    for product in products:
        serialized.append({
            'id': product.id,
            'product_name': product.product_name,
            'proteins': product.proteins,
            'carbs': product.carbs,
            'fats': product.fats
        })
    return jsonify(serialized)


@app.route('/', methods=['POST'])
def add_list():
    new_one = Product(**request.json)
    session.add(new_one)
    session.commit()
    serialized = {
        'id': new_one.id,
        'product_name': new_one.product_name,
        'proteins': new_one.proteins,
        'carbs': new_one.carbs,
        'fats': new_one.fats
    }
    return jsonify(serialized)


@app.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    item = Product.query.filter(Product.id == product_id).first()
    nutrients = request.json
    if not item:
        return {'message: This id not found'}, 400
    for key, value in nutrients.items():
        setattr(item, key, value)
    session.commit()
    serialized = {
        'id': item.id,
        'product_name': item.product_name,
        'proteins': item.proteins,
        'carbs': item.carbs,
        'fats': item.fats
    }
    return serialized


@app.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    item = Product.query.filter(Product.id == product_id).first()
    if not item:
        return {'message: Product not found'}, 400
    session.delete(item)
    session.commit()
    return '', 204


@app.teardown_appcontext
def close_session():
    session.remove()


if __name__ == '__main__':
    app.run(debug=True)
