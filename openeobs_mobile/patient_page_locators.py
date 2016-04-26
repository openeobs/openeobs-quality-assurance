"""Helpers for the patient page"""

from selenium.webdriver.common.by import By

ADHOC_OBS_MENU_BUTTON = (By.CLASS_NAME, 'obs')
OPEN_OBS_MENU = (By.ID, 'obs_menu')
OPEN_OBS_MENU_TITLE = (By.TAG_NAME, 'h2')
OPEN_OBS_MENU_LIST_ITEMS = (By.TAG_NAME, 'li')
OPEN_OBS_MENU_NEWS_ITEM = (By.CSS_SELECTOR,
                           '#obs_menu > div > ul > li.rightContent a')
OPEN_OBS_MENU_NEWS_DEADLINE = (By.CLASS_NAME, 'aside')

OPEN_OBS_MENU_GCS = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(2)')

OPEN_OBS_MENU_HEIGHT = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(3) > a')

OPEN_OBS_MENU_WEIGHT = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(4)')

OPEN_OBS_MENU_BLOOD_PRODUCT = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(5)')

OPEN_OBS_MENU_BLOOD_SUGAR = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(6)')

OPEN_OBS_MENU_BS_SCALE = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(7)')

OPEN_OBS_MENU_POSTURAL_PRESSURE = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(8)')

PATIENT_INFO = (By.CSS_SELECTOR, '#obsButton h3.name')
PATIENT_NAME = (By.CSS_SELECTOR, '#obsButton h3.name strong')
GRAPH_TAB_BUTTON = (By.CSS_SELECTOR,
                    '.content .block .tabs li:first-child a')
TABLE_TAB_BUTTON = (By.CSS_SELECTOR,
                    '.content .block .tabs li:last-child a')

GRAPH_CONTAINER = (By.ID, 'graph-content')
TABLE_CONTAINER = (By.ID, 'table-content')
TABLE_CONTAINER_TABLE = (By.CSS_SELECTOR, '#table-content table')
GRAPH_CHART = (By.ID, 'chart')
GRAPH_CHART_SVG = (By.CSS_SELECTOR, '#chart svg')
NO_OBS_IN_CHART = (By.CSS_SELECTOR, '#chart > h2')
TABULAR_VALUES_TABLE = (By.CSS_SELECTOR, '#chart .nhtable')
TABLE_HEADER = (By.TAG_NAME, 'th')
TABLE_ROW = (By.TAG_NAME, 'tr')
TABLE_DATA = (By.TAG_NAME, 'td')
START_TIME_CONTROL = (By.ID, 'start_time')
START_DATE_CONTROL = (By.ID, 'start_date')
END_TIME_CONTROL = (By.ID, 'end_time')
END_DATE_CONTROL = (By.ID, 'end_date')
RANGIFY_CONTROL = (By.ID, 'rangify')
CHART_CONTEXT_GRAPH = (By.CSS_SELECTOR, '.nhcontext .nhgraph')
CHART_FOCUS_GRAPHS = (By.CSS_SELECTOR, '.nhfocus .nhgraph')
CHART_GRAPH_LABEL = (By.CSS_SELECTOR, '.background .label')
CHART_GRAPH_MEASUREMENT = (By.CSS_SELECTOR, '.background .measurement')
