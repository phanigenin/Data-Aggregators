__author__ = 'phani'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from SeekingAlpha.items import SeekingalphaItem

class MySpider(BaseSpider):
    name = "SA"
    allowed_domains = ["seekingalpha.com"]
    start_urls = ["https://seekingalpha.com/stock-ideas","https://seekingalpha.com/feed/stock-ideas/quick-picks"]

    def parse(self, response):
        print(response)
        titles=response.selector.xpath("//p")
        items=[]
        for titles in titles:
            item=SeekingalphaItem()
            item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return items

# scrapy crawl SA -o Articles.csv -t csv