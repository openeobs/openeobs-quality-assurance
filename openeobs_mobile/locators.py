"""Locators for elements on mobile pages"""
from selenium.webdriver.common.by import By


# class ListPageLocators(object):
#     """
#     A class to help locate stuff on the Task List Page
#     """
#     list_el = (By.CSS_SELECTOR, '.content > .tasklist')
#     list_item_el = (By.CSS_SELECTOR, 'li > a.block')
#     list_item_patient = (By.CSS_SELECTOR, 'div.task-right')
#     list_item_patient_name = (By.TAG_NAME, 'strong')
#     list_item_patient_trend = (By.TAG_NAME, 'i')
#     list_item_patient_location = (By.TAG_NAME, 'em')
#     list_item_deadline = (By.CSS_SELECTOR, 'div.task-right .aside')
#     list_item_title = (By.CSS_SELECTOR, 'p.taskInfo')
#     stand_in_select = (
#         By.CSS_SELECTOR,
#         '#handover_form > ul > li:nth-child(2) > label > input')
#     stand_in_share = (
#         By.CSS_SELECTOR, 'body > div.share-footer > ul > li:nth-child(1) > a')
#     stand_in_list = (By.ID, 'assign_nurse')
#     stand_in_nurse = (
#         By.CSS_SELECTOR, '#nurse_list > ul > li:nth-child(1) > input')
#     stand_in_nurse_name = (
#         By.CSS_SELECTOR, '#nurse_list > ul > li:nth-child(1) > label')
#     stand_in_assign = (
#         By.CSS_SELECTOR, '#assign_nurse > ul > li:nth-child(1) > a')
#     stand_in_accept_button = (
#         By.CSS_SELECTOR,
#         'body > div.content > ul > li:nth-child(1) > '
#         'a > div > div.task-right > p')
#     stand_in_accept_confirm = (
#         By.CSS_SELECTOR, '#accept_invite > ul > li:nth-child(3) > a')
#     stand_in_success = (By.CSS_SELECTOR, '#invite_success > h2')


class TaskPageLocators(object):
    """
    A class to help identify things on the task page
    """
    patient_name_container = (By.ID, 'patientName')
    patient_name_link = (By.CSS_SELECTOR, '#patientName > a')
    patient_name_info = (By.CSS_SELECTOR, '#patientName .icon-info')
    patient_info_popup = (By.ID, 'patient_info')
    patient_info_popup_title = (By.TAG_NAME, 'h2')
    patient_info_popup_fscreen_btn = (By.ID, 'patient_obs_fullscreen')
    patient_info_fullscreen = (By.CSS_SELECTOR, '.no-scroll > .full-modal')
    patient_info_fullscreen_iframe = (By.TAG_NAME, 'iframe')
    patient_info_fullscreen_close = (By.ID, 'closeFullModal')
    task_form = (By.ID, 'obsForm')
    task_form_task_id = (By.NAME, 'taskId')
    task_form_start_time = (By.ID, 'startTimestamp')
    task_form_submit = (By.ID, 'submitButton')
    task_form_input_field = (By.CLASS_NAME, 'obsField')
    task_form_field_label = (By.CSS_SELECTOR, '.input-header > label')
    task_form_field_input = (By.CSS_SELECTOR, '.input-header > input')
    task_form_field_select = (By.CSS_SELECTOR, '.input-body > select')
    task_form_field_errors = (By.CSS_SELECTOR, '.input-body > .errors')
    task_form_field_help = (By.CSS_SELECTOR, '.input-body > .help')
    confirm_submit = (
        By.CSS_SELECTOR, '#submit_observation > ul > li:nth-child(2)')
    successful_submit = (By.CSS_SELECTOR, '#submit_success > h2')
    related_task = (By.CSS_SELECTOR, '#submit_success > div > p')
