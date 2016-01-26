from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.locators import ListPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui

class StandInPage(BasePage):

    def submit_stand_in(self):
        """
        Select a patient to share with a nurse
        :return: The name of the nurse who is receiving the patient
        """
        self.driver.find_element(*ListPageLocators.stand_in_select).click()
        self.driver.find_element(*ListPageLocators.stand_in_share).click()

        ui.WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(
                    ListPageLocators.stand_in_nurse)).click()

        nurses = self.driver.find_element(*ListPageLocators.stand_in_list)
        nurses.find_elements_by_tag_name('input')[0].click()

        nurse_name = self.driver.find_element(
                *ListPageLocators.stand_in_nurse_name).text

        ui.WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(
                    ListPageLocators.stand_in_assign)).click()

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
                    ListPageLocators.stand_in_accept_button)).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    ListPageLocators.stand_in_accept_confirm)).click()

        response = ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(
                    ListPageLocators.stand_in_success))

        return response