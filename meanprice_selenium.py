from pickle import FALSE
from pyparsing import Regex
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import re



def get_mean_price(url):
    gecko_path = '/usr/local/bin/geckodriver'
    ser = Service(gecko_path)
    options = webdriver.firefox.options.Options()
    options.headless = FALSE
    driver = webdriver.Firefox(options = options, service = ser)
    
    driver.get(url)
    time.sleep(5)
    prices = driver.find_elements(By.XPATH, '//span[contains(text(), "total") and @aria-hidden="true"]')
    results = []

    for i in prices:
        x = i.text
        m = re.findall('[0-9]+', x)
        n = int(m[0])
        results.append(n)

    return(sum(results)/len(results))



# url = 'https://www.airbnb.com/s/Warszawa/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Warszawa&place_id=ChIJAZ-GmmbMHkcR_NPqiCq-8HI&checkin=2022-05-09&checkout=2022-05-15&adults=2&source=structured_search_input_header&search_type=autocomplete_click&_set_bev_on_new_domain=1649331499_MTFjMWRmNTNmN2Yx&locale=en'
# print(get_mean_price(url))

