""""Home Page Test Module"""
import allure
from allure_commons.types import AttachmentType

from Config.config import TestData
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest


# pylint: disable=W0201

@allure.severity(allure.severity_level.MINOR)
class TestTemp(BaseTest):
    """"Home Page Test Class"""

    @allure.severity(allure.severity_level.MINOR)
    def driver(self, driver):
        """""driver method"""
        self.driver = driver

    @allure.severity(allure.severity_level.MINOR)
    def test_home_page_title(self):
        """"To test get home page title"""
        self.login_page = LoginPage(self.driver)
        homepage = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    @allure.severity(allure.severity_level.MINOR)
    def test_home_page_header(self):
        """"To test get the header value"""
        self.login_page = LoginPage(self.driver)
        homepage = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homepage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER
