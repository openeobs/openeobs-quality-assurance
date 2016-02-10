"""Tests to ensure that the task list page works correctly"""
from openeobs_mobile import list_page_locators
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.page_confirm import PageConfirm
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_NEWS_ITEM
from tests.test_common import TestCommon
from tests.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1, TASK_PAGE
from openeobs_mobile.task_page_locators import CONFIRM_SUBMIT, \
    SUCCESSFUL_SUBMIT
from openeobs_mobile.data import HIGH_RISK_SCORE_9_EWS_DATA, NO_RISK_EWS_DATA
from openeobs_mobile.patient_page import PatientPage
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.task_page_locators import GO_TO_MY_TASK


class TestTaskListPage(TestCommon):
    """
    Setup a session and test that the task list page works correctly
    """

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.task_list_page = ListPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.task_list_page.go_to_task_list()

    def test_can_logout(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.task_list_page.logout()
        self.assertTrue(PageConfirm(self.driver).is_login_page(),
                        'Did not get to the logout page correctly')

    def test_can_go_to_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.task_list_page.go_to_task_list()
        self.assertTrue(PageConfirm(self.driver).is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_go_to_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.task_list_page.go_to_patient_list()
        self.assertTrue(PageConfirm(self.driver).is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_to_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.task_list_page.go_to_standin()
        self.assertTrue(PageConfirm(self.driver).is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_carry_out_barcode_scan(self):
        """
        Test that can do a barcode scan
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            TASK_PAGE, ''
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
        self.assertTrue(PageConfirm(self.driver).is_task_page(),
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
            TASK_PAGE, ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        name_to_use = task_data['full_name']
        patient_name = self.driver.find_element(
            *list_page_locators.LIST_ITEM_PATIENT_NAME
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
            TASK_PAGE, ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        location = task_data['location']
        parent_location = task_data['parent_location']
        bed_to_use = '{0}, {1}'.format(location, parent_location)
        patient_location = self.driver.find_element(
            *list_page_locators.LIST_ITEM_PATIENT_LOCATION
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
            TASK_PAGE, ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        score = task_data['ews_score']
        trend = task_data['ews_trend']
        score_str = '({0} )'.format(score)
        patient_trend = self.driver.find_elements(
            *list_page_locators.LIST_ITEM_PATIENT_TREND
        )
        for item in patient_trend:
            if item.get_attribute('class') == 'icon-alert':
                patient_trend.remove(item)

        trend_str = 'icon-{0}-arrow'.format(trend)
        self.assertEqual(patient_trend[0].get_attribute('class'), trend_str,
                         'Incorrect trend')
        self.assertIn(score_str, patient_to_test.text, 'Incorrect score')

    def test_list_item_task_deadline(self):
        """
        Test that the patient name is in the list item
        """
        tasks = self.task_list_page.get_list_items()
        patient_to_test = tasks[0]
        task_id = patient_to_test.get_attribute('href').replace(
            TASK_PAGE, ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        deadline = task_data['deadline_time']
        task_deadline = self.driver.find_element(
            *list_page_locators.LIST_ITEM_DEADLINE
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
            TASK_PAGE, ''
        )
        task_data = self.task_list_page.task_helper(task_id)[0]
        summary = task_data['summary']
        task_summary = self.driver.find_element(
            *list_page_locators.LIST_ITEM_TITLE
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

    def test_take_task_news_obs(self):
        """
        Submit adhoc observation which creates News observation task
        and Take task NEWS Observation from task list, submit news score
        """

        # Enter high risk observation to create News Observation task in task
        # list
        self.patient_list_page.go_to_patient_list()
        high_score = HIGH_RISK_SCORE_9_EWS_DATA
        no_risk = NO_RISK_EWS_DATA
        news_task = []
        success = 'Successfully Submitted NEWS Observation'

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(OPEN_OBS_MENU_NEWS_ITEM)
        PatientPage(self.driver).enter_obs_data(high_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(CONFIRM_SUBMIT)
        )
        self.driver.find_element(*CONFIRM_SUBMIT).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                SUCCESSFUL_SUBMIT))
        )
        response = self.driver.find_element(*SUCCESSFUL_SUBMIT)
        self.assertEqual(success, response.text,
                         'NEWS observation unsuccessful')

        self.driver.find_element(*GO_TO_MY_TASK).click()

        # Click on the first news score task from Task list
        self.task_list_page.go_to_task_list()

        self.driver.refresh()
        for task in self.task_list_page.get_list_task():
            # print(task.text)
            if task.text == 'NEWS Observation':
                news_task.append(task)
        news_task[0].click()

        # enter low risk observation
        PatientPage(self.driver).enter_obs_data(no_risk)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(CONFIRM_SUBMIT)
        )

        self.driver.find_element(*CONFIRM_SUBMIT).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                SUCCESSFUL_SUBMIT))
        )
        response = self.driver.find_element(*SUCCESSFUL_SUBMIT)
        self.assertEqual(success, response.text,
                         'NEWS observation unsuccessful')
        # print(news_task)
