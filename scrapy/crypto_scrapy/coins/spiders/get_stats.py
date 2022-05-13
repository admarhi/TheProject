import scrapy

class Values(scrapy.Item):
    currency = scrapy.Field()
    value = scrapy.Field()
    market_cap = scrapy.Field()
    volume = scrapy.Field()
    change = scrapy.Field()    

class GetValuesSpider(scrapy.Spider):
    name = 'get_stats'
    allowed_domains = ['coinmarketcap.com']
    try:
        with open("linkkk.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):

        v = Values()
        v['currency'] = currency_name = response.xpath('//h2/text()').get()
        
        v['value'] = response.xpath('//div[@class="priceValue "]//text()').get()
        v['change'] = response.xpath('//div[@class="priceValue "]/following-sibling::span//text()').get()
        v['market_cap'] = response.xpath('//div[@class="statsValue"]//text()').get()
        v['volume'] = response.xpath('//div[@class="statsValue"]//text()').getall()[4]

        yield v

