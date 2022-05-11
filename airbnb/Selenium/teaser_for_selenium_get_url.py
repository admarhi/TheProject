# _*_ coding : utf-8 _*_
# @Time : 2022/4/27 18:43
# @Author : KAI XING 389862
# @File : airbnb
# @Project : Selenium.py

import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

start=time.time()
# Init:
gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False

# driver = webdriver.Chrome(options = options, service=ser)
driver = webdriver.Firefox(options = options, service = ser)

url = 'https://www.airbnb.com/?_set_bev_on_new_domain=1651079392_OWRlZTY1NTFhNTg5&enable_auto_translate=false&locale=en'

# Actual program:
driver.get(url)
time.sleep(3)
#Input Location
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

user_location = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#my_location = input('Where are you going:')
my_location = 'Warszawa'
user_location.send_keys(my_location)

#Input date
driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[3]/div[1]').click()

checkin_date = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='datepicker-day-2022-05-20']"))).click()

checkout_date = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='datepicker-day-2022-05-22']"))).click()

driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[5]/div[1]').click()

# #Input persons

svg_xpath = "/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[6]/div/section/div/div/div[1]/div[1]/div[2]/button[2]/span/*[name()='svg']/*[name()='path']"
element = driver.find_element(by=By.XPATH, value=svg_xpath)
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
actions.move_to_element(element).click().perform()

# #Search
driver.find_element(By.CLASS_NAME, value='_kaq6tx').click()

city = my_location

scrapyUrl = driver.current_url
print(city)
print(scrapyUrl)



def get_mean_price(scrapyUrl):
    driver.get(scrapyUrl)
    time.sleep(5)
    prices = driver.find_elements(By.XPATH, '//span[contains(text(), "total") and @aria-hidden="true"]')
    results = []
    for i in prices:
        x = i.text
        m = re.findall('[0-9]+', x)
        n = int(m[0])
        results.append(n)

    return(sum(results)/len(results))

print(get_mean_price(scrapyUrl))


end=time.time()
print('Running time: %s Seconds'%(end-start))
driver.quit()
