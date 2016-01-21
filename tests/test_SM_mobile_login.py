__author__ = 'amipatel'
from test_common import TestCommon
from openeobs_selenium.login_page import LoginPage
from openeobs_selenium.task_page import TaskPage
from openeobs_selenium.patient_page import PatientPage
class TestSMPatientPage(TestCommon):

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/patients/")
        self.login_page = LoginPage(self.driver)
        self.task_list_page = TaskPage(self.driver)
        self.login_page.login('saint','saint')
        self.task_list_page.go_to_task_list()

    def test_can_logout(self):
        self.task_list_page.logout()
        self.assertTrue(self.task_list_page.is_login_page(), 'did notget to the logout')
    #
    # def test_can_see_no_patient(self):
    #     patient_list = PatientPage.has_patient()
    #     print list(patient_list)