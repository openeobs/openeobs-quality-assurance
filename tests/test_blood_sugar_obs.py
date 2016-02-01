"""Test to ensure that the Blood Sugar ob works correctly"""

from openeobs_mobile.data import BLOOD_SUGAR_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.TaskPageLocators import *
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.PatientPageLocators import *

class TestBloodSugarObsPage(TestCommon):
    """
    Setup a session and test that a blood sugar observation can be submitted
    """
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_blood_sugar_obs(self):
        """
        Test that a blood sugar observation can be submitted
        """
        blood_sugar_input = BLOOD_SUGAR_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(
            open_obs_menu_blood_sugar)
        PatientPage(self.driver).enter_obs_data(blood_sugar_input)

        success = 'Successfully Submitted Blood Sugar Observation'
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                successful_submit))
        )
        response = self.driver.find_element(*successful_submit)
        self.assertEqual(success,
                         response.text, 'Blood sugar observation unsuccessful')
