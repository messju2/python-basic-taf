# conftest.py
import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    # Setup WebDriver instance
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()  # Clean up after test completion