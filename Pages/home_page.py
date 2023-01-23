""""Home Page Module"""
import time
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Utility.logger import LogGen


class HomePage(BasePage, LogGen):
    """"Home Page Class"""

    Header = (By.XPATH, "//a[normalize-space()='Candidate Evaluation Portal']")
    Account_Name = (By.XPATH, "//span[@class='d-none d-sm-none d-lg-block']")
    Setting_Icon = (By.XPATH, "//i[@class='nc-icon nc-settings-gear-65 font-size-20 mr-1']")
    Log_Out = (By.XPATH, "//a[normalize-space()='Sign Out']")
    Profile = (By.XPATH, "//a[normalize-space()='Profile']")
    Change_Password = (By.XPATH, "//a[normalize-space()='Change Password']")
    Home = (By.XPATH, "//span[normalize-space()='Home']")
    Footer = (By.XPATH, "//a[normalize-space()='SpanIdea']")
    Course = (By.XPATH, "//p[normalize-space()='Courses']")
    Old_Password = (By.XPATH, "//input[@placeholder='Old Password']")
    New_Password = (By.XPATH, "//input[@placeholder='New Password']")
    Password_Again = (By.XPATH, "//input[@placeholder='Password Again']")
    Submit = (By.XPATH, "//button[normalize-space()='Submit']")
    Old_Password_Visible = (By.XPATH, "//div[@class='card card-user']//div[1]//div[1]//div[1]//div[1]//span[1]//i[1]")
    New_Password_Visible = (By.XPATH, "/html/body/app-root/app-admin-layout/div/div[2]/di"
                                      "v/app-change-password/div/div/div/div/div[2]/form/div[2]/div/div/div/span/i")
    Password_Again_Visible = (By.XPATH, "/html/body/app-root/app-admin-layout/div/div[2]/div/app-ch"
                                        "ange-password/div/div/div/div/div[2]/form/div[3]/div/div/div/span/i")
    Cancel = (By.XPATH, "//button[normalize-space()='Cancel']")
    Search_Course = (By.XPATH, "//input[@placeholder='Search Course']")
    Search_Button = (By.XPATH, "//button[@class='btn btn-primary ml-2']")
    Cancel_Button = (By.XPATH, "//button[@class='btn btn-danger ml-2']")
    Page_Size = (By.XPATH, "//select[@id='select-page-size']")
    Refresh_Button = (By.XPATH, "//button[@title='Refresh']")
    Course_Name = (By.XPATH, "//a[normalize-space()='Python_coding']")
    Course_Name_Edit = (By.XPATH, "//input[@id='coursename']")
    Add_Question = (By.XPATH, "//tbody/tr[3]/td[7]/a[1]/i[1]")
    Course_Page = (By.XPATH, "//span[normalize-space()='Courses']")
    Search_Question = (By.XPATH, "//input[@placeholder='Search Question']")
    Question = (By.XPATH, "//a[normalize-space()='Python']")
    Question_Activate = (By.XPATH, "//body[1]/app-root[1]/app-admin-layout[1]/div[1]/div[2]/div[1]/app-supervisor-quest"
                                   "ion-listing[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]"
                                   "/tbody[1]/"
                                   "tr[2]/td[5]/a[1]/i[1]")
    Status_Confirm = (By.XPATH, "//div[@id='activeStatusModal']//button[@type='button'][normalize-space()='Confirm']")
    Close_Button = (By.XPATH, "//div[@id='activeStatusModal']//button[@type='button'][normalize-space()='Close']")
    Delete_Question = (By.XPATH, "//tbody/tr[1]/td[6]/a[1]/i[1]")
    Confirm_Delete = (By.XPATH, "//div[@id='deleteModal']//button[@type='button'][normalize-space()='Confirm']")
    Close_Delete = (By.XPATH, "//div[@id='deleteModal']//button[@type='button'][normalize-space()='Close']")
    Publish_Course = (By.XPATH, "//body[1]/app-root[1]/app-admin-layout[1]/div[1]/div[2]/div[1]/app-su"
                                "pervisor-courses-listing[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div"
                                "[1]/table[1]/tbody[1]/tr[1]/td[10]/a[1]/i[1]")
    Confirm_Publish = (By.XPATH, "//div[@class='card-content']//button[@type='button'][normalize-space()='Confirm']")
    Close_Publish = (By.XPATH, "//div[@class='card-content']//button[@type='button'][normalize-space()='Close']")
    Page_Link = (By.XPATH, "//a[normalize-space()='2']")
    Forward_Page_Link = (By.XPATH, "//span[normalize-space()='>']")
    Backward_Page_Link = (By.XPATH, "//span[normalize-space()='<']")
    Last_Page_Link = (By.XPATH, "//span[normalize-space()='>>']")
    First_Page_Link = (By.XPATH, "//span[normalize-space()='<<']")
    Add_Course = (By.XPATH, "//button[normalize-space()='Add Course']")
    Select_Category = (By.XPATH, "//select[@id='categoryId']")
    Select_Technology = (By.XPATH, "//select[@id='technologyId']")
    Select_Course_Type = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    Add_Course_Name = (By.CSS_SELECTOR, "#coursename")
    Add_Course_Time = (By.CSS_SELECTOR, "#Coursename")
    Evaluation = (By.XPATH, "//p[normalize-space()='Evaluations']")
    Search_Evaluations = (By.CSS_SELECTOR, "input[placeholder='Search Evaluations']")
    Evaluated_Courses = (By.XPATH, "//p[normalize-space()='Evaluated Courses']")
    Search_Evaluated_Courses = (By.CSS_SELECTOR, "input[placeholder='Search Evaluated Courses']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        """"To get home page title"""
        global log
        log = self.loggen()
        log.info("Running home page 1st testcase")
        log.info("Testing the home page title")
        return self.get_title(title)

    def get_header_value(self):
        """"To get the header value"""
        log.info("Running home page 2nd testcase")
        log.info("Testing the home page header")
        if self.is_visible(self.Header):
            return self.get_element_text(self.Header)

    def get_account_name_value(self):
        """"To get the account name"""
        log.info("Running home page 3rd testcase")
        log.info("Testing the account name")
        if self.is_visible(self.Account_Name):
            return self.get_element_text(self.Account_Name)

    def is_setting_icon_exist(self):
        """"To check setting icon is existed or not"""
        log.info("Running home page 4th testcase")
        log.info("Testing to check setting icon exist or not")
        return self.is_visible(self.Setting_Icon)

    def is_log_out(self):
        """"To check log out functionality"""
        log.info("Running home page 5th testcase")
        log.info("Testing the log out functionality")
        self.do_click(self.Account_Name)
        self.do_click(self.Log_Out)
        time.sleep(2)

    def click_profile(self):
        """"To click profile"""
        log.info("Running home page 6th testcase")
        log.info("Testing the click functionality of profile")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Profile, self.driver)
        time.sleep(2)

    def click_profile_cancel(self):
        """"To cancel the click profile option"""
        log.info("Running home page 7th testcase")
        log.info("Testing the click functionality of cancel button of profile")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Profile, self.driver)
        time.sleep(2)
        self.do_click(self.Cancel)

    def click_change_password(self):
        """"To check click functionality of click password"""
        log.info("Running home page 8th testcase")
        log.info("Testing the click functionality of change password")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Change_Password, self.driver)
        time.sleep(2)

    def click_home(self):
        """"To check home button functionality"""
        log.info("Running home page 9th testcase")
        log.info("Testing the click functionality of home button")
        self.do_click(self.Course)
        time.sleep(2)
        self.do_click(self.Home)
        time.sleep(2)

    def scroll_down(self):
        """"To check scroll down functionality"""
        log.info("Running home page 10th testcase")
        log.info("Testing the click functionality of scroll down")
        self.down_scroll(self.driver)
        time.sleep(2)

    def scroll_up(self):
        """"To check scroll up functionality"""
        log.info("Running home page 11th testcase")
        log.info("Testing the click functionality of scroll up")
        self.down_scroll(self.driver)
        time.sleep(2)
        self.up_scroll(self.driver)
        time.sleep(2)

    def click_footer(self):
        """"To click the footer link"""
        log.info("Running home page 12th testcase")
        log.info("Testing the click functionality of footer link")
        self.down_scroll(self.driver)
        time.sleep(2)
        self.do_click(self.Footer)
        time.sleep(2)
        self.switch_page(self.Footer, self.driver)
        time.sleep(2)

    def change_pass_new_op(self):
        """"To check change password functionality with different old password"""
        log.info("Running home page 13th testcase")
        log.info("Testing the functionality of change password with different old password")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Change_Password, self.driver)
        self.do_send_keys(self.Old_Password, "test")
        self.do_send_keys(self.New_Password, "test")
        self.do_send_keys(self.Password_Again, "test")
        self.do_click(self.Submit)
        time.sleep(2)

    def change_pass_same_op(self):
        """"To check change password functionality with same old password"""
        log.info("Running home page 14th testcase")
        log.info("Testing the functionality of change password with same old password")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Change_Password, self.driver)
        self.do_send_keys(self.Old_Password, "test")
        self.do_send_keys(self.New_Password, "test")
        self.do_send_keys(self.Password_Again, "test")
        self.do_click(self.Submit)
        time.sleep(2)

    def change_pass_diff_np(self):
        """"To check change password functionality with different new password"""
        log.info("Running home page 15th testcase")
        log.info("Testing the functionality of change password with different new password")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Change_Password, self.driver)
        self.do_send_keys(self.Old_Password, "test")
        self.do_send_keys(self.New_Password, "tes")
        self.do_send_keys(self.Password_Again, "test")
        self.do_click(self.Submit)
        time.sleep(2)

    def password_visibility(self):
        """"To check password visibility functionality"""
        self.do_click(self.Setting_Icon)
        log.info("Running home page 16th testcase")
        log.info("Testing the functionality of password visibility")
        self.dropdown_exe(self.Change_Password, self.driver)
        self.do_send_keys(self.Old_Password, "test")
        self.do_send_keys(self.New_Password, "test")
        self.do_send_keys(self.Password_Again, "test")
        self.do_click(self.Old_Password_Visible)
        time.sleep(2)
        self.do_click(self.New_Password_Visible)
        time.sleep(2)
        self.do_click(self.Password_Again_Visible)
        time.sleep(2)

    def click_password_cancel(self):
        """"To check cancel button functionality" in change password"""
        log.info("Running home page 17th testcase")
        log.info("Testing the click functionality of cancel button in change password")
        self.do_click(self.Setting_Icon)
        self.dropdown_exe(self.Change_Password, self.driver)
        self.do_send_keys(self.Old_Password, "test")
        self.do_send_keys(self.New_Password, "test")
        self.do_send_keys(self.Password_Again, "test")
        self.do_click(self.Cancel)
        time.sleep(2)

    def click_course_in_sidebar(self):
        """To click course option in sidebar"""
        log.info("Running home page 18th testcase")
        log.info("Testing the click functionality of course in sidebar")
        self.do_click(self.Course)
        time.sleep(2)

    def do_search_course(self):
        """"To check search functionality in course"""
        self.do_click(self.Course)
        self.do_send_keys(self.Search_Course, "python")
        self.do_click(self.Search_Button)
        time.sleep(2)

    def do_search_cancel(self):
        """"To check cancel button functionality in search option"""
        self.do_click(self.Course)
        self.do_send_keys(self.Search_Course, "python")
        time.sleep(2)
        self.do_click(self.Cancel_Button)
        time.sleep(2)

    def click_page_size(self):
        """"To click the page size"""
        self.do_click(self.Course)
        self.do_click(self.Page_Size)
        time.sleep(2)

    def select_page_size(self):
        """"To select the page size"""
        self.do_click(self.Course)
        self.page_select(self.Page_Size)
        time.sleep(2)

    def click_refresh_button(self):
        """"To refresh button functionality"""
        self.do_click(self.Course)
        self.do_click(self.Refresh_Button)
        time.sleep(2)

    def click_course_name(self):
        """"To check click functionality of course name"""
        self.do_click(self.Course)
        self.do_click(self.Course_Name)
        time.sleep(2)

    def course_name_edit(self):
        """"To edit the course name"""
        self.do_click(self.Course)
        self.do_click(self.Course_Name)
        self.do_clear(self.Course_Name_Edit)
        time.sleep(2)
        self.do_send_keys(self.Course_Name_Edit, "Python")
        self.do_click(self.Submit)
        time.sleep(2)

    def click_add_question(self):
        """"To check click functionality of add question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)

    def click_courses_in_add_question(self):
        """"To check click functionality courses in add question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Course_Page)
        time.sleep(2)

    def click_home_in_add_question(self):
        """"To check click functionality home button of add question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Home)
        time.sleep(2)

    def do_search_questions(self):
        """"To check search functionality of question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_send_keys(self.Search_Question, "What Is Constructor")
        self.do_click(self.Search_Button)
        time.sleep(2)

    def do_cancel_questions(self):
        """"To cancel the click functionality of add question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_send_keys(self.Search_Question, "What Is Constructor")
        self.do_click(self.Cancel_Button)
        time.sleep(2)

    def click_page_size_in_question(self):
        """"To click the page size in question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Page_Size)
        time.sleep(2)

    def select_page_size_in_question(self):
        """"To select the page size in question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.page_select(self.Page_Size)
        time.sleep(2)

    def click_refresh_button_in_question(self):
        """"To refresh button functionality in question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Refresh_Button)
        time.sleep(2)

    def click_question(self):
        """"To check click functionality of the question in add question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Question)
        time.sleep(2)

    def click_activate_question(self):
        """"To check click functionality of the activate question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Question_Activate)
        time.sleep(2)

    def confirm_activate_question_true(self):
        """"To click confirm option"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Question_Activate)
        time.sleep(2)
        self.do_click(self.Status_Confirm)
        time.sleep(2)

    def cancel_activate_question_confirmation(self):
        """"To click the close button"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Question_Activate)
        time.sleep(2)
        self.do_click(self.Close_Button)
        time.sleep(2)

    def confirm_activate_question_false(self):
        """"To click status change in question activate"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.do_click(self.Question_Activate)
        time.sleep(2)
        self.do_click(self.Status_Confirm)
        time.sleep(2)

    def click_delete_question(self):
        """"To check click functionality of delete question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        time.sleep(2)
        self.page_select(self.Page_Size)
        self.do_click(self.Delete_Question)
        time.sleep(2)

    def confirm_delete_question_true(self):
        """"To confirm the delete question option"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        self.page_select(self.Page_Size)
        time.sleep(2)
        self.do_click(self.Delete_Question)
        time.sleep(2)
        self.do_click(self.Confirm_Delete)
        time.sleep(2)

    def cancel_delete_question_confirmation(self):
        """"To close to delete question option"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        self.page_select(self.Page_Size)
        time.sleep(2)
        self.do_click(self.Delete_Question)
        time.sleep(2)
        self.do_click(self.Close_Delete)
        time.sleep(2)

    def confirm_delete_question_false(self):
        """"To change the status to delete question"""
        self.do_click(self.Course)
        self.do_click(self.Add_Question)
        self.page_select(self.Page_Size)
        time.sleep(2)
        self.do_click(self.Delete_Question)
        time.sleep(2)
        self.do_click(self.Confirm_Delete)
        time.sleep(2)

    def click_publish_course(self):
        """"To check the click functionality of publish course"""
        self.do_click(self.Course)
        self.do_click(self.Publish_Course)
        time.sleep(2)

    def confirm_publish_course_true(self):
        """"To confirm to publish question option"""
        self.do_click(self.Course)
        self.do_click(self.Publish_Course)
        time.sleep(2)
        self.do_click(self.Confirm_Publish)
        time.sleep(2)

    def cancel_publish_course_confirmation(self):
        """"To cancel to publish question option"""
        self.do_click(self.Course)
        self.do_click(self.Publish_Course)
        time.sleep(2)
        self.do_click(self.Close_Publish)
        time.sleep(2)

    def confirm_publish_course_false(self):
        """"To change the status the publishing question"""
        self.do_click(self.Course)
        self.do_click(self.Publish_Course)
        time.sleep(2)
        self.do_click(self.Confirm_Publish)
        time.sleep(2)

    def click_page_link(self):
        """"To check the click functionality of page link"""
        self.do_click(self.Course)
        self.do_click(self.Page_Link)
        time.sleep(2)

    def click_forward_page_link(self):
        """"To check the click functionality of forward page link"""
        self.do_click(self.Course)
        self.do_click(self.Forward_Page_Link)
        time.sleep(2)

    def click_backward_page_link(self):
        """"To check the click functionality of backward page link"""
        self.do_click(self.Course)
        self.do_click(self.Forward_Page_Link)
        time.sleep(2)
        self.do_click(self.Backward_Page_Link)
        time.sleep(4)

    def click_last_page_link(self):
        """"To check the click functionality of last page link"""
        self.do_click(self.Course)
        self.do_click(self.Last_Page_Link)
        time.sleep(2)

    def click_first_page_link(self):
        """"To check the click functionality of first page link"""
        self.do_click(self.Course)
        self.do_click(self.Last_Page_Link)
        time.sleep(2)
        self.do_click(self.First_Page_Link)
        time.sleep(2)

    def click_add_course(self):
        """"To check the click functionality add course in course"""
        self.do_click(self.Course)
        self.do_click(self.Add_Course)
        time.sleep(2)

    def add_course(self):
        """"To add the course"""
        self.do_click(self.Course)
        self.do_click(self.Add_Course)
        time.sleep(2)
        self.select_category(self.Select_Category)
        time.sleep(2)
        self.select_category(self.Select_Technology)
        time.sleep(2)
        self.select_category(self.Select_Course_Type)
        time.sleep(2)
        self.do_send_keys(self.Add_Course_Name, "Selenium with Pytest")
        time.sleep(2)
        self.do_send_keys(self.Add_Course_Time, "02:00:00")
        time.sleep(2)
        self.do_click(self.Submit)
        time.sleep(2)

    def click_cancel_button_in_add_course(self):
        """"To check the cancel button functionality of added course"""
        self.do_click(self.Course)
        self.do_click(self.Add_Course)
        time.sleep(2)
        self.select_category(self.Select_Category)
        time.sleep(2)
        self.select_category(self.Select_Technology)
        time.sleep(2)
        self.do_click(self.Cancel)
        time.sleep(2)

    def click_evaluations_in_sidebar(self):
        """"To check the click functionality of evaluations in sidebar"""
        self.do_click(self.Evaluation)
        time.sleep(2)

    def do_search_evaluation(self):
        """"To check the search functionality in evaluation"""
        self.do_click(self.Evaluation)
        self.do_send_keys(self.Search_Evaluations, "Python")
        self.do_click(self.Search_Button)
        time.sleep(2)

    def do_cancel_evaluation(self):
        """"To check the cancel button functionality in evaluation"""
        self.do_click(self.Evaluation)
        self.do_send_keys(self.Search_Evaluations, "Python")
        time.sleep(2)
        self.do_click(self.Cancel_Button)
        time.sleep(2)

    def click_page_size_in_evaluation(self):
        """"To check click functionality of page size in evaluation"""
        self.do_click(self.Evaluation)
        self.do_click(self.Page_Size)
        time.sleep(2)

    def select_page_size_in_evaluation(self):
        """"To select page size in evaluation"""
        self.do_click(self.Evaluation)
        self.page_select(self.Page_Size)
        time.sleep(2)

    def click_refresh_button_in_evaluation(self):
        """"To check click functionality of refresh button in evaluation"""
        self.do_click(self.Evaluation)
        self.do_click(self.Refresh_Button)
        time.sleep(2)

    def click_evaluated_courses_in_sidebar(self):
        """"To check the click functionality of evaluated courses in sidebar"""
        self.do_click(self.Evaluated_Courses)
        time.sleep(2)

    def do_search_evaluated_courses(self):
        """"To check the search functionality in evaluated courses"""
        self.do_click(self.Evaluated_Courses)
        self.do_send_keys(self.Search_Evaluated_Courses, "Python")
        self.do_click(self.Search_Button)
        time.sleep(2)

    def do_cancel_evaluated_courses(self):
        """"To check the cancel button functionality in evaluated courses"""
        self.do_click(self.Evaluated_Courses)
        self.do_send_keys(self.Search_Evaluated_Courses, "Python")
        time.sleep(2)
        self.do_click(self.Cancel_Button)
        time.sleep(2)

    def click_page_size_in_evaluated_courses(self):
        """"To check click functionality of page size in evaluated courses"""
        self.do_click(self.Evaluated_Courses)
        self.do_click(self.Page_Size)
        time.sleep(2)

    def select_page_size_in_evaluated_courses(self):
        """"To select page size in evaluated courses"""
        self.do_click(self.Evaluated_Courses)
        self.page_select(self.Page_Size)
        time.sleep(2)

    def click_refresh_button_in_evaluated_courses(self):
        """"To check click functionality of refresh button in evaluated courses"""
        self.do_click(self.Evaluated_Courses)
        self.do_click(self.Refresh_Button)
        time.sleep(2)