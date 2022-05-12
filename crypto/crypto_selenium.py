
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Init:
gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)

# Choose betwee chrome or firefox

# options = webdriver.chrome.options.Options()
options = webdriver.firefox.options.Options()
# driver = webdriver.Chrome(options = options, service=ser)
driver = webdriver.Firefox(options = options, service = ser)
options.headless = True # set to True to disable browse window


url = 'https://coinmarketcap.com/'
driver.get(url)
time.sleep(3)
# table = driver.find_element_by_xpath('//tbody')
table = driver.find_elements(by = By.XPATH, value = '//a[@class="cmc-link" and re:test(@href, "/currencies/[^/]*/$")]/@href')
driver.quit()
print(table)
for a in table:
    print(a)

