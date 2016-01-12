from openeobs_selenium.page_helpers import BasePage, ListPageLocators


class TaskListPage(BasePage):
    """
    Login Page methods and helps etc
    """

    def is_task_list_page(self):
        """
        Check that the page's title matches that of the login page
        :return: Boolean of if the title matches or not
        """
        return '/mobile/tasks' in self.driver.current_url

    def get_task_list_items(self):
        """
        Return a list of items in the task list
        :return: A list of elements in the task list
        """
        task_list = self.driver.find_element(*ListPageLocators.list_el)
        return task_list.find_elements(*ListPageLocators.list_item_el)