import os
import time
import psycopg2
import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Sreality_scrapper.Sreality_scrapper.spiders.property_spider import PropertySpider

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

curr = conn.cursor()

while True:
    curr.execute(f"SELECT to_regclass('SREALITY');")
    if curr.fetchone()[0] is not None:
        break
    else:
        logging.info("Table does not exist yet. Waiting...")
        time.sleep(1)

conn.close()

settings = get_project_settings()

PropertySpider.custom_settings={"ITEM_PIPELINES": {"Sreality_scrapper.Sreality_scrapper.pipelines.PostgresPipeline": 300}}

process = CrawlerProcess(settings)
process.crawl(PropertySpider)
process.start()
