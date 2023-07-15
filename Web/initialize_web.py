from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)


@app.route('/')
def index():
    if os.getenv('RUNNING_IN_DOCKER') is not None:
        host = "postgres-container"
    else:
        host = "localhost"

    conn = psycopg2.connect(
        host=host,
        database="postgres",
        user="postgres",
        password="postgre",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT title, img_urls FROM SREALITY;')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', data=rows)


def initialize_web():
    if os.getenv('RUNNING_IN_DOCKER') is not None:
        address = "0.0.0.0"
    else:
        address = "127.0.0.1"

    app.run(host=address, port=8080)


if os.getenv('RUNNING_IN_DOCKER') is not None:
    initialize_web()
