from pages.base_page import base_page
from selenium.webdriver.common.by import By
import time


class LoginPage(base_page):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH , '//*[@id="login_button_container"]/div/form/div[3]')

    def login(self, username, password):
        time.sleep(2)
        self.enter_text(self.USERNAME_FIELD, username)
        time.sleep(2)
        self.enter_text(self.PASSWORD_FIELD, password)
        time.sleep(2)
        self.click(self.LOGIN_BUTTON)
        


    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
        
