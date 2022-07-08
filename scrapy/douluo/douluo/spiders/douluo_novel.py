import scrapy
import re
from douluo import items


class DouluoNovelSpider(scrapy.Spider):
    name = 'douluo_novel'
    # allowed_domains = ['douluo.com']
    start_urls = ['https://www.zmccx.com/54_54196/']
    base_urls = "https://www.zmccx.com"

    def parse(self, response):
        pargram = re.findall('<dt>《斗罗大陆》正文</dt>(.*?)<div id="footer" name="footer"', response.body.decode("utf-8"),
                             re.S)[0]
        href = re.findall("href='(.*?)'", pargram, re.S)
        for url in href:
            url_t = self.base_urls + url
            yield scrapy.Request(url_t, callback=self.parse_info, meta={"url": url_t})

    def parse_info(self, response):
        item = items.DouluoItem()
        link = response.meta["url"]
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        content = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<', response.body.decode("utf-8"), re.S)
        content = "\n".join(content)
        item["title"] = title
        item["content"] = content
        item["link"] = link
        yield item
