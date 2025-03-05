from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Bender")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Rodrigez")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("rodrigez.b@mail.com")
    current_dir = os.path.abspath(os.path.dirname("p2.less.step8.py"))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'ntcrn текст.txt')           # добавляем к этому пути имя файла 
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "[type ='submit']" )
    button.click()

finally:
     time.sleep(10)
     browser.quit()

