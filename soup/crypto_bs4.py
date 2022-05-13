import urllib
from bs4 import BeautifulSoup as BS
import re
from urllib import request

url = 'https://coinmarketcap.com/'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser', from_encoding="iso-8859-1")
# print(bs)

currencies = []
list_curr = bs.find("table").find_all('a', {'href': re.compile('\/currencies\/[a-z]+/$')})
currencies = ['https://coinmarketcap.com' + curr['href'] for curr in list_curr]
# print(currencies)
output_data = []

for url2 in currencies:
    print(url2)
    html2 = request.urlopen(url2)
    bs2 = BS(html2.read(), 'html.parser', from_encoding="iso-8859-1")
    try:
        name = bs2.h2[2].text # Name of the currency
        value = bs2.find('div', {'class':"priceValue"}).text # Value of the currency (USD)
        marketCap = bs2.find('div', {'class':"statsValue"}).text # Market cap
        volumeTraded = bs2.find_all('div', {'class':"statsValue"})[4].text # Volume traded in the last 24 hours
        change = bs2.find('div', {'class':"priceValue"}).nextSibling.text # Change today
        output_data.append([name, value, change, marketCap, volumeTraded])
    except:
        print(f'Error scraping {url2}')

print(output_data)