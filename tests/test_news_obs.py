"""Test to ensure that a no risk NEWS obs works correctly"""
from openeobs_mobile.data import NO_RISK_EWS_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.locators import TaskPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.PatientPageLocators import *


class TestNewsPage(TestCommon):
    """
    Setup a session and test that a no risk NEWS observation
    can be submitted
    """
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_news_obs(self):
        """
        Test that a NEWS observation can be submitted
        """
        score = NO_RISK_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(TaskPageLocators.confirm_submit)
        )
        self.driver.find_element(*TaskPageLocators.confirm_submit).click()

        success = 'Successfully Submitted NEWS Observation'
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )
        response = self.driver.find_element(*
                                            TaskPageLocators.successful_submit)
        self.assertEqual(success, response.text,
                         'NEWS observation unsuccessful')
