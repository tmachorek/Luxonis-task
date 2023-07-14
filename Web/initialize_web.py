from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgre",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT title, img_urls FROM SREALITY')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', data=rows)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
