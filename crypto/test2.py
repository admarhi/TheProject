from urllib import request
from bs4 import BeautifulSoup as BS
import pandas as pd

html2 = request.urlopen('https://coinmarketcap.com/currencies/bancor/')
bs2 = BS(html2.read(), 'html.parser')

# print(bs2.h2.text) # Name of the currency
print(bs2.find('div', {'class':"priceValue"}).text) # Value of the currency (USD)
print(bs2.find('div', {'class':"statsValue"}).text) # Market cap
print(bs2.find_all('div', {'class':"statsValue"})[4].text) # Volume traded in the last 24 hours
print(bs2.find('div', {'class':"priceValue"}).nextSibling.text) # Change today

