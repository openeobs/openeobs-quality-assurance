"""Helpers for the observation form page"""
from selenium.webdriver.common.by import By

SCORED_SUBMIT_CONFIRM_DIALOG = (By.ID, 'submit_observation')
SUBMIT_SUCCESS_DIALOG = (By.ID, 'submit_success')
OPTION_BUTTONS = (By.CSS_SELECTOR, '.dialog > .options > li > a')
SUBMIT_OPTION = (
    By.CSS_SELECTOR, '.dialog > .options > li > a[@data-action="submit"]')
RENABLE_OPTION = (
    By.CSS_SELECTOR, '.dialog > .options > li > a[@data-action="renable"]')
TASK_LIST_OPTION = (
    By.CSS_SELECTOR, '.dialog > .options > li > a[@data-action="confirm"]')
ESCALATION_TASK_OPTION = (
    By.CSS_SELECTOR, '#submit_success > options > li:last-child > a')
