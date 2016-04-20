"""Test that the user is notified for a patient having no observation data"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.patient_page_locators import GRAPH_CHART
from openeobs_selenium.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1, \
    PATIENT_PAGE
from tests.test_common import TestCommon


class TestPatientPageVisualisationWithNoObsData(TestCommon):
    """
    Test that the No observation data available for patient message
    is shown on no obs being available
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.patient_page = PatientPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.list_page.go_to_patient_list()
        patients = self.list_page.get_list_items()
        patient_to_test = patients[0]
        self.patient_url = patient_to_test.get_attribute('href')
        patient_id = self.patient_url.replace(
            PATIENT_PAGE, ''
        )
        self.patient_page.remove_observations_for_patient(int(patient_id))
        self.driver.get(self.patient_url)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(GRAPH_CHART)
        )

    def test_shows_message_when_no_obs(self):
        """
        Test that the No observation data available for patient message is
        shown on no obs being available
        """

        self.assertTrue(self.patient_page.has_no_patient_data(),
                        'No Observation Data Available message not found')
