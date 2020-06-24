import scrapy

class BlogPost(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    published_at = scrapy.Field()