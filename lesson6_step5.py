from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
link = "http://suninjuly.github.io/find_link_text"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    link.click()
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("myash")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Rusmyack")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()