from openeobs_selenium.task_page import TaskPage
from openeobs_selenium.login_page import LoginPage
from openeobs_selenium.list_page import ListPage
from test_common import TestCommon
from openeobs_selenium.page_helpers import TaskPageLocators


class TestTaskPagePatientInfo(TestCommon):

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.task_page = TaskPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.list_page.go_to_task_list()
        tasks = self.list_page.get_list_items()
        task_to_test = tasks[0]
        self.task_url = task_to_test.get_attribute('href')
        self.driver.get(self.task_url)

    def test_can_logout(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.task_page.logout()
        self.assertTrue(self.task_page.is_login_page(),
                        'Did not get to the logout page correctly')

    def test_can_go_to_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.task_page.go_to_task_list()
        self.assertTrue(self.task_page.is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_can_go_to_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.task_page.go_to_patient_list()
        self.assertTrue(self.task_page.is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_to_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.task_page.go_to_standin()
        self.assertTrue(self.task_page.is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_carry_out_barcode_scan(self):
        """
        Test that can do a barcode scan
        """
        task_id = self.task_url.replace(
            'http://localhost:8069/mobile/task/', ''
        )
        id_to_use = self.task_page.task_scan_helper(int(task_id))
        self.task_page.do_barcode_scan(id_to_use['other_identifier'])

    def test_can_see_patient_info_on_pressing_patient_name(self):
        """
        Test that can get the patient info popup on pressing patient name
        """
        patient_name_button = self.driver.find_element(
            *TaskPageLocators.patient_name_link
        )
        patient_id = patient_name_button.get_attribute('patient-id')

        popup = self.task_page.open_patient_info()
        popup_header = popup.find_element(
            *TaskPageLocators.patient_info_popup_title
        )
        patient_data = self.task_page.patient_helper(int(patient_id))[0]
        popup_title = '{0}{1}'.format(patient_data['full_name'],
                                       patient_data['gender'])
        self.assertEqual(popup_title, popup_header.text.replace('\n', ' '),
                         'Incorrect popup name')

    def test_can_see_patient_info_on_pressing_info_button(self):
        """
        Test that can get the patient info popup on pressing patient name
        """
        patient_name_button = self.driver.find_element(
            *TaskPageLocators.patient_name_info
        )
        patient_id = patient_name_button.get_attribute('patient-id')

        popup = self.task_page.open_patient_info()
        popup_header = popup.find_element(
            *TaskPageLocators.patient_info_popup_title
        )
        patient_data = self.task_page.patient_helper(int(patient_id))[0]
        popup_title = '{0}{1}'.format(patient_data['full_name'],
                                       patient_data['gender'])
        self.assertEqual(popup_title, popup_header.text.replace('\n', ' '),
                         'Incorrect popup name')

    def test_pressing_patient_obs_data_button_shows_patient_page(self):
        """
        Test that pressing the 'View Patient Observation Data' shows the
        patient page in a fullscreen modal
        """
        patient_name_button = self.driver.find_element(
            *TaskPageLocators.patient_name_info
        )
        patient_id = patient_name_button.get_attribute('patient-id')
        fullscreen = self.task_page.open_patient_obs_data_fullscreen()
        iframe = fullscreen.find_element(
            *TaskPageLocators.patient_info_fullscreen_iframe
        )
        iframe_url = iframe.get_attribute('src')
        patient_url = 'http://localhost:8069/mobile/patient/{0}'.format(
            patient_id
        )
        self.assertEqual(iframe_url, patient_url, 'Incorrect iframe src url')

    def test_can_close_full_patient_obs_modal(self):
        """
        Test that can close the fullscreen modal
        """
        fullscreen = self.task_page.open_patient_obs_data_fullscreen()
        close_button = fullscreen.find_element(
            *TaskPageLocators.patient_info_fullscreen_close
        )
        close_button.click()
        self.assertTrue(self.task_page.fullscreen_not_open(),
                        'Fullscreen did not close')