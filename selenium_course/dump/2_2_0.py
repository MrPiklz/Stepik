from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



def sum(x, y):
    return str(int(x)+int(y))


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num_1 = browser.find_element(By.ID, "num1").text
    num_2 = browser.find_element(By.ID, "num2").text
    y = sum(num_1,num_2)
        
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла