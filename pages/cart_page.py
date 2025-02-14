from pages.base_page import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage(base_page):
    #locators for cart elements
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_COUNT = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    REMOVE = (By.XPATH, ".//button[contains(text(),'Remove')]")
    CHECKOUT_BUTTON = (By.XPATH , '//*[@id="checkout"]')

    #function for removing items which come under a certain price range
    def remove_item_from_cart(self):

        items_in_cart = self.driver.find_elements(*self.CART_ITEM) #getting all cart items

        for item in items_in_cart:
            # Get the price of the item and convert it to float
            item_price = item.find_element(*self.CART_ITEM_PRICE).text
            price_value = float(item_price.replace("$", "").strip())

            #checking if price is within the valid range
            if 8 <= price_value <= 10:
                time.sleep(2)

                # Get the item name, format it to match the button's data-test attribute
                item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text.lower().replace(" ", "-")
                remove_button_xpath = f"//button[@data-test='remove-{item_name}']"
                time.sleep(2)
                    

                # Wait until the remove button is clickable and then click it
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
    
