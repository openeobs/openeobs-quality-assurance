"""Tests to ensure that the patient list page works correctly"""
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from tests.test_common import TestCommon
from openeobs_mobile.locators import ListPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.PatientPageLocators import *


class TestPatientListPage(TestCommon):
    """
    Setup a session and test that the task list page works correctly
    """
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.patient_list_page.go_to_patient_list()

    def test_can_logout(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.patient_list_page.logout()
        self.assertTrue(self.patient_list_page.is_login_page(),
                        'Did not get to the logout page correctly')

    def test_can_go_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.patient_list_page.go_to_task_list()
        self.assertTrue(self.patient_list_page.is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.patient_list_page.go_to_patient_list()
        self.assertTrue(self.patient_list_page.is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.patient_list_page.go_to_standin()
        self.assertTrue(self.patient_list_page.is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_do_barcode_scan(self):
        """
        Test that can do a barcode scan
        """
        patients = self.patient_list_page.get_list_items()
        patient_to_test = patients[0]
        patient_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/patient/', ''
        )
        id_to_use = self.patient_list_page.patient_scan_helper(int(patient_id))
        self.patient_list_page.do_barcode_scan(id_to_use['other_identifier'])

    def test_view_patient_details(self):
        """
        Test that clicking on a work item tasks user to carry out the task
        """
        patients = self.patient_list_page.get_list_items()
        patient_to_test = patients[0]
        patient_url = patient_to_test.get_attribute('href')
        patient_to_test.click()
        self.assertTrue(self.patient_list_page.is_patient_page(),
                        'Did not get to patient page correctly')
        self.assertEqual(self.driver.current_url, patient_url,
                         'Incorrect url')

    def test_patient_name_in_list(self):
        """
        Test that the patient name is in the list item
        """
        patients = self.patient_list_page.get_list_items()
        patient_to_test = patients[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/patient/', ''
        )
        task_data = self.patient_list_page.patient_helper(task_id)[0]
        name_to_use = task_data['full_name']
        patient_name = self.driver.find_element(
            *ListPageLocators.list_item_patient_name
        )
        self.assertEqual(patient_name.text, name_to_use.strip(),
                         'Incorrect name')

    def test_patient_location_in_list(self):
        """
        Test that the patient name is in the list item
        """
        patients = self.patient_list_page.get_list_items()
        patient_to_test = patients[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/patient/', ''
        )
        task_data = self.patient_list_page.patient_helper(task_id)[0]
        location = task_data['location']
        parent_location = task_data['parent_location']
        bed_to_use = '{0}, {1}'.format(location, parent_location)
        patient_location = self.driver.find_element(
            *ListPageLocators.list_item_patient_location
        )
        self.assertEqual(bed_to_use, patient_location.text,
                         'Incorrect location')

    def test_score_and_trend_in_list(self):
        """
        Test that the score and trend are present in list item
        """
        tasks = self.patient_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/patient/', ''
        )
        task_data = self.patient_list_page.patient_helper(task_id)[0]
        score = task_data['ews_score']
        trend = task_data['ews_trend']
        score_str = '({0} )'.format(score)
        patient_trend = self.driver.find_element(
            *ListPageLocators.list_item_patient_trend
        )
        trend_str = 'icon-{0}-arrow'.format(trend)
        self.assertEqual(patient_trend.get_attribute('class'), trend_str,
                         'Incorrect trend')
        self.assertIn(score_str, patient_to_test.text, 'Incorrect score')

    def test_task_deadline_in_list(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.patient_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/patient/', ''
        )
        task_data = self.patient_list_page.patient_helper(task_id)[0]
        deadline = task_data['next_ews_time']
        task_deadline = self.driver.find_element(
            *ListPageLocators.list_item_deadline
        )
        self.assertEqual(deadline, task_deadline.text,
                         'Incorrect deadline')

    def test_shows_patients(self):
        """
        Test that the patient list shows patients for the user
        """
        patient_list = []
        for patient in self.patient_list_page.get_list_items():
            patient_list.append(patient)

        self.assertNotEquals(patient_list, [],
                             'Patient list not showing patients')

    def test_shows_patient_data(self):
        """
        Test that a patient record shows data (graph/table) for the patient
        """
        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)

        ui.WebDriverWait(self.driver, 1).until(
            ec.visibility_of_element_located(graph_chart)
        )

        patient_graph = self.driver.find_element(*graph_chart)

        self.assertEqual(patient_graph.is_displayed(), True, 'Graph not found')

        self.driver.find_element(*table_tab_button).click()

        ui.WebDriverWait(self.driver, 1).until(
            ec.visibility_of_element_located
            (table_container_table))

        patient_table = self.driver.find_element(*table_container_table)
        self.assertEqual(patient_table.is_displayed(), True, 'Table not found')

    def test_adhoc_obs(self):
        """
        Test that a patient record allows for adhoc obs
        """
        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        obs_menu = PatientPage(self.driver).open_adhoc_obs_menu()

        self.assertEqual(obs_menu.is_displayed(), True,
                         'Obs menu is not present')
