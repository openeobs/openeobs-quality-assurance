"""Helpers for the list page"""

from selenium.webdriver.common.by import By

LIST_EL = (By.CSS_SELECTOR, '.content > .tasklist')
LIST_ITEM_EL = (By.CSS_SELECTOR, 'li > a.block')
LIST_ITEM_PATIENT = (By.CSS_SELECTOR, 'div.task-right')
LIST_ITEM_PATIENT_NAME = (By.TAG_NAME, 'strong')
LIST_ITEM_PATIENT_TREND = (By.TAG_NAME, 'i')
LIST_ITEM_PATIENT_LOCATION = (By.TAG_NAME, 'em')
LIST_ITEM_DEADLINE = (By.CSS_SELECTOR, 'div.task-right .aside')
LIST_ITEM_TITLE = (By.CSS_SELECTOR, 'p.taskInfo')
