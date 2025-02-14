from pages.base_page import base_page
from selenium.webdriver.common.by import By
import time


class InventoryPage(base_page):
    FILTER_DROPDOWN = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    FILTER_PRICE_LOW_TO_HIGH = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')
    ADD_TO_CART_BACKPACK = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    ADD_TO_CART_BIKE_LIGHT = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    CART_COUNT = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    ITEM_NAME_ONESIE = (By.XPATH, '//*[@id="item_2_title_link"]/div')
    ADD_TO_CART = (By.XPATH, '//*[@id="add-to-cart"]')
    CART_BUTTON = (By.XPATH , '//*[@id="shopping_cart_container"]/a')
    

    def sort_low_to_high(self):
        self.click(self.FILTER_DROPDOWN)
        time.sleep(2)
        self.click(self.FILTER_PRICE_LOW_TO_HIGH)
        time.sleep(2)
    
    def add_items_to_cart(self):
        time.sleep(2)
        self.click(self.ADD_TO_CART_BACKPACK)
        time.sleep(2)
        self.click(self.ADD_TO_CART_BIKE_LIGHT)
        time.sleep(2)
    
    def get_cart_count(self):
        time.sleep(2)
        return int(self.get_text(self.CART_COUNT))
    
    def go_to_product_page(self):
        time.sleep(2)
        self.click(self.ITEM_NAME_ONESIE)
        time.sleep(2)

    def add_items_from_product_page(self):
        time.sleep(2)
        self.click(self.ADD_TO_CART)      
        time.sleep(2)
    
    def clicking_cart_icon(self):
        self.click(self.CART_BUTTON)
        time.sleep(2)


    



        
        
        









