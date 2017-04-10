from scrapy.spiders import XMLFeedSpider
from SeekingAlpha.items import SeekingalphaItem
from scrapy.http import Request

class MySpider(XMLFeedSpider):
    name = 'SAXML'
    allowed_domains = ['seekingalpha.com']
    start_urls = [#'https://seekingalpha.com/feed/stock-ideas/quick-picks.xml',
                  'https://seekingalpha.com/feed/stock-ideas/long-ideas.xml'] # Put your URL here
    iterator = 'iternodes'
    itertag = 'item'

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse_node(self, response, node):
        item = SeekingalphaItem()
        item['title'] = node.xpath('//title/text()').extract()[1]
        item['link'] = node.xpath('//link/text()').extract()[1]
        item['author'] = node.xpath('//author/text()').extract()
        item['guid'] = node.xpath('//guid/text()').extract()
        item['pubDate'] = node.xpath('//pubDate/text()').extract()
        item['tickers']=node.xpath('//category/text()').extract()

        return item

# scrapy crawl SAXML -o Articles.csv -t csv
# https://seekingalpha.com/account/ajax_get_comments?id=4059712&type=Article