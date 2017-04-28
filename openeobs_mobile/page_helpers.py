"""Helper methods for different types of pages"""

from selenium.webdriver.common.by import By
from openeobs_mobile.data import NO_RISK_EWS_DATA, LOW_RISK_SCORE_1_EWS_DATA, \
    HIGH_RISK_SCORE_11_EWS_DATA, MEDIUM_RISK_SCORE_6_EWS_DATA, \
    MEDIUM_RISK_SCORE_4_THREE_IN_ONE_EWS_DATA
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from erppeek import Client
from openeobs_mobile.menu_locators import PATIENT_LIST_EL, TASK_LIST_EL, \
    STAND_IN_EL, LOGOUT_EL, BARCODE_SCAN_EL, BARCODE_SCAN_INPUT


class BasePage(object):
    """
        Base class to initialise the base page
        that will be called from all pages
    """
    def __init__(self, driver):
        self.driver = driver

    def go_to_task_list(self):
        """
            Navigate to the task list
        """
        task_list_item = self.driver.find_element(*TASK_LIST_EL)
        task_list_item.click()
        ui.WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                (By.CSS_SELECTOR, '#taskNavItem.selected'))
        )

    def go_to_patient_list(self):
        """
            Navigate to the patient list
        """
        patient_list_item = self.driver.find_element(
            *PATIENT_LIST_EL)
        patient_list_item.click()
        ui.WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                (By.CSS_SELECTOR, '#patientNavItem.selected'))
        )

    def logout(self):
        """
            Log out of the app
        """
        logout = self.driver.find_element(*LOGOUT_EL)
        logout.click()

    def go_to_standin(self):
        """
            Go to the stand in page
        """
        standin_item = self.driver.find_element(*STAND_IN_EL)
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
        odoo_client = Client('http://localhost:8069', db=database, user=user,
                             password=password)
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
            patient_id, database='openeobs_quality_assurance_db', user='admin',
            password='admin'):
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
    def remove_tasks_for_patient(patient_id,
                                 activity_models=[],
                                 database='openeobs_quality_assurance_db',
                                 user='admin', password='admin'):
        """
        Remove a specific task for a patient
        :param patient_id: The patient to remove tasks for
        :param activity_models: The activity model to remove
        :param database: database to run against
        :param user: the username to run as
        :param password: password for username
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)
        activity_api = odoo_client.model('nh.activity')
        spells = activity_api.search([
            ['state', '=', 'started'],
            ['data_model', '=', 'nh.clinical.spell'],
            ['patient_id', '=', patient_id]
        ])
        activities = activity_api.search([
            ['data_model', 'in', activity_models],
            ['parent_id', 'in', spells]
        ])
        activity_api.unlink(activities)

    @staticmethod
    def add_no_risk_observation(
            patient_id, database='openeobs_quality_assurance_db', user='nasir',
            password='nasir'):
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
        activity_api.submit(ews_activity_id, NO_RISK_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_low_risk_observation(
            patient_id, database='openeobs_quality_assurance_db', user='nasir',
            password='nasir'):
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
        activity_api.submit(ews_activity_id,
                            LOW_RISK_SCORE_1_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_three_in_one_observation(
            patient_id, database='openeobs_quality_assurance_db', user='nasir',
            password='nasir'):
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
                            MEDIUM_RISK_SCORE_4_THREE_IN_ONE_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_medium_risk_observation(
            patient_id, database='openeobs_quality_assurance_db', user='nasir',
            password='nasir'):
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
                            MEDIUM_RISK_SCORE_6_EWS_DATA)
        activity_api.complete(ews_activity_id)

    @staticmethod
    def add_high_risk_observation(
            patient_id, database='openeobs_quality_assurance_db', user='nasir',
            password='nasir'):
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
                            HIGH_RISK_SCORE_11_EWS_DATA)
        activity_api.complete(ews_activity_id)

    def do_barcode_scan(self, patient_id):
        """
        Carry out a barcode scan with the patient id
        :param patient_id:
        """
        scan_item = self.driver.find_element(*BARCODE_SCAN_EL)
        scan_item.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.ID, 'patient_barcode')))

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                (By.CSS_SELECTOR, '#patient_barcode .barcode_scan')))
        try:
            barcode_input = \
                self.driver.find_element(*BARCODE_SCAN_INPUT)
            self.driver.execute_script(
                "var scan = document.getElementsByName('barcode_scan')[0]; "
                "scan.setAttribute('value', ',{0},'); "
                "scan.textContent = ',{0},';".format(patient_id)
            )
            barcode_input.send_keys(Keys.ENTER)
            ui.WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.TAG_NAME, 'dl')))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    @staticmethod
    def add_stand_in(database='openeobs_quality_assurance_db', user='nat',
                     password='nat'):
        """
        Add a stand in task
        :param database: The database to do stand in on
        :param user: User to create stand in as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)

        activity_api = odoo_client.model('nh.activity')
        ews_api = odoo_client.model('nh.clinical.patient.follow')
        user_pool = odoo_client.model('res.users')
        nurse_id = user_pool.search([
            ['login', '=', 'nasir'],
            ])
        ews_activity_id = ews_api.create_activity({'user_id': nurse_id[0]}, {
            'patient_ids': [[6, 0, [4]]]})

        activity_api.submit(ews_activity_id, {})

        return ews_activity_id

    @staticmethod
    def complete_stand_in(task_id, database='openeobs_quality_assurance_db',
                          user='nasir', password='nasir'):
        """
        Complete a stand in task
        :param database: The database to complete stand in on
        :param user: User to complete stand in as
        :param password: Password for the user
        """
        odoo_client = Client('http://localhost:8069', db=database,
                             user=user, password=password)

        activity_api = odoo_client.model('nh.activity')
        activity_api.complete(task_id)
