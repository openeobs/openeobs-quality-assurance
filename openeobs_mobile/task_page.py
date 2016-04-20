"""Methods for the task page"""
from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.task_page_locators import PATIENT_NAME_INFO, \
    PATIENT_INFO_POPUP_FSCREEN_BTN, PATIENT_INFO_POPUP, \
    PATIENT_INFO_FULLSCREEN, CANCEL_SUBMIT, CONFIRM_CANCEL, \
    SUCCESSFUL_CANCEL, TASK_FORM_SUBMIT, SUCCESSFUL_SUBMIT
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TaskPage(BasePage):
    """
    Task Page methods and interactions
    """
    def open_patient_info(self):
        """
        Open up the adhoc observation menu
        """
        info_button = self.driver.find_element(*PATIENT_NAME_INFO)
        info_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.ID, 'patient_info'))
        )
        return self.driver.find_element(*PATIENT_INFO_POPUP)

    def open_full_patient_obs_data(self):
        """
        Open up the full patient obs data modal
        """
        popup = self.open_patient_info()
        full_obs_button = popup.find_element(
            *PATIENT_INFO_POPUP_FSCREEN_BTN
        )
        full_obs_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.no-scroll > .full-modal'))
        )
        return self.driver.find_element(
            *PATIENT_INFO_FULLSCREEN
        )

    def fullscreen_not_open(self):
        """
        Check full screen isn't open
        """
        try:
            self.driver.find_element(
                *PATIENT_INFO_FULLSCREEN
            )
        except NoSuchElementException:
            return True
        return False

    def open_clinical(self, task_id, patient_list_page):
        """
        Create a clinical notification for a patient, and then open it
        """
        PatientPage(self.driver).add_medium_risk_observation(int(task_id))
        patient_list_page.go_to_task_list()
        tasks = patient_list_page.get_list_items()
        clinical_task = tasks[0]
        clinical_task.click()

    def confirm_clinical(self):
        """
        Confirm a clinical notification
        """
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(TASK_FORM_SUBMIT)
        )

        self.driver.find_element(*TASK_FORM_SUBMIT).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(SUCCESSFUL_SUBMIT)
        )

        response = self.driver.find_element(*SUCCESSFUL_SUBMIT).text
        return response

    def cancel_clinical(self):
        """
        Cancel a clinical notification
        """
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(CANCEL_SUBMIT)
        )

        self.driver.find_element(*CANCEL_SUBMIT).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(CONFIRM_CANCEL)
        )

        self.driver.find_element(*CONFIRM_CANCEL).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(SUCCESSFUL_CANCEL)
        )
        response = self.driver.find_element(*SUCCESSFUL_CANCEL).text

        return response
