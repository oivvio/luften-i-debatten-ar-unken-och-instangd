from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapyproject.items import DNImageByline
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


def dnparse(self, response):
        hxs = HtmlXPathSelector(response)
        bylines = hxs.select("//span[@class='middle-quote-photo']//img[@class='byline']")
        items = []
        for byline in bylines:
            item = DNImageByline()
            urls = []
            incomplete_urls = byline.select('@src').extract()
            for incomplete_url in incomplete_urls:
                if incomplete_url.find("//") == 0:
                    incomplete_url = "http:" + incomplete_url
                if incomplete_url.find("/Images") == 0:
                    incomplete_url = "http://www.dn.se" + incomplete_url
                urls.append(incomplete_url)

            item['image_urls'] = urls
            items.append(item)
        return items


class DNSpider(CrawlSpider):
    name = "dn"
    allowed_domains = ["dn.se"]
    start_urls = ["http://www.dn.se/ekonomi"]

    rules = (
        Rule(SgmlLinkExtractor(), follow=True, callback='parse_item'),
    )

    parse_item = dnparse
