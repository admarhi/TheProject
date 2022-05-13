import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class GetLinksSpider(scrapy.Spider):
    name = 'get_links'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['http://coinmarketcap.com/']

    def parse(self, response):
        xpath = '//a[@class="cmc-link" and re:test(@href, "/currencies/[^/]*/$")]/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'http://coinmarketcap.com' + s.get()
            yield l