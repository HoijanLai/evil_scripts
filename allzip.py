from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class get_js_page(url, username=None, password=None, target_elem='')
    browser = webdriver.Firefox()
    browser.get(url)
    
    # simulate bahavior on page
    user_elem = browser.find_element_by_id("username")
    pass_elem = browser.find_element_by_id("password")
    user_elem.send_keys(username)
    pass_elem.send_keys(password)
    browser.find_element_by_name("submit").click()

    # get the soup cook
    delay = 3
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, target_elem)))
    bsObj = BeautifulSoup(browser.page_source)

    return bsObj
    
def utils(bsObj):
    pass

