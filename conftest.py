import pytest
from selenium import webdriver
import logging
import pytest
import time


# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Print logs to terminal
    ]
)

@pytest.fixture(scope="session")
def driver():
    logging.info("Initializing Chrome WebDriver.")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)
    yield driver
    driver.quit()
    