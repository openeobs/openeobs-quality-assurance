"""Test to ensure that a Weight ob works correctly"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.data import WEIGHT_DATA
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_WEIGHT
from openeobs_mobile.task_page_locators import SUCCESSFUL_SUBMIT
from openeobs_selenium.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1
from tests.test_common import TestCommon


class TestWeightObsPage(TestCommon):
    """
    Setup a session and test that a weight observation can be submitted
    """

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_patient_list()

    def test_weight_obs(self):
        """
        Test that a weight observation can be submitted
        """
        weight_input = WEIGHT_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(OPEN_OBS_MENU_WEIGHT)
        PatientPage(self.driver).enter_obs_data(weight_input)

        success = 'Successfully Submitted Weight Observation'
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                SUCCESSFUL_SUBMIT))
        )

        response = self.driver.find_element(*SUCCESSFUL_SUBMIT)

        self.assertEqual(success, response.text,
                         'Weight observation unsuccessful')
