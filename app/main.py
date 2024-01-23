from flask import Flask, request
import app.db as db

app = Flask(__name__)

@app.post('/add')
def add_order():
    order_dict = request.get_json()
    order_id = str(db.add_order(order_dict))
    return order_id
