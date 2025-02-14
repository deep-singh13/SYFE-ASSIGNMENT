from pages.checkout_page import CheckoutPage
import logging
import time

def test_checkout(driver):
    checkout_page= CheckoutPage(driver)
    logging.info("entering the checkout details")
    checkout_page.checkout_process("Deepinder", "Singh", 121003)

    logging.info("retrieving the total amount")
    total_amount = checkout_page.getting_total_amount()
    assert total_amount > 0 #checking if the total amount is greater than 0

    logging.info(f"total amount is {total_amount}") #logging the total amount in terminal
    time.sleep(2)

    logging.info(f"clicking the finish button")
    checkout_page.clicking_finish() 

    logging.info("checking if the final success message is displayed")
    time.sleep(2)
    
    assert checkout_page.checking_success_message() == "Thank you for your order!" #checking if success message is valid
    logging.info("final success message verified successfully")

    

