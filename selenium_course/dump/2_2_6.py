from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



def func(x):
    return str(math.log(abs(12*math.sin(x))))


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.ID, "input_value").text
    
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(func(int(x)))

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла