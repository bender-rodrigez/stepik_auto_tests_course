from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    button.click()
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "[type ='submit']" )
    button2.click()

finally:
     time.sleep(10)
     browser.quit()