import os
import psycopg2
from flask import Flask, jsonify
from datetime import time


app = Flask(__name__)

keys = ['CampaignId', 'Title', 'Content', 'maxMembers', 'minMembers', 'Owner', 'CreateAt', 'StartAt', 'EndAt', 'Available', 'status']

def preprocess_data(data_tuple):
    processed_data = []
    for item in data_tuple:
        if isinstance(item, time):
            processed_data.append(item.strftime('%H:%M:%S'))
        else:
            processed_data.append(item)
    return tuple(processed_data)


def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            port=os.getenv('DB_PORT'),
                            database=os.getenv('DB_DATABASE'),
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route("/")
def hello_world():
    return "<p>Welcome To The Fionn Page</p>"


@app.route('/campaign')
def test():
    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute('SELECT * FROM campaign')
    
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    print(data[0])
    processed_data = preprocess_data(data[0])
    data_dict = dict(zip(keys, processed_data))
    
    return jsonify(data_dict)