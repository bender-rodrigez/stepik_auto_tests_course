from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://dobro.website/login?__target_path=%2Fsettings"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.XPATH, "/html/body/div/div[7]/button")
    button.click()
    input1 = browser.find_element(By.NAME, "username")
    input1.send_keys("grishkovmikhail@gmail.com")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("891Bender___3535")
    button = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/button")
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()