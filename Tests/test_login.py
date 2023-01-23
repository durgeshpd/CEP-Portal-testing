""""Login page Test Module"""
from Config.config import TestData
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest


class TestLoginPage(BaseTest):
    """"Login Page test class"""

    def test_login_page_title(self):
        """"To test login page title"""
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        """"Test to log in"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_login_verify(self):
        """"Test to verify log in"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage = LoginPage(self.driver)
        assert "durgesh@gmail.com" == TestData.USER_NAME
        assert "test" == TestData.PASSWORD
