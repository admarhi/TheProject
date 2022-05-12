
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = True # set to True to disable browse window
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
