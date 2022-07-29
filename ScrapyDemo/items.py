# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBookItem(scrapy.Item):
    table_name='book'
    # define the fields for your item here like:
    name = scrapy.Field()
    author=scrapy.Field()
    desc=scrapy.Field()
    price = scrapy.Field()
    img_url = scrapy.Field()
    createtime = scrapy.Field()
class ScrapyBookUrlItem(scrapy.Item):
    table_name = 'bookurl'
    # define the fields for your item here like:
    name = scrapy.Field()
    url=scrapy.Field()
    createtime = scrapy.Field()
