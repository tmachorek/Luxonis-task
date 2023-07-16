import time
import psycopg2
import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Sreality_scrapper.Sreality_scrapper.spiders.property_spider import PropertySpider

while True:
    try:
        if os.getenv('RUNNING_IN_DOCKER') is not None:
            host = "postgres"
        else:
            host = "localhost"

        conn = psycopg2.connect(
            host=host,
            database="postgres",
            user="postgres",
            password="postgre",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("select * from information_schema.tables where table_name=%s", ('SREALITY',))
        if bool(cur.rowcount):
            conn.close()
            print("Ready for Scrapy")
            break

        print("Table does not exist.")
        conn.close()
        time.sleep(1)
    except psycopg2.OperationalError:
        print("Db not up")
        time.sleep(5)


settings = get_project_settings()

PropertySpider.custom_settings={"ITEM_PIPELINES": {"Sreality_scrapper.Sreality_scrapper.pipelines.PostgresPipeline": 300}}

process = CrawlerProcess(settings)
process.crawl(PropertySpider)
process.start()
