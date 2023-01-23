"""Base Page Module."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    """ "Base Page Class"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """ "Click Function"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).click()

    def role_select(self, by_locator):
        """ "Select Function"""
        select = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
        )
        return select.select_by_index(2)

    def do_send_keys(self, by_locator, text):
        """ "To send Keys Function"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text)

    def get_url(self, url):
        """ "To get Url Function"""
        WebDriverWait(self.driver, 10).until(EC.title_is(url))
        return self.driver.current_url

    def get_element_text(self, by_locator):
        """ "To get text Function"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def is_visible(self, by_locator):
        """ "To check element is visible or not"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def get_title(self, title):
        """ "To get title of webpage"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    @staticmethod
    def down_scroll(driver):
        """ "To scroll down"""
        driver.execute_script("window   .scrollTo(0,document.body.scrollHeight)")

    @staticmethod
    def up_scroll(driver):
        """ "To scroll up"""
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    def dropdown_exe(self, by_locator, driver):
        """ "Dropdown functionality"""
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        driver.execute_script("arguments[0].click();", button)

    def page_select(self, by_locator):
        """ "To select the page size"""
        select = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
        )
        return select.select_by_index(1)

    def do_clear(self, by_locator):
        """ "To clear the text"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).clear()

    def switch_page(self, by_locator, driver):
        """ "To switch the page"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def select_category(self, by_locator):
        """ "To select the category"""
        select = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
        )
        return select.select_by_index(2)

    def select_technology(self, by_locator):
        """ "To select the technology"""
        select = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
        )
        return select.select_by_index(2)

    def select_course_type(self, by_locator):
        """ "To select the course type"""
        select = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
        )
        return select.select_by_index(1)