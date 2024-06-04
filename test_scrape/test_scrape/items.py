# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScrapeItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    upc = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()


class TestScrapeQuote(scrapy.Item):
    quote=scrapy.Field()
    author=scrapy.Field()
    author_link=scrapy.Field()
    tags=scrapy.Field()