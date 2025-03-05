from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://alumoart.ru/contacts")
    #input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']") 
    #input1.send_keys("Жельдере")
    #input2 = browser.find_element(By.CSS_SELECTOR, "[type='tel']")
    #input2.send_keys("+700000000")
    #input3 = browser.find_element(By.CSS_SELECTOR, "[type='email']")
    #input3.send_keys("noreal@nowhere.uz")
    select = Select(browser.find_element(By.ID, "sb-1724673743309"))
    select.select_by_value("Ковдор") 
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()