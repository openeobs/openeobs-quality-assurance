"""Creates a list of patients or tasks """
from openeobs_mobile import list_page_locators
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
        list_items = self.driver.find_element(*list_page_locators.LIST_EL)
        return list_items.find_elements(*list_page_locators.LIST_ITEM_EL)
