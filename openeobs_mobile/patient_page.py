"""Methods for the patient page"""

from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.task_page_locators import TASK_FORM_SUBMIT, TASK_FORM
from openeobs_mobile.patient_page_locators import ADHOC_OBS_MENU_BUTTON, \
    OPEN_OBS_MENU, GRAPH_CHART, TABLE_TAB_BUTTON, GRAPH_TAB_BUTTON, \
    GRAPH_CHART_SVG, TABULAR_VALUES_TABLE, TABLE_CONTAINER, TABLE_DATA, \
    TABLE_ROW, TABLE_HEADER
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class PatientPage(BasePage):
    """
    Patient Page methods and helps etc
    """

    def open_adhoc_obs_menu(self):
        """
        Open up the adhoc observation menu
        """
        obs_button = self.driver.find_element(
            *ADHOC_OBS_MENU_BUTTON
        )
        obs_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.ID, 'obs_menu'))
        )
        return self.driver.find_element(*OPEN_OBS_MENU)

    def adhoc_obs_menu_is_open(self):
        """
        Check that adhoc obs menu is up
        :return: Boolean of if the menu is open or not
        """
        try:
            self.driver.find_element(
                *OPEN_OBS_MENU
            )
        except NoSuchElementException:
            return False
        return True

    def has_no_patient_data(self):
        """
        Check that the patient's record shows data
        :return: Boolean if error message is shown or not
        """
        chart = self.driver.find_element(*GRAPH_CHART)
        return chart.text == 'No observation data available for patient'

    def tabs_are_shown(self):
        """
        Check that the tabs are visible
        :return: Boolean of if the tabs are visible or not
        """
        try:
            self.driver.find_element(
                *TABLE_TAB_BUTTON
            )
            self.driver.find_element(
                *GRAPH_TAB_BUTTON
            )
        except NoSuchElementException:
            return False
        return True

    def chart_is_shown(self):
        """
        Check that the chart is visible
        :return: Boolean of if the tabs are visible or not
        """
        try:
            self.driver.find_element(
                *GRAPH_CHART_SVG
            )
        except NoSuchElementException:
            return False
        return True

    def tabular_values_are_shown(self):
        """
        Check that the tabular values table is shown
        :return: Boolean of if the tabular values table is shown
        """
        try:
            self.driver.find_element(
                *TABULAR_VALUES_TABLE
            )
        except NoSuchElementException:
            return False
        return True

    def obs_table_is_shown(self):
        """
        Check that the obs table is shown
        :return: Boolean of if the obs table is shown
        """
        try:
            self.driver.find_element(
                *TABLE_CONTAINER
            )
        except NoSuchElementException:
            return False
        return True

    def change_to_table(self):
        """
        Change the tabs so shows the table
        """
        tab = self.driver.find_element(
            *TABLE_TAB_BUTTON
        )
        tab.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#table-content table'))
        )

    def get_tabular_values(self):
        """
        Get tabular values table
        :return: tabular values WebElement
        """
        return self.driver.find_element(
            *TABULAR_VALUES_TABLE
        )

    @staticmethod
    def get_table_headers(table):
        """
        Get the table headers for the supplied table
        :param table: A table to get headers from
        :return: A list of table header strings
        """
        headers = table.find_elements(
            *TABLE_HEADER
        )
        return [header.text for header in headers]

    @staticmethod
    def get_table_data(table_row):
        """
        Get the table data for the supplied table row
        :param table_row: A row in the table to get data from
        :return: A list of table data strings
        """
        data = table_row.find_elements(
            *TABLE_DATA
        )
        return [entry.text for entry in data]

    @staticmethod
    def get_table_rows(table):
        """
        Get the table rows for the supplied table
        :param table: A table to get rows from
        :return: A list of table rows
        """
        rows = table.find_elements(
            *TABLE_ROW
        )
        return rows

    def get_obs_table(self):
        """
        Get observation table table
        :return: tabular values WebElement
        """
        return self.driver.find_element(
            *TABLE_CONTAINER
        )

    @staticmethod
    def select_patient(patients):
        """
        Select a patient to observe
        :param patients: a list of patients
        """
        patient_to_test = patients[0]
        patient_to_test.click()

    def open_form(self, form_id):
        """
        Open an observation form
        :param form_id: The type of observation
        """
        self.open_adhoc_obs_menu()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(form_id)
        )

        self.driver.find_element(*form_id).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(TASK_FORM)
        )

    def enter_obs_data(self, data):
        """
        Enter data into an observation form
        :param data: The data to be entered
        """
        if 'oxygen_administration_flag' in data:
            oxy = self.driver.find_element_by_name('oxygen_administration_flag')
            oxy.send_keys(data['oxygen_administration_flag'])
            oxy.send_keys(Keys.TAB)

            if 'device_id' in data:
                device = self.driver.find_element_by_name('device_id')
                device.send_keys(data['device_id'])
                device.send_keys(Keys.TAB)

        for field, value in data.iteritems():
            input_field = self.driver.find_element_by_name(field)
            input_field.send_keys(value)
            input_field.send_keys(Keys.TAB)

        self.driver.find_element(
                *TASK_FORM_SUBMIT).click()
