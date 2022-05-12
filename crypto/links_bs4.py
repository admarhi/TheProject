from urllib import request
from bs4 import BeautifulSoup as BS
import re

url = 'https://coinmarketcap.com/'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

currencies = []
list_curr = bs.find('table').find_all('a')
currencies = ['https://coinmarketcap.com' + curr['href'] for curr in list_curr]

for i in range(0, 99):
    print(currencies[i])
    html2 = request.urlopen(currencies[i])
    bs2 = BS(html2.read(), 'html.parser')
    print(bs2.h2.text) # Name of the currency
    print(bs2.find('div', {'class':"priceValue"}).text) # Value of the currency (USD)
    print(bs2.find('div', {'class':"statsValue"}).text) # Market cap
    print(bs2.find_all('div', {'class':"statsValue"})[4].text) # Volume traded in the last 24 hours
    print(bs2.find('div', {'class':"priceValue"}).nextSibling.text) # Change today
