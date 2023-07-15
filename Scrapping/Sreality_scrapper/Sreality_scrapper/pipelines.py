import psycopg2
import os
import time


class PostgresPipeline:
    def __init__(self):
        self.conn = None
        self.curr = None

        self.create_connection()

    def create_connection(self):
        if os.getenv('RUNNING_IN_DOCKER') is not None:
            host = "postgres-container"
        else:
            host = "localhost"

        self.conn = psycopg2.connect(
            host=host,
            database="postgres",
            user="postgres",
            password="postgre",
            port="5432"
        )

        self.curr = self.conn.cursor()

    def store_in_db(self, item):
        while True:
            self.curr.execute(f"SELECT to_regclass('SREALITY');")
            if self.curr.fetchone()[0] is not None:
                break
            else:
                print("Table does not exist yet. Waiting...")
                time.sleep(5)

        try:
            self.curr.execute(""" INSERT INTO SREALITY (title, img_urls) VALUES(%s, %s);""",
                              (item["title"], item["img_urls"]))
        except BaseException as e:
            print(e)
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item