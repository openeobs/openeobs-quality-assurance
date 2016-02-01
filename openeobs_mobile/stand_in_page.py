"""Methods for the stand-in page"""
from openeobs_mobile import list_page_locators

from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.page_helpers import BasePage
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


class StandInPage(BasePage):
    """
    Standin Page methods and helps etc
    """

    def submit_stand_in(self):
        """
        Select a patient to share with a nurse
        :return: The name of the nurse who is receiving the patient
        """
        self.driver.find_element(*list_page_locators.stand_in_select).click()
        self.driver.find_element(*list_page_locators.stand_in_share).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                list_page_locators.stand_in_list))

        self.driver.find_element(*list_page_locators.stand_in_nurse).click()
        nurse_name = \
            self.driver.find_element(*list_page_locators.stand_in_nurse_name).text

        self.driver.find_element(*list_page_locators.stand_in_assign).click()

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
                list_page_locators.stand_in_accept_button))
        self.driver.find_element(*
                                 list_page_locators
                                 .stand_in_accept_button).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                list_page_locators.stand_in_accept_confirm))
        self.driver.find_element(*
                                 list_page_locators
                                 .stand_in_accept_confirm).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                list_page_locators.stand_in_success))
        response = self.driver.find_element(*list_page_locators.stand_in_success)
        return response
