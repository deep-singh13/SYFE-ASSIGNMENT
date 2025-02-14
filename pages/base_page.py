from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class base_page:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver , 10)
        
    
    def find_element(self , locator):
        logging.info(f"finding element {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        logging.info(f"clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        logging.info(f"enterong text in element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        logging.info(f"getting text from element :{locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text


