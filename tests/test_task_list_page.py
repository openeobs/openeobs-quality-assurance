"""Tests to ensure that the task list page works correctly"""
from openeobs_mobile import ListPageLocators
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from tests.test_common import TestCommon



class TestTaskListPage(TestCommon):
    """
    Setup a session and test that the task list page works correctly
    """
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

    def test_go_to_patient_list_page(self):
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
        id_to_use = self.task_list_page.task_scan_helper(task_id)
        self.task_list_page.do_barcode_scan(id_to_use['other_identifier'])

    def test_click_list_item(self):
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

    def test_list_item_patient_name(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        name_to_use = task_data['full_name']
        patient_name = self.driver.find_element(
            *ListPageLocators.list_item_patient_name
        )
        self.assertEqual(patient_name.text, name_to_use.strip(),
                         'Incorrect name')

    def test_list_item_patient_location(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        location = task_data['location']
        parent_location = task_data['parent_location']
        bed_to_use = '{0}, {1}'.format(location, parent_location)
        patient_location = self.driver.find_element(
            *ListPageLocators.list_item_patient_location
        )
        self.assertEqual(bed_to_use, patient_location.text,
                         'Incorrect location')

    def test_list_item_score_trend(self):
        """
        Test that the score and trend are present in list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        score = task_data['ews_score']
        trend = task_data['ews_trend']
        score_str = '({0} )'.format(score)
        patient_trend = self.driver.find_element(
            *ListPageLocators.list_item_patient_trend
        )
        trend_str = 'icon-{0}-arrow'.format(trend)
        patient_trend = patient_trend.get_attribute('class')
        self.assertEqual(patient_trend.get_attribute('class'), trend_str,
                         'Incorrect trend')
        self.assertIn(score_str, patient_to_test.text, 'Incorrect score')

    def test_list_item_task_deadline(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        deadline = task_data['deadline_time']
        task_deadline = self.driver.find_element(
            *ListPageLocators.list_item_deadline
        )
        self.assertEqual(deadline, task_deadline.text,
                         'Incorrect deadline')

    def test_list_item_task_summary(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            'http://localhost:8069/mobile/task/', ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        summary = task_data['summary']
        task_summary = self.driver.find_element(
            *ListPageLocators.list_item_title
        )
        self.assertEqual(summary, task_summary.text,
                         'Incorrect summary')

    def test_shows_tasks(self):
        """
        Test that the task list shows tasks for the user
        """
        task_list = []
        for patient in self.task_list_page.get_list_items():
            task_list.append(patient)

        self.assertNotEquals(task_list, [], 'Task list not showing tasks')
