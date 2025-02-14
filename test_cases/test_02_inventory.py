from pages.inventory_page import InventoryPage
import logging


def test_add_items_to_cart(driver):
    # Initialize the InventoryPage object with the provided WebDriver instance
    inventory_page = InventoryPage(driver)
    logging.info(f"setting sorting from low to high")


    inventory_page.sort_low_to_high()
    
    logging.info(f"entering items to cart from inventory page")
    inventory_page.add_items_to_cart()

    logging.info(f"checking if cart value is equal to 2")
    assert inventory_page.get_cart_count() == 2
    logging.info("cart value check successful")

    logging.info(f"clicking on the product page")
    inventory_page.go_to_product_page()

    logging.info(f"adding the item to cart from the product page")
    inventory_page.add_items_from_product_page()


    logging.info(f"checking if the cart value is equal to 3")
    assert inventory_page.get_cart_count() == 3

    logging.info("clicking the cart icon to go to the cart page")
    inventory_page.clicking_cart_icon()

