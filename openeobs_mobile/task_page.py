from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.page_helpers import BasePage, TaskPageLocators, \
    ListPageLocators
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
        info_button = self.driver.find_element(
            *TaskPageLocators.patient_name_info
        )
        info_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.ID, 'patient_info'))
        )
        return self.driver.find_element(*TaskPageLocators.patient_info_popup)

    def open_patient_obs_data_fullscreen(self):
        """
        Open up the full patient obs data modal
        """
        popup = self.open_patient_info()
        full_obs_button = popup.find_element(
            *TaskPageLocators.patient_info_popup_fullscreen_button
        )
        full_obs_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.no-scroll > .full-modal'))
        )
        return self.driver.find_element(
            *TaskPageLocators.patient_info_fullscreen
        )

    def fullscreen_not_open(self):
        """
        Check full screen isn't open
        """
        try:
            self.driver.find_element(
                *TaskPageLocators.patient_info_fullscreen
            )
        except NoSuchElementException:
            return True
        return False

    def submit_stand_in(self):
        """
        Select a patient to share with a nurse
        :return: The name of the nurse who is receiving the patient
        """
        self.driver.find_element(*ListPageLocators.stand_in_select).click()
        self.driver.find_element(*ListPageLocators.stand_in_share).click()

        ui.WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(
                    (ListPageLocators.stand_in_nurse))).click()

        nurses = self.driver.find_element(*ListPageLocators.stand_in_list)
        nurses.find_elements_by_tag_name('input')[0].click()

        nurse_name = self.driver.find_element(
                *ListPageLocators.stand_in_nurse_name).text

        ui.WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(
                    (ListPageLocators.stand_in_assign))).click()

        return nurse_name

    def confirm_stand_in(self, nurse, task_list):
        """
        Accept a shared patient from another nurse
        :param nurse: the nurse who has received the patient request
        :param task_list: the task list object
        :return response: The submission response
        """
        self.driver.get('http://localhost:8069/mobile/login')
        LoginPage(self.driver).login(nurse, nurse)

        task_list.go_to_patient_list()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    (ListPageLocators.stand_in_accept_button))).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    (ListPageLocators.stand_in_accept_confirm))).click()

        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    (ListPageLocators.stand_in_success)))

        return response