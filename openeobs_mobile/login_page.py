"""Methods for the login page"""

from openeobs_mobile.page_helpers import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from openeobs_mobile.LoginPageLocators import *

class LoginPage(BasePage):
    """
    Login Page methods and helps etc
    """

    def login(self, username, password,
              database='openeobs_quality_assurance_db'):
        """
        Fill out the login form and press the submit button
        :param username: Username to login with
        :param password: Password for the username supplied
        """
        username_e = self.driver.find_element(*username_el)
        password_e = self.driver.find_element(*password_el)
        login_button = self.driver.find_element(*login_button_el)
        try:
            database_selector = self.driver.find_element(
                *database_dropdown_el
            )
            Select(database_selector).select_by_value(database)
        except NoSuchElementException:
            pass

        username_e.send_keys(username)
        password_e.send_keys(password)
        login_button.click()

    def has_logged_in(self):
        """
        Check that the current page is the task list (which is the screen seen
        on logging in
        :return: Boolean of if on the task list
        """
        return '/mobile/tasks/' in self.driver.current_url

    def shows_login_error(self):
        """
        Check that the login page shows an error message
        :return: Boolean of if the error message is shown
        """
        error_e = self.driver.find_element(*error_el)
        return error_e.text == 'Invalid username/password'

    def show_dropdown_for_databases(self):
        """
        Check that the login page shows the dropdown for multiple databases
        :return: Boolean of if the drop down is present
        """
        try:
            self.driver.find_element(*database_dropdown_el)
        except NoSuchElementException:
            return False
        return True
