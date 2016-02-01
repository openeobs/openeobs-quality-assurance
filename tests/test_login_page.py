"""Test to ensure that the login page works correctly"""

from openeobs_mobile.login_page import LoginPage
from tests.test_common import TestCommon


class TestLoginPage(TestCommon):
    """
    Setup a session and test the login page
    """
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)

    def test_login_page_title(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.assertTrue(self.login_page.is_login_page(),
                        'Incorrect page title')

    def test_correct_credentials(self):
        """
        Test that can log into the app with correct credentials
        """
        self.login_page.login('nasir', 'nasir')
        self.assertTrue(self.login_page.has_logged_in(), 'Unable to log in')

    def test_error_incorrect_credentials(self):
        """
        Test that the login page shows an error on trying to login without
        correct credentials
        """
        self.login_page.login('invalid_credentials', 'invalid_credentials')
        self.assertTrue(self.login_page.shows_login_error(),
                        'Does not show the error message')
