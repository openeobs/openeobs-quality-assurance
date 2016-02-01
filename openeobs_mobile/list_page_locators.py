__author__ = 'amipatel'
from selenium.webdriver.common.by import By

list_el = (By.CSS_SELECTOR, '.content > .tasklist')
list_item_el = (By.CSS_SELECTOR, 'li > a.block')
list_item_patient = (By.CSS_SELECTOR, 'div.task-right')
list_item_patient_name = (By.TAG_NAME, 'strong')
list_item_patient_trend = (By.TAG_NAME, 'i')
list_item_patient_location = (By.TAG_NAME, 'em')
list_item_deadline = (By.CSS_SELECTOR, 'div.task-right .aside')
list_item_title = (By.CSS_SELECTOR, 'p.taskInfo')
stand_in_select = (
    By.CSS_SELECTOR,
    '#handover_form > ul > li:nth-child(2) > label > input')
stand_in_share = (
    By.CSS_SELECTOR, 'body > div.share-footer > ul > li:nth-child(1) > a')
stand_in_list = (By.ID, 'assign_nurse')
stand_in_nurse = (
    By.CSS_SELECTOR, '#nurse_list > ul > li:nth-child(1) > input')
stand_in_nurse_name = (
    By.CSS_SELECTOR, '#nurse_list > ul > li:nth-child(1) > label')
stand_in_assign = (
    By.CSS_SELECTOR, '#assign_nurse > ul > li:nth-child(1) > a')
stand_in_accept_button = (
    By.CSS_SELECTOR,
    'body > div.content > ul > li:nth-child(1) > '
    'a > div > div.task-right > p')
stand_in_accept_confirm = (
    By.CSS_SELECTOR, '#accept_invite > ul > li:nth-child(3) > a')
stand_in_success = (By.CSS_SELECTOR, '#invite_success > h2')