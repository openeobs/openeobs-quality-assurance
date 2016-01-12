from selenium.webdriver.common.by import By


class BasePage(object):
    """
    Base class to initialise the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver


class LoginPageLocators(object):
    """
    A class to help locate stuff on the Login Page
    """
    username_el = (By.ID, 'username')
    password_el = (By.ID, 'password')
    login_button_el = (By.ID, 'loginbutton')
    database_dropdown_el = (By.ID, 'database')
    error_el = (By.CSS_SELECTOR, '.alert.alert-error')
