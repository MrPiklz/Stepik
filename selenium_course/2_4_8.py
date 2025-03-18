from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def primer(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "100")
    )
button = browser.find_element(By.ID, "book")
button.click()

input1 = browser.find_element(By.ID, "input_value").text

input2 = browser.find_element(By.ID, "answer")
input2.send_keys(primer(int(input1)))

input3 = browser.find_element(By.ID, "solve")
input3.click()

message = browser.find_element(By.ID, "verify_message")
