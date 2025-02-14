from pages.login_page import LoginPage
import logging
#task 1 login validation
def test_invalid_login(driver):  
    login_page = LoginPage(driver)
    logging.info("entering invalid username")
    login_page.login("invalid_user", "wrong_password")
    #checking if error message as expected
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message().strip()

    logging.info("entering valid username")
    login_page.login("standard_user", "secret_sauce")
    #checking successful redirection to the inventory page
    assert "/inventory.html" in driver.current_url


       

