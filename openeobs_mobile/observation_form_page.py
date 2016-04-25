from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.task_page_locators import TASK_FORM_SUBMIT
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


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

        self.driver.find_element(*TASK_FORM_SUBMIT).click()
