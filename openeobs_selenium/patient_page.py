from openeobs_selenium.page_helpers import BasePage, PatientPageLocators
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


class PatientPage(BasePage):
    """
    Login Page methods and helps etc
    """

    def open_adhoc_obs_menu(self):
        """
        Open up the adhoc observation menu
        """
        obs_button = self.driver.find_element(
            *PatientPageLocators.adhoc_obs_menu_button
        )
        obs_button.click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.ID, 'obs_menu'))
        )
        return self.driver.find_element(*PatientPageLocators.open_obs_menu)

    def has_patient_data(self):
        """
        Check that the patient's record shows data
        :return: Boolean if error message is shown or not
        """
        chart = self.driver.find_element(*PatientPageLocators.graph_chart)
        return chart.text == 'No observation data available for patient'
