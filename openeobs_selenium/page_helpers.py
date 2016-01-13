from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from erppeek import Client


class BasePage(object):
    """
    Base class to initialise the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver

    def go_to_task_list(self):
        """
        Navigate to the task list
        """
        task_list_item = self.driver.find_element(*MenuLocators.task_list_el)
        task_list_item.click()

    def go_to_patient_list(self):
        """
        Navigate to the patient list
        """
        patient_list_item = \
            self.driver.find_element(*MenuLocators.patient_list_el)
        patient_list_item.click()

    def logout(self):
        """
        Log out of the app
        """
        logout = self.driver.find_element(*MenuLocators.logout_el)
        logout.click()

    def go_to_standin(self):
        """
        Go to the stand in page
        """
        standin_item = self.driver.find_element(*MenuLocators.stand_in_el)
        standin_item.click()

    @staticmethod
    def task_helper(task_id, database='openeobs_quality_assurance_db',
                    user='nasir', password='nasir'):
        """
        use a task id to get id for do a barcode scan
        :param task_id: ID of Task to do foo
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        return odoo_client.model('nh.eobs.api').get_activities([task_id])

    @staticmethod
    def patient_helper(patient_id, database='openeobs_quality_assurance_db',
                       user='nasir', password='nasir'):
        """
        use a patient id to get id for do a barcode scan
        :param patient_id: ID of patient to do foo
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        return odoo_client.model('nh.eobs.api').get_patients([int(patient_id)])

    @staticmethod
    def task_scan_helper(task_id, database='openeobs_quality_assurance_db',
                         user='nasir', password='nasir'):
        """
        use a task id to get id for do a barcode scan
        :param task_id: ID of Task to do foo
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        patient_api = odoo_client.model('nh.clinical.patient')
        activity_record = activity_api.read(int(task_id), ['patient_id'])
        patient_id = activity_record['patient_id'][0]
        patient_record = patient_api.read(patient_id, [
            'other_identifier',
            'patient_identifier',
            'display_name',
            'current_location_id'
        ])
        return patient_record

    @staticmethod
    def patient_scan_helper(patient_id,
                            database='openeobs_quality_assurance_db',
                            user='nasir', password='nasir'):
        """
        use a patient id to get id for do a barcode scan
        :param patient_id: ID of patient to do foo
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        patient_api = odoo_client.model('nh.clinical.patient')
        patient_record = patient_api.read(patient_id, [
            'other_identifier',
            'patient_identifier',
            'display_name',
            'current_location_id'
        ])
        return patient_record

    @staticmethod
    def remove_observations_for_patient(
            patient_id,  database='openeobs_quality_assurance_db',
            user='admin', password='admin'):
        """
        Remove all the observations for the patient
        :param patient_id: The patient to remove obs for
        :return: Boolean of if the operation was successful
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        # Find activity of news type with parent id of patient spell
        activity_api = odoo_client.model('nh.activity')
        spells = activity_api.search([
            ['state', '=', 'started'],
            ['data_model', '=', 'nh.clinical.spell'],
            ['patient_id', '=', patient_id]
        ])
        obs = activity_api.search([
            ['data_model', '=', 'nh.clinical.patient.observation.ews'],
            ['parent_id', 'in', spells]
        ])
        activity_api.unlink(obs)

    def do_barcode_scan(self, patient_id):
        """
        Carry out a barcode scan with the patient id
        :param patient_id:
        """
        scan_item = self.driver.find_element(*MenuLocators.barcode_scan_el)
        scan_item.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    (By.ID,
                     'patient_barcode')
            )
        )
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                (By.CSS_SELECTOR, '#patient_barcode .barcode_scan')
            )
        )
        try:
            barcode_input = \
                self.driver.find_element(*MenuLocators.barcode_scan_input)
            self.driver.execute_script(
                "var scan = document.getElementsByName('barcode_scan')[0]; "
                "scan.setAttribute('value', ',{0},'); "
                "scan.textContent = ',{0},';".format(patient_id)
            )
            barcode_input.send_keys(Keys.ENTER)
            ui.WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(
                        (By.TAG_NAME,
                         'dl')
                )
            )
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def is_login_page(self):
        """
        Check that the page's title matches that of the login page
        :return: Boolean of if the title matches or not
        """
        return '/mobile/login' in self.driver.current_url

    def is_task_list_page(self):
        """
        Check that is task_list page
        :return: Boolean of if is on task list page
        """
        return '/mobile/tasks' in self.driver.current_url

    def is_patient_list_page(self):
        """
        Check that is on patient list page
        :return: Boolean of if is on patient list page
        """
        return '/mobile/patients' in self.driver.current_url

    def is_task_page(self):
        """
        Check that is on a task page
        :return: Boolean of if is on a task page
        """
        return '/mobile/task/' in self.driver.current_url

    def is_patient_page(self):
        """
        Check that is on a patient page
        :return: Boolea of if is on a patient page
        """
        return '/mobile/patient/' in self.driver.current_url

    def is_stand_in_page(self):
        """
        Check that is on the stand in page
        :return: Boolean of if on stand in page
        """
        return '/mobile/patients/share' in self.driver.current_url


class LoginPageLocators(object):
    """
    A class to help locate stuff on the Login Page
    """
    username_el = (By.ID, 'username')
    password_el = (By.ID, 'password')
    login_button_el = (By.ID, 'loginbutton')
    database_dropdown_el = (By.ID, 'database')
    error_el = (By.CSS_SELECTOR, '.alert.alert-error')


class ListPageLocators(object):
    """
    A class to help locate stuff on the Task List Page
    """
    list_el = (By.CSS_SELECTOR, '.content > .tasklist')
    list_item_el = (By.CSS_SELECTOR, 'li > a.block')
    list_item_patient = (By.CSS_SELECTOR, 'div.task-right')
    list_item_patient_name = (By.TAG_NAME, 'strong')
    list_item_patient_trend = (By.TAG_NAME, 'i')
    list_item_patient_location = (By.TAG_NAME, 'em')
    list_item_deadline = (By.CSS_SELECTOR, 'div.task-right .aside')
    list_item_title = (By.CSS_SELECTOR, 'p.taskInfo')


class MenuLocators(object):
    """
    A class to help identify things in the menu
    """
    task_list_el = (By.ID, 'taskNavItem')
    patient_list_el = (By.ID, 'patientNavItem')
    stand_in_el = (By.LINK_TEXT, 'Stand In')
    barcode_scan_el = (By.CSS_SELECTOR, '.header-main li.scan_parent .scan')
    barcode_scan_input = (By.CSS_SELECTOR, '#patient_barcode .barcode_scan')
    logout_el = (By.CSS_SELECTOR, '.header-main li.logout .button')


class PatientPageLocators(object):
    """
    A class to help identify things on the patient page
    """
    adhoc_obs_menu_button = (By.CLASS_NAME, 'obs')
    open_obs_menu = (By.ID, 'obs_menu')
    open_obs_menu_title = (By.TAG_NAME, 'h2')
    open_obs_menu_list_items = (By.TAG_NAME, 'li')
    open_obs_menu_news_item = (By.CLASS_NAME, 'rightContent')
    open_obs_menu_news_item_deadline = (By.CLASS_NAME, 'aside')
    patient_info = (By.CSS_SELECTOR, '#obsButton h3.name')
    patient_name = (By.CSS_SELECTOR, '#obsButton h3.name strong')
    graph_tab_button = (By.CSS_SELECTOR,
                        '.content .block .tabs li:first-child a')
    table_tab_button = (By.CSS_SELECTOR,
                        '.content .block .tabs li:last-child a')
    graph_container = (By.ID, 'graph-content')
    table_container = (By.ID, 'table-content')
    graph_chart = (By.ID, 'chart')
    no_obs_in_chart = (By.CSS_SELECTOR, '#chart > h2')
    start_time_control = (By.ID, 'start_time')
    start_date_control = (By.ID, 'start_date')
    end_time_control = (By.ID, 'end_time')
    end_date_control = (By.ID, 'end_date')
    rangify_control = (By.ID, 'rangify')


class TaskPageLocators(object):
    """
    A class to help identify things on the task page
    """
    patient_name_container = (By.ID, 'patientName')
    patient_name_link = (By.CSS_SELECTOR, '#patientName > a')
    patient_name_info = (By.CSS_SELECTOR, '#patientName .icon-info')
    patient_info_popup = (By.ID, 'patient_info')
    patient_info_popup_title = (By.TAG_NAME, 'h2')
    patient_info_popup_fullscreen_button = (By.ID, 'patient_obs_fullscreen')
    patient_info_fullscreen = (By.CSS_SELECTOR, '.no-scroll > .full-modal')
    patient_info_fullscreen_iframe = (By.TAG_NAME, 'iframe')
    patient_info_fullscreen_close = (By.ID, 'closeFullModal')
    task_form = (By.ID, 'obsForm')
    task_form_task_id = (By.NAME, 'taskId')
    task_form_start_time = (By.ID, 'startTimestamp')
    task_form_submit = (By.ID, 'submitButton')
    task_form_input_field = (By.CLASS_NAME, 'obsField')
    task_form_field_label = (By.CSS_SELECTOR, '.input-header > label')
    task_form_field_input = (By.CSS_SELECTOR, '.input-header > input')
    task_form_field_select = (By.CSS_SELECTOR, '.input-body > select')
    task_form_field_errors = (By.CSS_SELECTOR, '.input-body > .errors')
    task_form_field_help = (By.CSS_SELECTOR, '.input-body > .help')
