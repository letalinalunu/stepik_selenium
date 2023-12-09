from selenium import webdriver
import time
import math
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/explicit_wait2.html")
def result(x):
    return math.log(abs(12*math.sin(int(x))))
try:
    WebDriverWait(driver,15).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button1 = driver.find_element(By.ID, "book").click()
    print('Im click bitch')
    # time.sleep(5)
    # alert1 = driver.switch_to.alert.accept() #переключаемся на алерт
    # driver.switch_to.window(driver.window_handles[1]) #переключаемся на новое окно
    x = driver.find_element(By.ID, "input_value").text
    input = driver.find_element(By.ID, "answer").send_keys(result(x))
    button2 = driver.find_element(By.ID, "solve").click()
    allert2 = driver.switch_to.alert
    pyperclip.copy(allert2.text.split(':')[-1])
    allert2.accept()

    # button = driver.find_element(By.TAG_NAME, "button")
    # driver.execute_script("window.scrollBy(0, 150);")
    # river.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.location_once_scrolled_into_view # скролл методами драйвера
    # time.sleep(20)
    # input.send_keys(result(x))
    # option1 = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    # option1.click()
    # option2 = driver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    # option2.click()
  # input = driver.find_element(By.ID, "answer")
    time.sleep(2)
    # button.click()
    # time.sleep(20)

finally:
    driver.quit()
#time.sleep(5)