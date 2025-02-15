from pages.base_page import base_page
from selenium.webdriver.common.by import By
import time


class CheckoutPage(base_page):
    #locators for Checkout page
    FIRST_NAME_FIELD = (By.XPATH , '//*[@id="first-name"]')
    LAST_NAME_FIELD  = (By.XPATH , '//*[@id="last-name"]')
    POSTAL_CODE_FIELD = (By.XPATH ,'//*[@id="postal-code"]')
    CONTINUE_BUTTON = (By.XPATH , '//*[@id="continue"]' )
    TOTAL_AMOUNT = (By.XPATH , '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
    FINAL_THANKYOU_MESSAGE = (By.XPATH , '//*[@id="checkout_complete_container"]/h2')

    #function for adding the checkout details
    def checkout_process(self, first_name, last_name, postal_code):
        time.sleep(2)
        self.enter_text(self.FIRST_NAME_FIELD , first_name)
        time.sleep(2)
        self.enter_text(self.LAST_NAME_FIELD , last_name)
        time.sleep(2)
        self.enter_text(self.POSTAL_CODE_FIELD , postal_code)
        time.sleep(2)
        self.click(self.CONTINUE_BUTTON)
        time.sleep(2)

    #function for returning the total amount displayed on checkout page
    def getting_total_amount(self):
        total_text = self.get_text(self.TOTAL_AMOUNT)
        return float(total_text.replace("Total: $", "").strip()) 

    #function for clicking the finish button
    def clicking_finish(self):
        self.click(self.FINISH_BUTTON)
    
    #function for returning  success message
    def checking_success_message(self):
        return self.get_text(self.FINAL_THANKYOU_MESSAGE)

        

    


