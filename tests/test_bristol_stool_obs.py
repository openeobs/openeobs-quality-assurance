"""Test to ensure Bristol Stool Scale ob works correctly"""
from openeobs_mobile.data import BRISTOL_STOOL_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.task_page_locators import SUCCESSFUL_SUBMIT
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_BS_SCALE
from tests.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1


class TestBristolStoolObsPage(TestCommon):
    """
    Setup a session and test that a Bristol stool scale
    observation can be submitted
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_patient_list()

    def test_bristol_stool_obs(self):
        """
        Test that a Bristol Stool Scale observation can be submitted
        """
        bristol_stool_inputs = BRISTOL_STOOL_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(
            OPEN_OBS_MENU_BS_SCALE)
        PatientPage(self.driver).enter_obs_data(bristol_stool_inputs)

        success = 'Successfully Submitted Bristol Stool Scale Observation'
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                SUCCESSFUL_SUBMIT))
        )
        response = self.driver.find_element(*SUCCESSFUL_SUBMIT)
        self.assertEqual(success, response.text,
                         'Bristol Stool Scale observation unsuccessful')
