from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def page_login(url, username=None, password=None):
    browser = webdriver.Firefox()
    browser.get(url)
    # simulate bahavior on page
    user_elem = browser.find_element_by_id("username")
    pass_elem = browser.find_element_by_id("password")
    user_elem.send_keys(username)
    pass_elem.send_keys(password)
    browser.find_element_by_name("submit").click()

    return browser

def render_and_get(browser, target_elem_id='', delay=3):
    # get the soup cook
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, target_elem_id)))
    bsObj = BeautifulSoup(browser.page_source, "html.parser")
    return bsObj

def get_all_extension(bsObj, ext='.zip', filter_mark=''):
    links = []
    for atag in bsObj.findAll('a'):
        link = atag.get('href')
        if link and ext in link and filter_mark in link:
            links.append(link)
    return links

# This main will use selenium to render page and collect elements from html
if __name__ == "__main__":
    url = ''
    browser = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs')
    browser.get(url)
    bsObj = render_and_get(browser, 'main-content')
    links = get_all_extension(bsObj)

    with open('data_link.txt', 'w') as f:
        for link in links:
            f.write(link+'\n')
