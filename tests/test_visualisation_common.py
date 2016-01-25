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

    def test_doesnt_show_no_obs_message(self):
        """
        Test that the No observation data available for patient message is
        shown on no obs being available
        """
        self.assertFalse(self.patient_page.has_no_patient_data(),
                         'No Observation Data Available message not found')

    def test_shows_tabs(self):
        """
        Test that the tabs are shown
        """
        self.assertTrue(self.patient_page.tabs_are_shown(),
                        'Tabs to switch between chart and table are not shown')

    def test_shows_chart(self):
        """
        Test that the chart is displayed with a single data point present
        """
        self.assertTrue(self.patient_page.chart_is_shown(),
                        'Chart is not shown')

    def test_shows_tabular_values(self):
        """
        Test that shows the tabular values table
        """
        self.assertTrue(self.patient_page.tabular_values_are_shown(),
                        'Tabular values aren\'t shown')

    def test_shows_table(self):
        """
        Test that pressing the table tab shows the table
        """
        self.patient_page.change_to_table()
        self.assertTrue(self.patient_page.obs_table_is_shown(),
                        'Observation table is not shown')

    def test_shows_obs_menu(self):
        """
        Test that pressing the take Observation button still works
        """
        self.patient_page.open_adhoc_obs_menu()
        self.assertTrue(self.patient_page.adhoc_obs_menu_is_open(),
                        'Adhoc observation menu is not open')

    def test_shows_chart_after_viewing_table(self):
        """
        Test that pressing the chart tab after being on table tab works
        """
        self.patient_page.change_to_table()
        self.patient_page.change_to_chart()
        self.assertTrue(self.patient_page.chart_is_shown(),
                        'Chart does not display when returning from table')

    def test_shows_ranged_values_control(self):
        """
        Test that the ranged values control is shown
        """
        self.assertTrue(self.patient_page.rangify_control_is_shown(),
                        'Rangify control not shown')
