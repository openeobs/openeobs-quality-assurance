"""Helpers for the menu page"""
from selenium.webdriver.common.by import By

TASK_LIST_EL = (By.ID, 'taskNavItem')
PATIENT_LIST_EL = (By.ID, 'patientNavItem')
STAND_IN_EL = (By.LINK_TEXT, 'Stand In')
BARCODE_SCAN_EL = (By.CSS_SELECTOR, '.header-main li.scan_parent .scan')
BARCODE_SCAN_INPUT = (By.CSS_SELECTOR, '#patient_barcode .barcode_scan')
LOGOUT_EL = (By.CSS_SELECTOR, '.header-main li.logout .button')
SERVER_ERROR = (By.ID, 'data_error')
