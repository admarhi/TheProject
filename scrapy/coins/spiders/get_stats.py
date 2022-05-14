import scrapy
import time

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
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):

        v = Values()
        v['currency'] = response.xpath('//h2/text()').get()
        
        v['value'] = response.xpath('//div[@class="priceValue "]//text()').get()
        v['change'] = response.xpath('//div[@class="priceValue "]/following-sibling::span//text()').get()
        v['market_cap'] = response.xpath('//div[@class="statsValue"]//text()').get()
        v['volume'] = response.xpath('//div[@class="statsValue"]//text()').getall()[4]

        yield v

    def close(self, reason):
        start_time = self.crawler.stats.get_value('start_time')
        finish_time = self.crawler.stats.get_value('finish_time')
        total = finish_time-start_time
        with open("times.txt", "a") as f:
            f.write(str(total)+'\n')
        print("Total run time: ", total)


############# Total run time:  0:12:15.489774
############# estimated without delay between crawls - ? either 135 seconds - roughly the same as selenium
############# or 435 s, which would be much longer.