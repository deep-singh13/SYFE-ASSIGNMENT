from pages.base_page import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage(base_page):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    #CART_BUTTON = (By.XPATH , '//*[@id="shopping_cart_container"]/a')
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_COUNT = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    REMOVE = (By.XPATH, ".//button[contains(text(),'Remove')]")
    CHECKOUT_BUTTON = (By.XPATH , '//*[@id="checkout"]')

    def remove_item_from_cart(self):
        #self.click(self.CART_BUTTON)
        items_in_cart = self.driver.find_elements(*self.CART_ITEM)

        for item in items_in_cart:
            item_price = item.find_element(*self.CART_ITEM_PRICE).text
            price_value = float(item_price.replace("$", "").strip())

            if 8 <= price_value <= 10:
                time.sleep(2)
                item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.lower().replace(" ", "-")
                remove_button_xpath = f"//button[@data-test='remove-{item_name}']"
                time.sleep(2)
                    


                remove_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, remove_button_xpath))
                 )

                remove_button.click()
                time.sleep(2)
                break
                
    
    
    def check_cart_count(self):
        return int(self.get_text(self.CART_COUNT))


    def clicking_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)
    
