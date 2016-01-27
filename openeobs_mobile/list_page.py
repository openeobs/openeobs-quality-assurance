from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.locators import ListPageLocators


class ListPage(BasePage):

    """
    Login Page methods and helps etc
    """

    def get_list_items(self):
        """
        Return a list of items in the task list
        :return: A list of elements in the task list
        """
        list = self.driver.find_element(*ListPageLocators.list_el)
        return list.find_elements(*ListPageLocators.list_item_el)
