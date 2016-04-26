"""Helpers for the login page"""
from selenium.webdriver.common.by import By

USERNAME_EL = (By.ID, 'username')
PASSWORD_EL = (By.ID, 'password')
LOGIN_BUTTON_EL = (By.ID, 'loginbutton')
LOGIN_BUTTON_DESKTOP = (By.CLASS_NAME, 'btn btn-primary')
DATABASE_DROPDOWN_EL = (By.ID, 'database')
ERROR_EL = (By.CSS_SELECTOR, '.alert.alert-error')
