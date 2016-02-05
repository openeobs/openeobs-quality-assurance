"""Test to ensure that error handling works correctly"""
from openeobs_mobile.data import INCORRECT_EWS_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.menu_locators import SERVER_ERROR
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.task_page_locators import TASK_FORM_INVALID_SUBMIT
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_NEWS_ITEM
from tests.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1


class TestErrorHandling(TestCommon):
    """
    Setup a session and test that e-Obs error handling works
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_patient_list()

    def test_news_error(self):
        """
        Test that entering incorrect data into a NEWS ob will cause an error
        """
        incorrect_score = INCORRECT_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(OPEN_OBS_MENU_NEWS_ITEM)
        PatientPage(self.driver).enter_obs_data(incorrect_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(TASK_FORM_INVALID_SUBMIT)
        )

        response = self.driver.find_element(
            *TASK_FORM_INVALID_SUBMIT).is_displayed()

        self.assertEqual(response, True,
                         'Incorrect error handling on NEWS form')

    def test_barcode_error(self):
        """
        Test that entering incorrect data into a barcode scan will
        cause an error
        """
        no_patient_id = self.patient_list_page.patient_scan_helper(99)
        self.patient_list_page.do_barcode_scan(
            no_patient_id['other_identifier'])

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(SERVER_ERROR)
        )

        response = self.driver.find_element(
            *SERVER_ERROR).is_displayed()

        self.assertEqual(response, True,
                         'Incorrect error handling on barcode scan')
