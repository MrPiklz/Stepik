from selenium import webdriver
import os
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/redirect_accept.html"

def mmath(x):
    return str(math.log(abs(12*math.sin(x))))
    

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    
    
    input1 = browser.find_element(By.ID, "input_value").text

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(str(mmath(int(input1))))

    button = browser.find_element(By.TAG_NAME, "button")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла