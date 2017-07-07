# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcfunArticleSpiderItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    comment_nums = scrapy.Field()
    view_nums = scrapy.Field()
    fav_nums = scrapy.Field()
