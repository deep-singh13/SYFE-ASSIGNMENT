from pages.logout_page import LogoutPage
import logging
import time
def test_logging_out(driver):

    logout_page = LogoutPage(driver)
    
    logging.info("clicking the hamburger menu")
    time.sleep(2)
    logout_page.clicking_hamburger_menu()

    logging.info("clicking the logout button")
    time.sleep(2)
    logout_page.clicking_logout_button()

    logging.info("checking successful redirection")
    time.sleep(2)
    assert "https://www.saucedemo.com/" in driver.current_url
    
    logging.info("successfull redirection")
    time.sleep(2)


