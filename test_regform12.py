import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegForms12(unittest.TestCase):


    def test_form1(self):
        # self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH,
                                          "/html/body/div/form/div[1]/div[1]/input[@class='form-control first']")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH,
                                          "/html/body/div/form/div[1]/div[2]/input[@class='form-control second']")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH,
                                          "/html/body/div/form/div[1]/div[3]/input[@class='form-control third']")
            input3.send_keys("sosok@ya.ru")
            input4 = browser.find_element(By.XPATH,
                                          "/html/body/div/form/div[2]/div[1]/input[@class='form-control first']")
            input4.send_keys("89001234567")
            input5 = browser.find_element(By.XPATH,
                                          "/html/body/div/form/div[2]/div[2]/input[@class='form-control second']")
            input5.send_keys("MazaFaka c.")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # time.sleep(3)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

            browser.close()
            browser.quit()
            self.assertEqual(welcome_text,"Congratulations! You have successfully registered!", "Test form2 fail")



    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH,
                                      "/html/body/div/form/div[1]/div[1]/input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH,
                                      "/html/body/div/form/div[1]/div[2]/input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH,
                                      "/html/body/div/form/div[1]/div[3]/input[@class='form-control third']")
        input3.send_keys("sosok@ya.ru")
        input4 = browser.find_element(By.XPATH,
                                      "/html/body/div/form/div[2]/div[1]/input[@class='form-control first']")
        input4.send_keys("89001234567")
        input5 = browser.find_element(By.XPATH,
                                      "/html/body/div/form/div[2]/div[2]/input[@class='form-control second']")
        input5.send_keys("MazaFaka c.")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        browser.close()
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test form2 fail")
        # self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()




