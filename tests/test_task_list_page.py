from openeobs_selenium.login_page import LoginPage
from openeobs_selenium.list_page import ListPage
from test_common import TestCommon
from openeobs_selenium.page_helpers import ListPageLocators


class TestTaskListPage(TestCommon):

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.task_list_page = ListPage(self.driver)
        self.login_page.login('nasir', 'nasir')
        self.task_list_page.go_to_task_list()

    def test_can_logout(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.task_list_page.logout()
        self.assertTrue(self.task_list_page.is_login_page(),
                        'Did not get to the logout page correctly')

    def test_can_go_to_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.task_list_page.go_to_task_list()
        self.assertTrue(self.task_list_page.is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_can_go_to_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.task_list_page.go_to_patient_list()
        self.assertTrue(self.task_list_page.is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_to_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.task_list_page.go_to_standin()
        self.assertTrue(self.task_list_page.is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_carry_out_barcode_scan(self):
        """
        Test that can do a barcode scan
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        id_to_use = self.task_list_page.task_helper(task_id)
        self.task_list_page.do_barcode_scan(id_to_use['other_identifier'])

    def test_can_click_list_item_to_carry_out_task(self):
        """
        Test that clicking on a work item tasks user to carry out the task
        """
        tasks = self.task_list_page.get_list_items()
        task_to_test = tasks[0]
        task_url = task_to_test.get_attribute('href')
        task_to_test.click()
        self.assertTrue(self.task_list_page.is_task_page(),
                        'Did not get to task page correctly')
        self.assertEqual(self.driver.current_url, task_url,
                         'Incorrect url')

    def test_list_item_contains_patient_name(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        name_to_use = self.task_list_page.task_helper(task_id)['display_name']
        patient_name = self.driver.find_element(
            *ListPageLocators.list_item_patient_name
        )
        self.assertEqual(patient_name.text, name_to_use, 'Incorrect name')

    def test_list_item_contains_patient_location(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        bed_to_use = \
            self.task_list_page.task_helper(task_id)['current_location_id'][1]
        patient_location = self.driver.find_element(
            *ListPageLocators.list_item_patient_location
        )
        self.assertIn(bed_to_use, patient_location.text, 'Incorrect location')
