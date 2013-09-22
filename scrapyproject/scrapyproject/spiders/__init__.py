from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapyproject.items import DNImageByline
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


def dnparse(self, response):
        hxs = HtmlXPathSelector(response)
        bylines = hxs.select("//span[@class='photo']//img[@class='byline']")
        items = []
        for byline in bylines:
            item = DNImageByline()
            item['image_urls'] = byline.select('@src').extract()
            items.append(item)
        return items


class DNSpider(CrawlSpider):
    name = "dn"
    allowed_domains = ["dn.se"]
    start_urls = ["http://www.dn.se/"]

    rules = (
        Rule(SgmlLinkExtractor(), follow=True, callback='parse_item'),
    )

    parse_item = dnparse
