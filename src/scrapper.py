import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
from chromedriver_py import binary_path
from main import *
from src.paths import *

service_object = Service(binary_path)
browser = webdriver.Chrome(service=service_object)

def expedia_scrapper(departure, arrival, going_dt, returning_dt):
    #TODO: add 'select_button' for both dates;
    
    EXPEDIA_URL = 'https://www.expedia.com.br/passagens-aereas'
    
    browser.get(EXPEDIA_URL)

    select_departure_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_BUTTON)))
    select_departure_button.click()
    flight_from = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_PATH)))
    flight_from.clear()
    flight_from.send_keys(' ' + departure)
    find_first_item = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'uitk-button')]")))
    browser.execute_script("arguments[0].scrollIntoView(true)", find_first_item)
    ActionChains(browser).move_to_element(find_first_item).click().perform()
    
    # select_arrival_button = browser.find_element(by=By.XPATH, value=EXPEDIA_ARRIVAL_BUTTON)
    # t.sleep(1)
    # select_arrival_button.click()
    # flight_to = browser.find_element(by=By.XPATH, value=EXPEDIA_ARRIVAL_PATH)
    # t.sleep(1)
    # flight_to.clear()
    # flight_to.send_keys(' ' + arrival)
    # t.sleep(1.5)
    # first_item = browser.find_element(by=By.XPATH, value=EXPEDIA_ARRIVAL_FIRST_ITEM)
    # t.sleep(1.5)
    # first_item.click()
    
    # departure_date = browser.find_element(by=By.XPATH, value=EXPEDIA_DEPARTURE_DATE)
    # departure_date.clear()
    # departure_date.send_keys(going_dt.day + '/' + going_dt.month + '/' + going_dt.year)
    
    # arrival_date = browser.find_element(by=By.XPATH, value=EXPEDIA_ARRIVAL_DATE)
    # arrival_date.clear()
    # arrival_date.send_keys(returning_dt.day + '/' + returning_dt.month + '/' + returning_dt.year)
    
    

def decolar_scrapper(origin, departure, going_dt, returning_dt):
    #TODO: add web scrapper for Decolar
    DECOLAR_URL = 'https://www.decolar.com/'
    