from openeobs_mobile.data import DataDicts
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from erppeek import Client
from openeobs_mobile.locators import MenuLocators


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
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
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
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
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
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
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
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
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
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
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


    @staticmethod
    def add_no_risk_observation_for_patient(patient_id,
        database='openeobs_quality_assurance_db',
            user='nasir', password='nasir'):
        """
        Add an observation that gives no clinical risk
        :param patient_id: The patient to do observation for
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        ews_api = odoo_client.model('nh.clinical.patient.observation.ews')
        ews_activity_id = ews_api.create_activity({},
                                                  {'patient_id': patient_id})
        activity_api.submit(ews_activity_id, DataDicts.NO_RISK_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_low_risk_observation_for_patient(patient_id,
        database='openeobs_quality_assurance_db',
            user='nasir', password='nasir'):
        """
        Add an observation that gives low clinical risk
        :param patient_id: The patient to do observation for
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        ews_api = odoo_client.model('nh.clinical.patient.observation.ews')
        ews_activity_id = ews_api.create_activity({},
                                                  {'patient_id': patient_id})
        activity_api.submit(ews_activity_id, DataDicts.LOW_RISK_SCORE_1_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_three_in_one_observation_for_patient(patient_id,
        database='openeobs_quality_assurance_db',
            user='nasir', password='nasir'):
        """
        Add an observation that gives medium clinical risk due to 3in1
        :param patient_id: The patient to do observation for
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        ews_api = odoo_client.model('nh.clinical.patient.observation.ews')
        ews_activity_id = ews_api.create_activity({},
                                                  {'patient_id': patient_id})
        activity_api.submit(ews_activity_id,
                            DataDicts.MEDIUM_RISK_SCORE_4_THREE_IN_ONE_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_medium_risk_observation_for_patient(patient_id,
        database='openeobs_quality_assurance_db',
            user='nasir', password='nasir'):
        """
        Add an observation that gives medium clinical risk due to 3in1
        :param patient_id: The patient to do observation for
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        ews_api = odoo_client.model('nh.clinical.patient.observation.ews')
        ews_activity_id = ews_api.create_activity({},
                                                  {'patient_id': patient_id})
        activity_api.submit(ews_activity_id,
                            DataDicts.MEDIUM_RISK_SCORE_6_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_high_risk_observation_for_patient(patient_id,
        database='openeobs_quality_assurance_db',
            user='nasir', password='nasir'):
        """
        Add an observation that gives medium clinical risk due to 3in1
        :param patient_id: The patient to do observation for
        :param database: The database to do observation on
        :param user: User to carry out observation as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        ews_api = odoo_client.model('nh.clinical.patient.observation.ews')
        ews_activity_id = ews_api.create_activity({},
                                                  {'patient_id': patient_id})
        activity_api.submit(ews_activity_id,
                            DataDicts.HIGH_RISK_SCORE_11_EWS_DATA)
        activity_api.complete(ews_activity_id)

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
