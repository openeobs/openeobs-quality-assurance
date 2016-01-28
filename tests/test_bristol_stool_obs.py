"""Test to ensure Bristol Stool Scale ob works correctly"""

from openeobs_mobile.data import BRISTOL_STOOL_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.locators import PatientPageLocators, TaskPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


class TestBristolStoolObsPage(TestCommon):
    """
    Setup a session and test that a Bristol stool scale
    observation can be submitted
    """
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_bristol_stool_obs(self):
        """
        Test that a Bristol Stool Scale observation can be submitted
        """
        bristol_stool_inputs = BRISTOL_STOOL_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(
            PatientPageLocators.open_obs_menu_bs_scale)
        PatientPage(self.driver).enter_obs_data(bristol_stool_inputs)

        success = 'Successfully Submitted Bristol Stool Scale Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(success, response.text,
                         'Bristol Stool Scale observation unsuccessful')
