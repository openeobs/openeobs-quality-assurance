"""Test that adhoc obs can be submitted successfully"""
from openeobs_mobile.page_confirm import PageConfirm
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
from tests.test_common import TestCommon
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_TITLE, \
    OPEN_OBS_MENU_NEWS_DEADLINE, OPEN_OBS_MENU_NEWS_ITEM, \
    OPEN_OBS_MENU_LIST_ITEMS
from tests.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1, \
    PATIENT_PAGE


class TestPatientPageAdhocObs(TestCommon):
    """
    Test to ensure that the adhoc observation work correctly
    """

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.patient_page = PatientPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.list_page.go_to_patient_list()
        patients = self.list_page.get_list_items()
        patient_to_test = patients[0]
        self.patient_url = patient_to_test.get_attribute('href')
        self.driver.get(self.patient_url)

    def test_can_logout(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.patient_page.logout()
        self.assertTrue(PageConfirm(self.driver).is_login_page(),
                        'Did not get to the logout page correctly')

    def test_can_go_to_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.patient_page.go_to_task_list()
        self.assertTrue(PageConfirm(self.driver).is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_go_to_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.patient_page.go_to_patient_list()
        self.assertTrue(PageConfirm(self.driver).is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_to_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.patient_page.go_to_standin()
        self.assertTrue(PageConfirm(self.driver).is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_carry_out_barcode_scan(self):
        """
        Test that can do a barcode scan
        """
        task_id = self.patient_url.replace(
            PATIENT_PAGE, ''
        )
        id_to_use = self.patient_page.patient_scan_helper(int(task_id))
        self.patient_page.do_barcode_scan(id_to_use['other_identifier'])

    def test_can_open_adhoc_menu(self):
        """
        Test that can see and open a menu to select an adhoc observation to
        carry out for the patient
        """
        menu = self.patient_page.open_adhoc_obs_menu()
        menu_title = menu.find_element(
            *OPEN_OBS_MENU_TITLE
        )
        observations = menu.find_elements(
            *OPEN_OBS_MENU_LIST_ITEMS
        )
        self.assertGreater(len(observations), 0,
                           'Incorrect number of adhoc obs')
        task_id = self.patient_url.replace(
            PATIENT_PAGE, ''
        )
        data = self.patient_page.patient_helper(int(task_id))[0]
        patient_name = data['full_name']
        self.assertEqual(menu_title.text,
                         'Pick an observation for {0}'.format(patient_name),
                         'Incorrect menu title')

    def test_adhoc_news_ob_deadline(self):
        """
        Test that the NEWS observation in the adhoc observation list shows
        the deadline to the next scheduled NEWS observation
        """
        menu = self.patient_page.open_adhoc_obs_menu()
        news_item = menu.find_element(
            *OPEN_OBS_MENU_NEWS_ITEM
        )
        deadline = news_item.find_element(
            *OPEN_OBS_MENU_NEWS_DEADLINE
        )
        task_id = self.patient_url.replace(
            PATIENT_PAGE, ''
        )
        data = self.patient_page.patient_helper(int(task_id))[0]
        ews_deadline = data['next_ews_time']
        self.assertEqual(deadline.text, ews_deadline,
                         'Incorrect NEWS deadline')
