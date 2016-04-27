"""Helpers for the desktop interface"""

from selenium.webdriver.common.by import By

DESKTOP_TITLE = (By.CLASS_NAME, 'oe_view_title')
KANBAN_BOARD = (By.CLASS_NAME, 'oe_view_manager_wrapper')
KANBAN_ITEMS = (By.CLASS_NAME, 'oe_kanban_content')
PATIENT_RECORD = (By.CLASS_NAME, 'oe_form_sheetbg')
ADMISSION_DETAILS = (By.ID, 'ui-id-1')
DEMOGRAPHICS = (By.ID, 'ui-id-2')
OTHER_OBS = (By.ID, 'ui-id-3')
DEVICES = (By.ID, 'ui-id-4')
MONITORING = (By.ID, 'ui-id-5')
HEIGHT = (By.CSS_SELECTOR, '.oe_form_field_float.nhc_selenium_height')
WEIGHT = (By.CSS_SELECTOR, 'nhc_selenium_weight > td')
