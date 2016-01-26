from selenium.common.exceptions import NoSuchElementException
from test_common import TestCommon
from openeobs_selenium.patient_page import PatientPage
from openeobs_selenium.login_page import LoginPage
from openeobs_selenium.task_page import TaskPage
from openeobs_selenium.list_page import ListPage
from openeobs_selenium.page_helpers import PatientPageLocators

class TestSMPatientPage(TestCommon):
    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.task_list_page = ListPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.patient_page = PatientPage(self.driver)
        self.login_page.login('saint', 'saint')
        self.task_list_page.go_to_task_list()

    def test_can_logout(self):
        self.task_list_page.logout()
        self.assertTrue(self.task_list_page.is_login_page(), 'did not get to the logout')

    def test_has_no_task(self):
        """
        Senior Manager should not see any observation related tasks in tasks list
        """

        task_list = []

        for patient in self.task_list_page.get_list_items():
            task_list.append(patient)
            self.assertEquals(task_list,[],'There are no tasks')

    def test_go_to_patients_list_page(self):
        """
        Senior manager should allowed to see patient list
        """
        self.patient_list_page.go_to_patient_list()
        self.assertTrue(self.patient_page.is_patient_list_page(),'Did not go to patient page correctly')

    def test_can_not_take_patient_observation(self):
        """
        Senior manager should not allowed to take ad-hoc observation from mobile version of eobs.
        """
        # menu = self.patient_page.open_adhoc_obs_menu()
        self.patient_list_page.go_to_patient_list()

        patients = self.patient_list_page.get_list_items()
        patients_to_test = patients[0]
        patients_to_test.click()

        # try:
        #     adhoc_obs_menu_button = self.driver.find_element(*PatientPageLocators.adhoc_obs_menu_button).is_displayed()
        #
         #except NoSuchElementException:
          #   print('test')
        adhoc_obs_menu_button = self.driver.find_elements(*PatientPageLocators.adhoc_obs_menu_button)
        # print(adhoc_obs_menu_button)
        self.assertEquals(adhoc_obs_menu_button,[],'Obs button should not be visible to Senior Manager ')
        #    if adhoc_obs_menu_button:
        #        print('SM is not allowed to take observation')









