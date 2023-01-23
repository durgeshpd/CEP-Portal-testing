""""Home Page Test Module"""
from Config.config import TestData
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest

# pylint: disable=W0201


class TestHome(BaseTest):
    """"Home Page Test Class"""

    def driver(self, driver):
        """""driver method"""
        self.driver = driver

    def test_home_page_title(self):
        """"To test get home page title"""
        self.login_page = LoginPage(self.driver)
        homepage = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        """"To test get the header value"""
        self.login_page = LoginPage(self.driver)
        homepage = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homepage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_account_name(self):
        """"To test get the account name"""
        self.login_page = LoginPage(self.driver)
        homepage = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homepage.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_testing_icon(self):
        """"To test check setting icon is existed or not"""
        self.login_page = LoginPage(self.driver)
        homepage = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homepage.is_setting_icon_exist()

    def test_log_out(self):
        """"To test check log out functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.is_log_out()

    def test_click_profile(self):
        """"To test click profile"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_profile()

    def test_click_change_password(self):
        """"To test cancel the click profile option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_change_password()

    def test_profile_cancel(self):
        """"To test check click functionality of click password"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_profile_cancel()

    def test_click_home(self):
        """"To test check home button functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_home()

    def test_scroll_down(self):
        """"To test check scroll down functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.scroll_down()

    def test_scroll_up(self):
        """"To test check scroll up functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.scroll_up()

    def test_footer(self):
        """"To test click the footer link"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_footer()

    def test_change_password_same_op(self):
        """"To test check change password functionality with different old password"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.change_pass_same_op()

    def test_change_password_new_op(self):
        """"To test check change password functionality with same old password"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.change_pass_new_op()

    def test_change_password_diff_np(self):
        """"To test check change password functionality with different new password"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.change_pass_diff_np()

    def test_password_visibility(self):
        """"To test check password visibility functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.password_visibility()

    def test_password_cancel(self):
        """"To test check cancel button functionality" in change password"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_password_cancel()

    def test_click_course_in_sidebar(self):
        """To test click course option in sidebar"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_course_in_sidebar()

    def test_search_course(self):
        """"To test check search functionality in course"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_search_course()

    def test_cancel_course(self):
        """"To test check cancel button functionality in search option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_search_cancel()

    def test_click_page_size(self):
        """"To test click the page size"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_page_size()

    def test_select_page_size(self):
        """"To test select the page size"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.select_page_size()

    def test_click_refresh_button(self):
        """"To test refresh button functionality"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_refresh_button()

    def test_click_course_name(self):
        """"To test check click functionality of course name"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_course_name()

    def test_course_name_edit(self):
        """"To test edit the course name"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.course_name_edit()

    def test_click_add_question(self):
        """"To test check click functionality of add question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_add_question()

    def test_click_courses_add_questions(self):
        """"To test check click functionality courses in add question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_courses_in_add_question()

    def test_click_home_add_questions(self):
        """"To test check click functionality home button of add question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_home_in_add_question()

    def test_do_search_questions(self):
        """"To test check search functionality of question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_search_questions()

    def test_do_cancel_questions(self):
        """"To test cancel the click functionality of add question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_cancel_questions()

    def test_click_question(self):
        """"To test click the page size in question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_question()

    def test_click_activate_question(self):
        """"To test select the page size in question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_activate_question()

    def test_confirm_activate_question_true(self):
        """"To test refresh button functionality in question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.confirm_activate_question_true()

    def test_click_activate_question_false(self):
        """To test check click functionality of the question in add question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.cancel_activate_question_confirmation()

    def test_confirm_activate_question_false(self):
        """"To test check click functionality of the activate question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.confirm_activate_question_false()

    def test_click_delete_question(self):
        """To test click confirm option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_delete_question()

    def test_confirm_delete_question_true(self):
        """"To test click the close button"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.confirm_delete_question_true()

    def test_cancel_delete_question_confirmation(self):
        """"To test click status change in question activate"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.cancel_delete_question_confirmation()

    def test_confirm_delete_question_false(self):
        """"To test confirm the delete question option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.confirm_delete_question_false()

    def test_click_publish_course(self):
        """"To test close to delete question option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_publish_course()

    def test_confirm_publish_course_true(self):
        """"To test change the status to delete question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.confirm_publish_course_true()

    def test_cancel_publish_course_confirmation(self):
        """"To test cancel to publish question option"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.cancel_publish_course_confirmation()

    def test_confirm_publish_course_false(self):
        """"To test change the status the publishing question"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.confirm_publish_course_false()

    def test_click_page_link(self):
        """"To test check the click functionality of page link"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_page_link()

    def test_click_forward_page_link(self):
        """"To test check the click functionality of forward page link"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_forward_page_link()

    def test_click_backward_page_lnk(self):
        """"To test check the click functionality of backward page link"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_backward_page_link()

    def test_click_last_page_link(self):
        """"To test check the click functionality of last page link"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_last_page_link()

    def test_click_first_page_link(self):
        """"To test check the click functionality of first page link"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_first_page_link()

    def test_click_add_course(self):
        """"To test check the click functionality add course in course"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_add_course()

    def test_add_course(self):
        """"To test add the course"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.add_course()

    def test_click_cancel_button_in_add_course(self):
        """"To test check the cancel button functionality of added course"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_cancel_button_in_add_course()

    def test_click_evaluations_in_sidebar(self):
        """"To test check the click functionality of evaluations in sidebar"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_evaluations_in_sidebar()

    def test_do_search_evaluation(self):
        """"To test check the search functionality in evaluation"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_search_evaluation()

    def test_do_cancel_evaluation(self):
        """"To test check the cancel button functionality in evaluation"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_cancel_evaluation()

    def test_click_page_size_in_evaluation(self):
        """"To test check click functionality of page size in evaluation"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_page_size_in_evaluation()

    def test_select_page_size_in_evaluation(self):
        """"To test select page size in evaluation"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.select_page_size_in_evaluation()

    def test_click_refresh_button_in_evaluation(self):
        """"To test check click functionality of refresh button in evaluation"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_refresh_button_in_evaluation()

    def test_click_evaluated_courses_in_sidebar(self):
        """"To test check the click functionality of evaluated courses in sidebar"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_evaluated_courses_in_sidebar()

    def test_do_search_evaluated_courses(self):
        """"To test check the cancel button functionality in evaluated courses"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_search_evaluated_courses()

    def test_do_cancel_evaluated_courses(self):
        """"To test check click functionality of page size in evaluated courses"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.do_cancel_evaluated_courses()

    def test_click_page_size_in_evaluated_courses(self):
        """"To test check click functionality of page size in evaluated courses"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_page_size_in_evaluated_courses()

    def test_select_page_size_in_evaluated_courses(self):
        """"To test select page size in evaluated courses"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.select_page_size_in_evaluated_courses()

    def test_click_refresh_button_in_evaluated_courses(self):
        """"To test check click functionality of refresh button in evaluated courses"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.home_page = HomePage(self.driver)
        self.home_page.click_refresh_button_in_evaluated_courses()