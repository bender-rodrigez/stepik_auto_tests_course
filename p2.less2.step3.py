from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    c = (int(a)+int(b))
    print(c)
    #from selenium.webdriver.support.ui import Select
    #from selenium.webdriver.support.select import Select
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(c)) 
    button = browser.find_element(By.CSS_SELECTOR, "[type ='submit']" )
    button.click()

finally:
   time.sleep(10)
   browser.quit()
    