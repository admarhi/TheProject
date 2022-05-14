import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class GetLinksSpider(scrapy.Spider):
    name = 'get_links'
    allowed_domains = ['coinmarketcap.com']
    limiter = True
    if limiter:
        start_urls = ['https://coinmarketcap.com']
    else:
        numpages = 102
        start_urls = ['https://coinmarketcap.com/?page='+str(i) for i in range(numpages)] 

    def parse(self, response):
        xpath = '//a[@class="cmc-link" and re:test(@href, "/currencies/[^/]*/$")]/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'http://coinmarketcap.com' + s.get()
            yield l
    

    def close(self, reason):
        start_time = self.crawler.stats.get_value('start_time')
        finish_time = self.crawler.stats.get_value('finish_time')
        print("Total run time: ", finish_time-start_time)
        total = finish_time-start_time
        with open("times_getlinks.txt", "a") as f:
            f.write(str(total)+'\n')

################# Total run time:  0:00:03.982606 ##############