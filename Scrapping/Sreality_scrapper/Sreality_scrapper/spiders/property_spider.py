import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from collections import OrderedDict


class Property(scrapy.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._values = OrderedDict()

    title = scrapy.Field()
    img_urls = scrapy.Field()


class PropertyLoader(ItemLoader):
    default_item_class = Property
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    img_urls_out = MapCompose()


class PropertySpider(scrapy.Spider):
    name = "property-spider"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"]

    def parse_flat(self, response):
        flat_loader = PropertyLoader(response=response)
        flat_loader.add_value('title', response.json().get("name", {}).get("value"))
        img_urls = [image["_links"]["view"]["href"] for image in response.json().get("_embedded", {}).get("images", [])
                    if image["_links"].get("view")]
        flat_loader.add_value('img_urls', img_urls)

        yield flat_loader.load_item()

    def parse(self, response):
        estates = response.json().get("_embedded", {}).get("estates", [])
        for estate in estates:
            estate_url = f"https://www.sreality.cz/api{estate['_links']['self']['href']}"
            yield scrapy.Request(estate_url, callback=self.parse_flat)
