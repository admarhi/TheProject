
from fake_useragent import UserAgent 
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)

options = Options()
options.headless = True
# driver = webdriver.Firefox(options=options)

userAgent = UserAgent().random
options.add_argument(f'user-agent={userAgent}')

# firefox_binary = webdriver.firefox.bin('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
# driver = webdriver.Firefox(options = options, service = ser, firefox_binary=firefox_binary)

driver = webdriver.Firefox(options = options, service = ser)

url = 'https://coinmarketcap.com/'
driver.get(url)
time.sleep(3)

links = driver.find_elements(by = By.XPATH, value = '//a[starts-with(@href, "/currencies/")]')
driver.quit()
output_data = []

for i in range(len(links)):
    url = links[i].text
    driver.get(url)
    time.sleep(2)

    name = driver.find_element(by = By.XPATH, value = '//h2').text
    value = driver.find_element(by = By.XPATH, value = '//div[@class="priceValue "]').text
    change = driver.find_element(by = By.XPATH, value = '//div[@class="priceValue "]/following-sibling::span').text

    stats = driver.find_elements(by = By.XPATH, value ='//div[@class="statsValue"]')
    marketCap = stats[0].text
    volumeTraded = stats[4].text
    driver.quit()
    print(name)
    print(value)
    print(change)
    print(marketCap)
    print(volumeTraded)
    output_data.append([name, value, change, marketCap, volumeTraded])

print(output_data)
