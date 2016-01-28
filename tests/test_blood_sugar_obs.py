from openeobs_mobile.data import BLOOD_SUGAR_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from test_common import TestCommon
from openeobs_mobile.locators import PatientPageLocators, TaskPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


class TestBloodSugarObsPage(TestCommon):

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
                PatientPageLocators.open_obs_menu_blood_sugar_item)
        PatientPage(self.driver).enter_obs_data(blood_sugar_input)

        success = 'Successfully Submitted Blood Sugar Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Blood sugar observation unsuccessful')
