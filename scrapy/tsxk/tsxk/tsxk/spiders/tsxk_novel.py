import scrapy
import re
from tsxk import items


class TsxkNovelSpider(scrapy.Spider):
    name = 'tsxk_novel'
    # allowed_domains = ['tsxk.com']
    start_urls = ['https://www.zmccx.com/50_50817/']
    base_urls = 'https://www.zmccx.com'

    def parse(self, response):
        pargram = re.findall('<dt>《吞噬星空》正文</dt>(.*?)<div id="footer" name="footer"', response.body.decode("utf-8"),
                             re.S)[0]
        href = re.findall("href='(.*?)'", pargram, re.S)
        for url in href:
            url_t = self.base_urls + url
            yield scrapy.Request(url_t, callback=self.parse_info, meta={"url": url_t})

    def parse_info(self, response):
        item = items.TsxkItem()
        link = response.meta["url"]
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        content = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<', response.body.decode("utf-8"), re.S)
        content = "\n".join(content)
        # content = re.findall('id="content">(.*?)推荐', response.body.decode("utf-8"), re.S)[0]
        item["title"] = title
        item["content"] = content
        item["link"] = link
        yield item
