# tests/selenium_test.py
import pytest
from selenium.webdriver.common.by import By

from utils.driver_factory import DriverFactory
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    # Initialize WebDriver using the factory
    driver = DriverFactory.get_driver()
    yield driver  # This makes driver available for each test case
    driver.quit()  # Close the driver after the test is done

def test_valid_login(driver):
    login_page = MainPage(driver)

    driver.get("http://www.polymorph.nl/my-account")  # URL to your login page

    login_page.enter_username("test")
    login_page.enter_password("Test.1234")
    login_page.click_login()

    # Verify that login was successful (this could be a redirect or a page element appearing)
    assert "My Account" in driver.title  # Replace "Dashboard" with the expected page title


def test_invalid_login(driver):
    login_page = MainPage(driver)

    driver.get("http://www.polymorph.nl/my-account")  # URL to your login page

    login_page.enter_username("invaliduser")
    login_page.enter_password("wrongpassword")
    login_page.click_login()

    # Verify that an error message is displayed
    error_message = driver.find_element(By.CLASS_NAME, "user-registration-error")
    assert error_message.is_displayed()  # Check if error message is visible
