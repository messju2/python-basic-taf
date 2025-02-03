# utils/driver_factory.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
#            options.add_argument("--headless")  # Optional: run headless (without browser window)
            options.add_argument("--disable-gpu")
            options.binary_location = ".//drivers/chromedriver"
            driver = webdriver.Chrome()

        else:
            raise Exception(f"Browser {browser} not supported!")

        driver.maximize_window()
        return driver