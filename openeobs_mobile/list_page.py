"""Creates a list of patients or tasks """
from openeobs_mobile import list_page_locators
from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile import task_page_locators


class ListPage(BasePage):
    """
    List Page methods and helps etc
    """

    def get_list_items(self):
        """
        Return a list of items in the task list
        :return: A list of elements in the task list
        """
        list_items = self.driver.find_element(*list_page_locators.LIST_EL)
        return list_items.find_elements(*list_page_locators.LIST_ITEM_EL)

    def get_list_task(self):
        """
        Returns list of tasks
        :return: A list of tasks
        """
        task_items = self.driver.find_elements(*task_page_locators.TASK)
        return task_items
