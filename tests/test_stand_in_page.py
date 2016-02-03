"""Test to ensure that the stand in page works correctly"""
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.stand_in_page import StandInPage
from tests.test_common import TestCommon
from tests.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1


class TestStandInPage(TestCommon):
    """
    Setup a session and test the standin page
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_standin()

    def test_stand_in(self):
        """
        Test that the stand-in function works
        """
        nurse_name = StandInPage(self.driver).submit_stand_in()

        nurse = nurse_name.split(' ', 1)[0].lower()
        response = StandInPage(self.driver).confirm_stand_in(
            nurse, self.patient_list_page)

        success = 'Successfully accepted stand-in invite'
        self.assertEqual(success, response.text, 'Stand in was unsuccessful')
