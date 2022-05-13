from multiprocessing.connection import wait
from requests import request
import scrapy
from scrapy_splash import SplashRequest
from urllib.parse import urlencode


class TotalPrice(scrapy.Item):
    price = scrapy.Field()
    has_wifi = scrapy.Field()
    #//div[text()="Wifi"]

class ChoosePricesSpider(scrapy.Spider):
    name = 'choose_prices'
    
    def start_requests(self):
        start_urls = ["https://www.hotels.com/search.do?destination-id=11594&q-check-in=2022-05-11&q-check-out=2022-05-12&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER"]

        for url in start_urls:
            lua_script = """
            function main(splash, args)
                splash.images_enabled = false 
                local num_scrolls = 10
                local scroll_delay = 1

                local scroll_to = splash:jsfunc("window.scrollTo")
                local get_body_height = splash:jsfunc(
                    "function() {return document.body.scrollHeight;}"
                    )
                assert(splash:go(splash.args.url))
                splash:wait(5)

                for _ = 1, num_scrolls do
                    local height = get_body_height()
                    for i = 1, 10 do
                        scroll_to(0, height * i/10)
                        splash:wait(scroll_delay/10)
                    end
                end
    
                return splash:html()
            end
            """
            headers = {'User-Agent': 'Scrapy/1.3.0 (+http://scrapy.org)'}
            #url = "https://stackoverflow.com/questions/41075257/adding-a-wait-for-element-while-performing-a-splashrequest-in-python-scrapy"
            yield SplashRequest(url, self.parse, 
                    endpoint='execute', 
                    args={'lua_source':lua_script, 'timeout': 3600}, 
                    headers=headers,
                    meta={'handle_httpstatus_all': True},
                    
            ) 

    def parse(self, response):
        #xpath = '//span[contains(text(), "total")]'
        xpath = '//a[@class="_61P-R0"]'
        # and @aria-hidden="true"]'
        #contains(text(), "total")
        #selection = response
        #xpath(xpath).extract_first()
        l = TotalPrice()
        l['price'] = response.xpath(xpath)
        yield l


        #.singleNodeValue;
        '''                local get_spans = splash:jsfunc([[
                    function getElementByXpath(path) {
                    var spans = document.evaluate('//span[contains(text(), "total")]',document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    return spans;
                        }
                    ]])

                    return get_spans().node.outerHTML
                    

                    endpoint='render.html', 

                    '''


'''
surethings:
                splash:set_viewport_full()
                splash.private_mode_enabled = false
                splash.indexeddb_enabled = true
                splash.html5_media_enabled = true

infinite scrolling:
function main(splash)
        local num_scrolls = 10
        local scroll_delay = 1

        local scroll_to = splash:jsfunc("window.scrollTo")
        local get_body_height = splash:jsfunc(
            "function() {return document.body.scrollHeight;}"
        )
        assert(splash:go(splash.args.url))
        splash:wait(splash.args.wait)

        for _ = 1, num_scrolls do
            local height = get_body_height()
            for i = 1, 10 do
                scroll_to(0, height * i/10)
                splash:wait(scroll_delay/10)
            end
        end        
        return splash:html()
end


'''