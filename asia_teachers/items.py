import scrapy

class AsiaTeachersItem(scrapy.Item):
    name = scrapy.Field()
    expertise = scrapy.Field()
