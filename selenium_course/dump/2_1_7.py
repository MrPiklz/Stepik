from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "treasure")
    x_element_val = x_element.get_attribute("valuex")
    #x = x_element.text
    y = calc(x_element_val)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    time.sleep(30)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла