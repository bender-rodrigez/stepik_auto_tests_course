from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
   browser = webdriver.Chrome()
   browser.get("http://suninjuly.github.io/get_attribute.html")
   def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
   x_element = browser.find_element(By.ID, "treasure")
   x = x_element.get_attribute("valuex")
   print(x)
   #print("value of treasure: ", x_element)
   #assert x_element is not None, 
   y = calc(x)
   input = browser.find_element(By.ID, "answer")
   input.send_keys(y)
   option1 = browser.find_element(By.ID, "robotCheckbox")
   option1.click()
   option1 = browser.find_element(By.ID, "robotsRule")
   option1.click()
   button = browser.find_element(By.CSS_SELECTOR, "[type ='submit']" )
   button.click()

finally:
 time.sleep(10)
 browser.quit()