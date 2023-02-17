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
    #TODO: figure out how to find the elements on the popupwindow;
    
    EXPEDIA_URL = 'https://www.expedia.com.br/passagens-aereas'
    
    browser.get(EXPEDIA_URL)

    select_departure_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_BUTTON)))
    select_departure_button.click()
    flight_from = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_PATH)))
    flight_from.clear()
    flight_from.send_keys(' ' + departure)
    flight_from.send_keys(Keys.ENTER)
    
    # find_first_item_dep = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, './/*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]/div/div/div[1]/section/div[2]/div[2]/div[1]/div/ul/li[1]/div/button')))
    # ActionChains(browser).move_to_element(find_first_item_dep).click().perform()
    # find_first_item_dep.send_keys(Keys.ENTER)
    
    # select_arrival_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, EXPEDIA_ARRIVAL_BUTTON)))
    # select_arrival_button.click()
    # flight_to = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, EXPEDIA_ARRIVAL_PATH)))
    # flight_to.clear()
    # flight_to.send_keys(' ' + arrival)
    # find_first_item_arrv = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'uitk-action-list-item-content')]")))
    # ActionChains(browser).move_to_element(find_first_item_arrv).click().perform()
    
    
    # departure_date = browser.find_element(by=By.XPATH, value=EXPEDIA_DEPARTURE_DATE)
    # departure_date.clear()
    # departure_date.send_keys(going_dt.day + '/' + going_dt.month + '/' + going_dt.year)
    
    # arrival_date = browser.find_element(by=By.XPATH, value=EXPEDIA_ARRIVAL_DATE)
    # arrival_date.clear()
    # arrival_date.send_keys(returning_dt.day + '/' + returning_dt.month + '/' + returning_dt.year)
    
    

def decolar_scrapper(origin, departure, going_dt, returning_dt):
    #TODO: add web scrapper for Decolar
    DECOLAR_URL = 'https://www.decolar.com/'
    