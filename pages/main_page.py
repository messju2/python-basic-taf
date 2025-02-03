from selenium.webdriver.common.by import By
from taf.test_drivers.facade import Facade


class MainPage(Facade):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")

    def enter_username(self, username):
        self.send_keys(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)
