from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """
    A class to help locate stuff on the Login Page
    """
    username_el = (By.ID, 'username')
    password_el = (By.ID, 'password')
    login_button_el = (By.ID, 'loginbutton')
    database_dropdown_el = (By.ID, 'database')
    error_el = (By.CSS_SELECTOR, '.alert.alert-error')


class ListPageLocators(object):
    """
    A class to help locate stuff on the Task List Page
    """
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
    stand_in_list = (By.CLASS_NAME, 'sharelist')
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


class MenuLocators(object):
    """
    A class to help identify things in the menu
    """
    task_list_el = (By.ID, 'taskNavItem')
    patient_list_el = (By.ID, 'patientNavItem')
    stand_in_el = (By.LINK_TEXT, 'Stand In')
    barcode_scan_el = (By.CSS_SELECTOR, '.header-main li.scan_parent .scan')
    barcode_scan_input = (By.CSS_SELECTOR, '#patient_barcode .barcode_scan')
    logout_el = (By.CSS_SELECTOR, '.header-main li.logout .button')


class PatientPageLocators(object):
    """
    A class to help identify things on the patient page
    """
    adhoc_obs_menu_button = (By.CLASS_NAME, 'obs')
    open_obs_menu = (By.ID, 'obs_menu')
    open_obs_menu_title = (By.TAG_NAME, 'h2')
    open_obs_menu_list_items = (By.TAG_NAME, 'li')
    open_obs_menu_news_item = (By.CSS_SELECTOR,
                               '#obs_menu > div > ul > li.rightContent')
    open_obs_menu_news_item_deadline = (By.CLASS_NAME, 'aside')
    open_obs_menu_gcs_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(2)')
    open_obs_menu_height_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(3)')
    open_obs_menu_weight_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(4)')
    open_obs_menu_blood_product_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(5)')
    open_obs_menu_blood_sugar_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(6)')
    open_obs_menu_bristol_stool_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(7)')
    open_obs_menu_postural_pressure_item = (
        By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(8)')
    patient_info = (By.CSS_SELECTOR, '#obsButton h3.name')
    patient_name = (By.CSS_SELECTOR, '#obsButton h3.name strong')
    graph_tab_button = (By.CSS_SELECTOR,
                        '.content .block .tabs li:first-child a')
    table_tab_button = (By.CSS_SELECTOR,
                        '.content .block .tabs li:last-child a')
    graph_container = (By.ID, 'graph-content')
    table_container = (By.ID, 'table-content')
    table_container_table = (By.CSS_SELECTOR, '#table-content table')
    graph_chart = (By.ID, 'chart')
    graph_chart_svg = (By.CSS_SELECTOR, '#chart svg')
    no_obs_in_chart = (By.CSS_SELECTOR, '#chart > h2')
    tabular_values_table = (By.CSS_SELECTOR, '#chart .nhtable')
    table_header = (By.TAG_NAME, 'th')
    table_row = (By.TAG_NAME, 'tr')
    table_data = (By.TAG_NAME, 'td')
    start_time_control = (By.ID, 'start_time')
    start_date_control = (By.ID, 'start_date')
    end_time_control = (By.ID, 'end_time')
    end_date_control = (By.ID, 'end_date')
    rangify_control = (By.ID, 'rangify')
    chart_context_graph = (By.CSS_SELECTOR, '.nhcontext .nhgraph')
    chart_focus_graphs = (By.CSS_SELECTOR, '.nhfocus .nhgraph')
    chart_graph_label = (By.CSS_SELECTOR, '.background .label')
    chart_graph_measurement = (By.CSS_SELECTOR, '.background .measurement')


class TaskPageLocators(object):
    """
    A class to help identify things on the task page
    """
    patient_name_container = (By.ID, 'patientName')
    patient_name_link = (By.CSS_SELECTOR, '#patientName > a')
    patient_name_info = (By.CSS_SELECTOR, '#patientName .icon-info')
    patient_info_popup = (By.ID, 'patient_info')
    patient_info_popup_title = (By.TAG_NAME, 'h2')
    patient_info_popup_fullscreen_button = (By.ID, 'patient_obs_fullscreen')
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
