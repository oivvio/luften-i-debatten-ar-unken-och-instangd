# -*- coding: utf-8 -*-

BOT_NAME = 'scrapyproject'

SPIDER_MODULES = ['scrapyproject.spiders']
NEWSPIDER_MODULE = 'scrapyproject.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 300
}


HTTPCACHE_POLICY = 'scrapy.contrib.httpcache.DummyPolicy'
HTTPCACHE_STORAGE = 'scrapy.contrib.httpcache.DbmCacheStorage'

HTTPCACHE_ENABLED = True

#DEPTH_LIMIT = 1
DEPTH_LIMIT = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'luften_är_unken_och_instängd (+http://www.liberationtech.net)'


ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']

IMAGES_STORE = '/tmp/dnimages'
