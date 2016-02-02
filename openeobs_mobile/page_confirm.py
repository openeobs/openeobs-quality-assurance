"""Helper class to confirm user location"""
from openeobs_mobile.page_helpers import BasePage


class PageConfirm(BasePage):
    """
    Methods to confirm what page the user is currently on
    """
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
