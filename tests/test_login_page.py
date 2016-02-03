"""Test to ensure that the login page works correctly"""
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.page_confirm import PageConfirm
from tests.test_common import TestCommon
from tests.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1


class TestLoginPage(TestCommon):
    """
    Setup a session and test the login page
    """

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)

    def test_login_page_title(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.assertTrue(PageConfirm(self.driver).is_login_page(),
                        'Incorrect page title')

    def test_successful_login(self):
        """
        Test that can log into the app with correct credentials
        """

        self.login_page.login(NURSE_USERNM1,
                              NURSE_PWD1)
        self.assertTrue(self.login_page.has_logged_in(), 'Unable to log in')

    def test_error_message_login(self):
        """
        Test that the login page shows an error on trying to login with
        incorrect credentials
        """
        self.login_page.login('invalid_credentials', 'invalid_credentials')
        self.assertTrue(self.login_page.shows_login_error(),
                        'Does not show the error message')
