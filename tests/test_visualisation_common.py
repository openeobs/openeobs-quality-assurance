from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from test_common import TestCommon


class TestVisualisationCommon(TestCommon):

    risk = 'none'

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.patient_page = PatientPage(self.driver)

        risk_mapping = {
            'none': self.patient_page.add_no_risk_observation_for_patient,
            'low': self.patient_page.add_low_risk_observation_for_patient,
            'medium':
                self.patient_page.add_medium_risk_observation_for_patient,
            'high': self.patient_page.add_high_risk_observation_for_patient,
            '3in1': self.patient_page.add_three_in_one_observation_for_patient
        }

        self.login_page.login('nasir', 'nasir')
        self.list_page.go_to_patient_list()
        patients = self.list_page.get_list_items()
        patient_to_test = patients[0]
        self.patient_url = patient_to_test.get_attribute('href')
        self.patient_id = self.patient_url.replace(
            'http://localhost:8069/mobile/patient/', ''
        )
        self.patient_page.remove_observations_for_patient(int(self.patient_id))
        risk_mapping[self.risk](int(self.patient_id))
        self.driver.get(self.patient_url)
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                     '#chart svg')
            )
        )
