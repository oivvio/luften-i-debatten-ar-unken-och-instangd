from scrapy.item import Item, Field

class DNImageByline(Item):
    image_urls = Field()
    images = Field()

