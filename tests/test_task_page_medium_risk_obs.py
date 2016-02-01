"""Test to ensure that a medium risk NEWS ob works correctly"""
from openeobs_mobile.data import MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.task_page_locators import confirm_submit, related_task
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.patient_page_locators import open_obs_menu_news_item


class TestMediumRiskPage(TestCommon):
    """
    Setup a session and test that a medium risk NEWS observation
    can be submitted, and that the correct action triggers
    """

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_medium_risk_obs(self):
        """
        Test that an 'urgently inform medical team' task
        is triggered after a medium NEWS score
        """
        medium_score = MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(medium_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(confirm_submit)
        )

        self.driver.find_element(*confirm_submit).click()

        task = 'Urgently inform medical team'
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((related_task))
        )
        response = self.driver.find_element(*related_task)

        self.assertEqual(task, response.text,
                         'Incorrect triggered action for medium risk ob')
