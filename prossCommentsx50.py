from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle

driver = webdriver.Chrome()

driver.get("https://85.26.202.125:4443/incidents2/auth")

# Ожидание загрузки страницы
time.sleep(5)
input1 = driver.find_element(By.CSS_SELECTOR,"[type = 'text']" )
input1.send_keys("GrishkovM124")
input2 = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div/div[2]/form/div[2]/div[1]/input" )
input2.send_keys("GrishkovM124")
time.sleep(2)
button = driver.find_element(By. XPATH, "/html/body/div/div[1]/div/div/div/div[2]/form/button")
button.click()
time.sleep(5)
cookies = driver.get_cookies()
with open("cookies.pkl", "wb") as file:
     pickle.dump(cookies, file)
time.sleep(5)
driver.get("https://85.26.202.125:4443/incidents2/event-archive/20250131063908_2667_0?return=/dashboard")


# Текст комментария
#comment_text = "Это тестовый комментарий."

# Количество повторений
#num_comments = 5

#for i in range(num_comments):
    # Находим поле для ввода комментария
    #comment_box = driver.find_element(By.CSS_SELECTOR, "form-group__input")  # Замените "comment" на актуальный атрибут name или id
    
    # Вводим текст комментария
   # comment_box.send_keys(comment_text)
    
    # Находим кнопку отправки комментария
    #submit_button = driver.find_element(By.XPATH, "//html/body/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[3]/div[2]/div/div[2]/form/div[2]/button")  # Замените XPath на актуальный
    
    # Нажимаем кнопку отправки
    #submit_button.click()
    
    # Ожидание перед следующим комментарием (чтобы избежать блокировки)
    #time.sleep(2)

# Закрытие браузера
#driver.quit()