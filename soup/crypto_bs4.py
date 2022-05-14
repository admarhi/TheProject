from bs4 import BeautifulSoup as BS
import re
from urllib import request
from csv import writer
import requests
import time

start_time = time.time()

limiter = True
if limiter:
    url = 'https://coinmarketcap.com/'
    r = requests.get(url)
    bs = BS(r.content, features="lxml")
    list_curr = bs.find('table').find_all('a', {'href': re.compile('\/currencies\/[a-z]+-*[a-z]+\/$')})
else:
    urls = ['https://coinmarketcap.com/?page='+str(i) for i in range(100)]
    list_curr = []
    for url in urls:
        r = requests.get(url)
        bs = BS(r.content)
        list_curr.append(bs.find('table').find_all('a', {'href': re.compile('\/currencies\/[a-z]+-*[a-z]+\/$')}))

currencies = ['https://coinmarketcap.com' + curr['href'] for curr in list_curr]

for url2 in currencies:
    try:
        #print(url2)
        r2 = requests.get(url2)
        bs2 = BS(r2.content, features="lxml")
        name = bs2.h2.text # Name of the currency
        value = bs2.find('div', {'class':"priceValue"}).text # Value of the currency (USD)
        marketCap = bs2.find('div', {'class':"statsValue"}).text # Market cap
        volumeTraded = bs2.find_all('div', {'class':"statsValue"})[4].text # Volume traded in the last 24 hours
        change = bs2.find('div', {'class':"priceValue"}).nextSibling.text # Change today
        output_data = [name, value, change, marketCap, volumeTraded]
        with open('soup_results.csv', 'a', newline='') as file:
            writer_object = writer(file)
            writer_object.writerow(output_data)
            file.close()
    except:
        print(f'Error scraping {url2}')
     

#print difference between current time at the end and start time
print("RUNTIME --- %s seconds ---" % (time.time() - start_time))

############### RUNTIME --- 22.203864097595215 seconds ---###############
############### without printing: 17.457253217697144 seconds ############
