from fake_useragent import UserAgent 
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from csv import writer
import re
import time

start_time = time.time()

gecko_path = '/usr/local/bin/geckodriver'
gecko_path = '/home/nights/Desktop/WEBSCRAPING/geckodriver'
ser = Service(gecko_path)

options = Options()
options.headless = True
# userAgent = UserAgent().random
# options.add_argument('user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
driver = webdriver.Firefox(options = options, service = ser)

limiter = True
if limiter:
    url = 'https://coinmarketcap.com/?page=1'
    driver.get(url)
    time.sleep(3)
    # list_curr = driver.find_elements(by = By.XPATH, value = '//a[@class="cmc-link" and re:test(@href, "/currencies/.*/$")]/@href')
    # xpath = '//a[@class="cmc-link" and re:test(@href, "\/currencies/[^/]*/$")]/@href'
    xpath = '//a[starts-with(@href, "/currencies/")]'
    list_curr = driver.find_elements(by = By.XPATH, value = xpath)
else:
    urls = ['https://coinmarketcap.com/?page='+str(i) for i in range(100)]
    list_curr = []
    for url in urls:
        driver.get(url)
        time.sleep(3)
        xpath = '//a[starts-with(@href, "/currencies/")]'
        list_curr.append(driver.find_elements(by = By.XPATH, value = xpath))

links = [link.get_attribute('href') for link in list_curr]

print('#####################################')
# for s in list_curr:
#     print(s.text)
    # links.append('http://coinmarketcap.com/' + s.text) 

# links = ['https://coinmarketcap.com' + curr['href'] for curr in list_curr]

print('#####################################')
print(links)
print('#####################################')

regex = re.compile("https:\/\/coinmarketcap\.com\/currencies\/[a-z]+-*[a-z]+\/$")
clean_links = [s for s in links if regex.match(s)]

print('#####################################')
print(clean_links)
print('#####################################')


for i in range(len(clean_links)):
    try:
        url = clean_links[i]
        print("############## This is the url", url)
        driver.get(url)
        time.sleep(3)
        name = driver.find_element(by = By.XPATH, value = '//h2').text
        value = driver.find_element(by = By.XPATH, value = '//div[@class="priceValue "]').text
        change = driver.find_element(by = By.XPATH, value = '//div[@class="priceValue "]/following-sibling::span').text
        stats = driver.find_elements(by = By.XPATH, value ='//div[@class="statsValue"]')
        marketCap = stats[0].text
        volumeTraded = stats[4].text
        
        output_data = [name, value, change, marketCap, volumeTraded]
        # file = open('selenium_results.csv', 'a', newline='')
        with open('selenium_results.csv', 'a', newline='') as file:
            writer_object = writer(file)
            writer_object.writerow(output_data)
            file.close()
    except:
        print(clean_links[i], 'is not working')
driver.quit()

#print difference between current time at the end and start time
print("RUNTIME --- %s seconds ---" % (time.time() - start_time))

################# RUNTIME --- 437.41893911361694 seconds --- ##########
#### without waiting times, estimated: 134 seconds