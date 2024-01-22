from flask import Flask, request
import os
from dotenv import load_dotenv
import db

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.post('/add')
def add_order():
    order_dict = request.get_json()
    order_id = str(db.add_order(order_dict))
    return order_id
