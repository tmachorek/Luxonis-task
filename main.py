import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from Scrapping.Sreality_scrapper.Sreality_scrapper.spiders.property_spider import PropertySpider
from Web.initialize_web import initialize_web


def initialize_spider():
    settings = get_project_settings()

    process = CrawlerProcess(settings)
    process.crawl(PropertySpider)
    process.start()


def main():
    initialize_spider()

    if os.getenv('RUNNING_IN_DOCKER') is None:
        initialize_web()


if __name__ == '__main__':
    main()
