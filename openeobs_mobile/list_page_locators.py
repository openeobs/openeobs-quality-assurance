"""Helpers for the list page"""
__author__ = 'amipatel'
from selenium.webdriver.common.by import By

LIST_EL = (By.CSS_SELECTOR, '.content > .tasklist')
LIST_ITEM_EL = (By.CSS_SELECTOR, 'li > a.block')
LIST_ITEM_PATIENT = (By.CSS_SELECTOR, 'div.task-right')
LIST_ITEM_PATIENT_NAME = (By.TAG_NAME, 'strong')
LIST_ITEM_PATIENT_TREND = (By.TAG_NAME, 'i')
LIST_ITEM_PATIENT_LOCATION = (By.TAG_NAME, 'em')
LIST_ITEM_DEADLINE = (By.CSS_SELECTOR, 'div.task-right .aside')
LIST_ITEM_TITLE = (By.CSS_SELECTOR, 'p.taskInfo')

STAND_IN_SELECT = (By.CSS_SELECTOR,
                   '#handover_form > ul > li:nth-child(2) > label > input')

STAND_IN_SHARE = (By.CSS_SELECTOR,
                  'body > div.share-footer > ul > li:nth-child(1) > a')

STAND_IN_LIST = (By.ID, 'assign_nurse')
STAND_IN_NURSE = (By.CSS_SELECTOR,
                  '#nurse_list > ul > li:nth-child(1) > input')

STAND_IN_NURSE_NAME = (By.CSS_SELECTOR,
                       '#nurse_list > ul > li:nth-child(1) > label')

STAND_IN_ASSIGN = (By.CSS_SELECTOR, '#assign_nurse > ul > li:nth-child(1) > a')

STAND_IN_ACCEPT_BUTTON = (By.CSS_SELECTOR,
                          'body > div.content > ul > li:nth-child(1) > '
                          'a > div > div.task-right > p')

STAND_IN_ACCEPT_CONFIRM = (By.CSS_SELECTOR,
                           '#accept_invite > ul > li:nth-child(3) > a')
STAND_IN_SUCCESS = (By.CSS_SELECTOR, '#invite_success > h2')
