from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.task_page_locators import TASK_FORM_SUBMIT
from openeobs_mobile.observation_form_locators import \
    SCORED_SUBMIT_CONFIRM_DIALOG, SUBMIT_OPTION, RENABLE_OPTION, \
    SUBMIT_SUCCESS_DIALOG, TASK_LIST_OPTION, ESCALATION_TASK_OPTION
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


class ObservationFormPage(BasePage):
    def enter_obs_data(self, data):
        """
        Enter data into an observation form
        :param data: The data to be entered
        """
        for field in data:
            value = field.get('value')
            name = field.get('name')
            data_type = field.get('type')
            
            if data_type == 'select':
                select_field = self.driver.find_element_by_name(name)
                select_select = Select(select_field)
                select_select.select_by_visible_text(value)
                select_field.send_keys(Keys.TAB)
            else:
                input_field = self.driver.find_element_by_name(name)
                input_field.send_keys(value)
                input_field.send_keys(Keys.TAB)

        form_submit_button = self.driver.find_element(*TASK_FORM_SUBMIT)
        form_submit_button.click()

    def confirm_submit_scored_ob(self):
        """
        Wait for and submit a scored observation
        """
        ui.WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SCORED_SUBMIT_CONFIRM_DIALOG)
        )
        submit_button = self.driver.find_element(*SUBMIT_OPTION)
        submit_button.click()
        ui.WebDriverWait(self.driver, 10).until_not(
            ec.presence_of_element_located(SCORED_SUBMIT_CONFIRM_DIALOG)
        )

    def close_submit_scored_ob(self):
        """
        Wait for and submit a scored observation
        """
        ui.WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SCORED_SUBMIT_CONFIRM_DIALOG)
        )
        submit_button = self.driver.find_element(*RENABLE_OPTION)
        submit_button.click()
        ui.WebDriverWait(self.driver, 10).until_not(
            ec.presence_of_element_located(SCORED_SUBMIT_CONFIRM_DIALOG)
        )

    def take_escalation_task(self):
        """
        Wait for post submit dialog and press the button to load the escalation
        task 
        """
        ui.WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SUBMIT_SUCCESS_DIALOG)
        )
        submit_button = self.driver.find_element(*ESCALATION_TASK_OPTION)
        submit_button.click()
        ui.WebDriverWait(self.driver, 10).until_not(
            ec.presence_of_element_located(SUBMIT_SUCCESS_DIALOG)
        )

    def back_to_task_list(self):
        """
        Wait for post submit dialog and press the button to go back to
        the task list
        """
        ui.WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SUBMIT_SUCCESS_DIALOG)
        )
        submit_button = self.driver.find_element(*TASK_LIST_OPTION)
        submit_button.click()
        ui.WebDriverWait(self.driver, 10).until_not(
            ec.presence_of_element_located(SUBMIT_SUCCESS_DIALOG)
        )
