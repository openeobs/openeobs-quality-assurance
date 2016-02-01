"""Creates a list of patients or tasks """
from openeobs_mobile import ListPageLocators
from openeobs_mobile.page_helpers import BasePage


class ListPage(BasePage):

    """
    List Page methods and helps etc
    """

    def get_list_items(self):
        """
        Return a list of items in the task list
        :return: A list of elements in the task list
        """
        list_items = self.driver.find_element(*ListPageLocators.list_el)
        return list_items.find_elements(*ListPageLocators.list_item_el)
