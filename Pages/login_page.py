""""Login page Module"""
import time
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.base_page import BasePage
from Pages.home_page import HomePage


class LoginPage(BasePage):
    """"This is login Page class"""

    ROLE = By.ID, "exampleFormControlSelect1"
    EMAIL = By.XPATH, "//input[@placeholder='Username']"
    PASSWORD = By.XPATH, "//input[@placeholder='Password']"
    LOGIN_BUTTON = By.XPATH, "//button[normalize-space()='Login']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        """"To login page title"""
        return self.get_title(title)

    def do_login(self, username, password):
        """"To log in"""
        self.do_click(self.ROLE)
        self.role_select(self.ROLE)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(2)
        return HomePage(self.driver)
    