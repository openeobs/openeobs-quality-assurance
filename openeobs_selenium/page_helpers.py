from selenium.webdriver.common.by import By


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

    def do_barcode_scan(self, patient_id):
        """
        Carry out a barcode scan with the patient id
        :param patient_id:
        """
        scan_item = self.driver.find_element(*MenuLocators.barcode_scan_el)
        # TODO: Implement this
        scan_item.click()

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


class LoginPageLocators(object):
    """
    A class to help locate stuff on the Login Page
    """
    username_el = (By.ID, 'username')
    password_el = (By.ID, 'password')
    login_button_el = (By.ID, 'loginbutton')
    database_dropdown_el = (By.ID, 'database')
    error_el = (By.CSS_SELECTOR, '.alert.alert-error')


class ListPageLocators(object):
    """
    A class to help locate stuff on the Task List Page
    """
    list_el = (By.CSS_SELECTOR, '.content > .tasklist')
    list_item_el = (By.CSS_SELECTOR, 'li > a.block')
    list_item_patient = (By.CSS_SELECTOR, 'div.task-right')
    list_item_patient_name = (By.TAG_NAME, 'strong')
    list_item_patient_trend = (By.TAG_NAME, 'i')
    list_item_patient_location = (By.TAG_NAME, 'em')
    list_item_deadline = (By.CSS_SELECTOR, 'div.task-left')
    list_item_title = (By.CSS_SELECTOR, 'p.taskInfo')


class MenuLocators(object):
    """
    A class to help identify things in the menu
    """
    task_list_el = (By.ID, 'taskNavItem')
    patient_list_el = (By.ID, 'patientNavItem')
    stand_in_el = (By.LINK_TEXT, 'Stand In')
    barcode_scan_el = (By.CSS_SELECTOR, '.header-main li.scan_parent .scan')
    logout_el = (By.CSS_SELECTOR, '.header-main li.logout .button')
