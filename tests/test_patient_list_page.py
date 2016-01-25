import time

from openeobs_mobile.data import Data_Dicts
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.task_page import TaskPage
from test_common import TestCommon
from openeobs_mobile.locators import ListPageLocators, PatientPageLocators, \
    TaskPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


class TestPatientListPage(TestCommon):

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

    def test_can_go_to_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.patient_list_page.go_to_task_list()
        self.assertTrue(self.patient_list_page.is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_can_go_to_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.patient_list_page.go_to_patient_list()
        self.assertTrue(self.patient_list_page.is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_to_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.patient_list_page.go_to_standin()
        self.assertTrue(self.patient_list_page.is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_carry_out_barcode_scan(self):
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

    def test_can_click_list_item_to_view_patient_details(self):
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

    def test_list_item_contains_patient_name(self):
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

    def test_list_item_contains_patient_location(self):
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

    def test_list_item_contains_score_and_trend(self):
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

    def test_list_item_contains_task_deadline(self):
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

        self.assertNotEquals(patient_list, [], 'Patient list not showing patients')


    def test_shows_patient_data(self):
        """
        Test that a patient record shows data (graph/table) for the patient
        """
        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)

        patient_graph = ui.WebDriverWait(self.driver, 1).until(
            ec.visibility_of_element_located((PatientPageLocators.graph_chart))
        )

        self.assertEqual(patient_graph.is_displayed(), True, 'Graph not found')

        self.driver.find_element(
                *PatientPageLocators.table_tab_button).click()

        patient_table = ui.WebDriverWait(self.driver, 1).until(
            ec.visibility_of_element_located((PatientPageLocators.table_container_table))
        )

        self.assertEqual(patient_table.is_displayed(), True, 'Table not found')

    def test_adhoc_obs(self):
        """
        Test that a patient record allows for adhoc obs
        """
        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        obs_menu = PatientPage(self.driver).open_adhoc_obs_menu()

        self.assertEqual(obs_menu.is_displayed(), True, 'Obs menu is not present')

    def test_assess_patient(self):
        """
        Test that an 'assess patient' task is triggered after a low NEWS score
        """
        low_score = Data_Dicts.LOW_RISK_SCORE_1_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(low_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((TaskPageLocators.confirm_submit))
        ).click()

        task = 'Assess Patient'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.related_task))
        )
        self.assertEqual(
                task, response.text, 'Incorrect triggered action')

    def test_urgently_inform_medical_team(self):
        """
        Test that an 'urgently inform medical team' task is triggered after a medium NEWS score
        """
        medium_score = Data_Dicts.MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(medium_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((TaskPageLocators.confirm_submit))
        ).click()

        task = 'Urgently inform medical team'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.related_task))
        )
        self.assertEqual(
                task, response.text, 'Incorrect triggered action')

    def test_immediately_inform_medical_team(self):
        """
        Test that an 'immediately inform medical team' task is triggered after a high NEWS score
        """
        high_score = Data_Dicts.HIGH_RISK_SCORE_9_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(high_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((TaskPageLocators.confirm_submit))
        ).click()

        task = 'Immediately inform medical team'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.related_task))
        )
        self.assertEqual(
                task, response.text, 'Incorrect triggered action')

    def test_news_ob(self):
        """
        Test that a NEWS observation can be submitted
        """
        score = Data_Dicts.NO_RISK_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_news_item)
        PatientPage(self.driver).enter_obs_data(score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((TaskPageLocators.confirm_submit))
        ).click()

        success = 'Successfully Submitted NEWS Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )
        self.assertEqual(
                success, response.text, 'NEWS observation unsuccessful')

    def test_gcs_obs(self):
        """
        Test that a GCS observation can be submitted
        """
        gcs_inputs = Data_Dicts.GCS_SCORE_15_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_gcs_item)
        PatientPage(self.driver).enter_obs_data(gcs_inputs)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((TaskPageLocators.confirm_submit))
        ).click()

        success = 'Successfully Submitted GCS Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'GCS observation unsuccessful')

    def test_height_obs(self):
        """
        Test that a height observation can be submitted
        """
        height_input = Data_Dicts.HEIGHT_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_height_item)
        PatientPage(self.driver).enter_obs_data(height_input)

        success = 'Successfully Submitted Height Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Height observation unsuccessful')

    def test_weight_obs(self):
        """
        Test that a weight observation can be submitted
        """
        weight_input = Data_Dicts.WEIGHT_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_weight_item)
        PatientPage(self.driver).enter_obs_data(weight_input)

        success = 'Successfully Submitted Weight Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Weight observation unsuccessful')

    def test_blood_product_obs(self):
        """
        Test that a blood product observation can be submitted
        """
        blood_product_inputs = Data_Dicts.BLOOD_PRODUCT_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_blood_product_item)
        PatientPage(self.driver).enter_obs_data(blood_product_inputs)

        success = 'Successfully Submitted Blood Product Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Blood product observation unsuccessful')

    def test_blood_sugar_obs(self):
        """
        Test that a blood sugar observation can be submitted
        """
        blood_sugar_input = Data_Dicts.BLOOD_SUGAR_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_blood_sugar_item)
        PatientPage(self.driver).enter_obs_data(blood_sugar_input)

        success = 'Successfully Submitted Blood Sugar Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Blood sugar observation unsuccessful')

    def test_bristol_stool_obs(self):
        """
        Test that a bristol stool scale observation can be submitted
        """
        bristol_stool_inputs = Data_Dicts.BRISTOL_STOOL_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_bristol_stool_item)
        PatientPage(self.driver).enter_obs_data(bristol_stool_inputs)

        success = 'Successfully Submitted Bristol Stool Scale Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Bristol Stool Scale observation unsuccessful')

    def test_postural_blood_pressure_obs(self):
        """
        Test that a postural blood pressure observation can be submitted
        """
        postural_pressure_inputs = Data_Dicts.POSTURAL_BLOOD_PRESSURE_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(PatientPageLocators.open_obs_menu_postural_pressure_item)
        PatientPage(self.driver).enter_obs_data(postural_pressure_inputs)

        success = 'Successfully Submitted Postural Blood Pressure Observation'
        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                TaskPageLocators.successful_submit))
        )

        self.assertEqual(
                success, response.text, 'Postural blood pressure observation unsuccessful')
