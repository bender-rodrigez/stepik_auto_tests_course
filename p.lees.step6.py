from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type ='submit']" )
    button.click()
finally:
     time.sleep(10)
     browser.quit()
