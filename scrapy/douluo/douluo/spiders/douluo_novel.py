import scrapy


class DouluoNovelSpider(scrapy.Spider):
    name = 'douluo_novel'
    allowed_domains = ['douluo.com']
    start_urls = ['http://douluo.com/']

    def parse(self, response):
        pass
