from pages.base_page import base_page
from selenium.webdriver.common.by import By

class LogoutPage(base_page):
    HAMBURGER_MENU_BUTTON = (By.XPATH,'//*[@id="react-burger-menu-btn"]')
    LOGOUT_BUTTON = (By.XPATH , '//*[@id="logout_sidebar_link"]')

    def clicking_hamburger_menu(self):
        self.click(self.HAMBURGER_MENU_BUTTON)
    
    def clicking_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    

    