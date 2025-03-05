from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

link = "https://dobro.website/login?__target_path=%2Fsettings"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, "/html/body/div/div[7]/button")
    button.click()
    button = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/p/a")
    button.click()
    time.sleep(2)
    input1 = browser.find_element(By.NAME, "firstName")
    input1.send_keys("Бендер")
    input2 = browser.find_element(By.NAME, "lastName")
    input2.send_keys("Родригез")
    #input3 = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div[4]/div/div[1]/div/div/input")
    #input3.click()
    #input3.send_keys(keyword.CONTROL + "a")
    #input3.send_keys("Сызрань")
    input4 = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div[5]/div/div/div[1]/div/input")
    input4.click()
    input4.send_keys("11.01.1991")
    input4.click()
    #input4 = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[4]/div[5]/div/span")
    #input4.click()
    input5 = browser.find_element(By.CSS_SELECTOR, "[type='email']")
    input5.send_keys("grishkovmikhail@gmail.com")
    input5 = browser.find_element(By.CSS_SELECTOR, ".FormPhoneInput_form__phone__o6ANr")
    input5.click()
    input5.send_keys("9000000000")
    input6 = browser.find_element(By.CSS_SELECTOR, "[type='password']")
    input6.send_keys("ggg!G12")
    input6 = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div[9]/div/div[1]/input")
    input6.send_keys("ggg!G12")
    #input7 = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div[10]/label")
    #input7.click()
    option1 = browser.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div[10]/label/span/span/span")
    option1.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type ='submit']")
    button.click()



    




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()