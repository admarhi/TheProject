
from operator import itemgetter
import pandas as pd
from bs4 import BeautifulSoup as BS
from urllib import request
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

def get_cities():
    url = 'https://en.wikipedia.org/wiki/List_of_largest_cities'
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')
    table = bs.find('table',{'class':"wikitable"})
    df = pd.read_html(str(table))
    df = pd.concat(df)
    return df.iloc[1:, 0]
    

def get_city_page(destination, number_people):
    # Get the url
    url = 'https://www.airbnb.com/'
    driver.get(url)
    time.sleep(3)

    # Input Destination
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
    user_location = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
    user_location.send_keys(destination)

    # Input Date
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[3]/div[1]').click()
    # checkin_date = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='datepicker-day-2022-05-19']"))).click()
    # checkout_date = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='datepicker-day-2022-05-22']"))).click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='datepicker-day-%s']"%checkin_date))).click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='datepicker-day-%s']"%checkout_date))).click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[5]/div[1]').click()

    # Input Number of People
    svg_xpath = "/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[6]/div/section/div/div/div[1]/div[1]/div[2]/button[2]/span/*[name()='svg']/*[name()='path']"
    element = driver.find_element(by=By.XPATH, value=svg_xpath)
    actions = ActionChains(driver)
    for i in range(number_people):
        actions.move_to_element(element).click().perform()
        i += 1
    
    # Execute Search
    driver.find_element(By.CLASS_NAME, value='_kaq6tx').click()

    # Return the Results
    # city = destination
    result_url = driver.current_url
    return(result_url)


def get_mean_price(city_url):
    driver.get(city_url)
    time.sleep(3)
    try:
        prices = driver.find_elements(By.XPATH, '//span[contains(text(), "total") and @aria-hidden="true"]')
        results = []
        for i in prices:
            x = i.text
            m = re.findall('[0-9,]+', x) # finds the price with comma
            n = int(m[0].replace(',','')) # removes the comma and converst to int
            print(n)
            results.append(n)
        return(sum(results)/len(results))
    except:
        return('No matches found')


# Init:
gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)
# options = webdriver.chrome.options.Options()
options = webdriver.firefox.options.Options()
options.headless = False
# driver = webdriver.Chrome(options = options, service=ser)

number_people = int(input('How many people will be traveling? (int) '))
checkin_date = str(input('When will you check in? (YYYY-MM-DD)'))
checkout_date = str(input('When will you check out? (YYYY-MM-DD)'))

start=time.time()
x = get_cities()
driver = webdriver.Firefox(options = options, service = ser)
price_dict = {}
for i in x:
    city_url = get_city_page(i, number_people)
    print(city_url)
    city_price = get_mean_price(city_url)
    print(city_price)
    price_dict[i] = city_price
    # print(price_dict)
end = time.time()
print('Running time: %s Seconds'%(end-start))
print('##################')
print('The Top 5 cheapest destinations are:')
print(dict(sorted(price_dict.items(), key = itemgetter(1))[:5]))


