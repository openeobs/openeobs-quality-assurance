"""Test to ensure that a medium risk NEWS ob works correctly"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.data import MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA, \
    MEDIUM_SCORE_RESPONSE
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_NEWS_ITEM
from openeobs_mobile.task_page_locators import CONFIRM_SUBMIT, RELATED_TASK
from openeobs_selenium.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1
from tests.test_common import TestCommon


class TestMediumRiskPage(TestCommon):
    """
    Setup a session and test that a medium risk NEWS observation
    can be submitted, and that the correct action triggers
    """

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_patient_list()

    def test_medium_risk_obs(self):
        """
        Test that an 'urgently inform medical team' task
        is triggered after a medium NEWS score
        """
        medium_score = MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(OPEN_OBS_MENU_NEWS_ITEM)
        PatientPage(self.driver).enter_obs_data(medium_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(CONFIRM_SUBMIT)
        )

        self.driver.find_element(*CONFIRM_SUBMIT).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(RELATED_TASK)
        )
        response = self.driver.find_element(*RELATED_TASK)

        self.assertEqual(MEDIUM_SCORE_RESPONSE, response.text,
                         'Incorrect triggered action for medium risk ob')
