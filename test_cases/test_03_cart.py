from pages.cart_page import CartPage
import logging

def test_remove_items_between_range(driver):
    cart_page = CartPage(driver)
    logging.info(f"remove the item between the range of 8 to 10 dollars from the cart")
    cart_page.remove_item_from_cart()
    logging.info(f"checking if new cart value is equal to 2")
    assert cart_page.check_cart_count() == 2

    logging.info("clicking the checkout button")
    cart_page.clicking_checkout_button()