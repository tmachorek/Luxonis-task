from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Sreality_scrapper.Sreality_scrapper.spiders.property_spider import PropertySpider

settings = get_project_settings()

PropertySpider.custom_settings={"ITEM_PIPELINES": {"Sreality_scrapper.Sreality_scrapper.pipelines.PostgresPipeline": 300}}

process = CrawlerProcess(settings)
process.crawl(PropertySpider)
process.start()
