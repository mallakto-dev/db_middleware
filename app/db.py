from dotenv import load_dotenv
import psycopg2
from os import getenv
from datetime import datetime


SITE_ID = 161

load_dotenv()


def connect():
    database = getenv('DATABASE_URL')
    conn = psycopg2.connect(database)
    return conn


def add_order(order_raw):
    conn = connect()

    current_date_raw = datetime.now()
    current_date = f'{current_date_raw.year}-{current_date_raw.month}-{current_date_raw.day}'

    order = serialize_order(order_raw)
    order['order_status'] = 'активен'
    order['created_at'] = current_date
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO orders (user_id, order_items, order_type, order_status, created_at, total_cost, user_name, user_phone, user_address)
            VALUES (%(user_id)s, %(order_items)s, %(order_type)s, %(order_status)s, %(created_at)s, %(total_cost)s, %(user_name)s, %(user_phone)s, %(user_address)s)
            RETURNING order_id""",
            order
        )
        order_id = cursor.fetchone()[0]
        conn.commit()
        return order_id


def serialize_order(order_dict):
    order_items = ''.join(list(map(lambda d: f"{d.get('title')}: *{d.get('quantity')}*\n", order_dict.get('order'))))
    serialized_order = {'user_id': SITE_ID,
                        'order_items': order_items,
                        'order_type': order_dict.get('delivery'),
                        'total_cost': order_dict.get('total'),
                        'user_name': order_dict.get('nameInput'),
                        'user_phone': order_dict.get('phone'),
                        'user_address': order_dict.get('address')
                        }
    return serialized_order

