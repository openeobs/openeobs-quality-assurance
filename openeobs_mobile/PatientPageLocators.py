from selenium.webdriver.common.by import By

adhoc_obs_menu_button = (By.CLASS_NAME, 'obs')
open_obs_menu = (By.ID, 'obs_menu')
open_obs_menu_title = (By.TAG_NAME, 'h2')
open_obs_menu_list_items = (By.TAG_NAME, 'li')
open_obs_menu_news_item = (By.CSS_SELECTOR,
                           '#obs_menu > div > ul > li.rightContent')
open_obs_menu_news_deadline = (By.CLASS_NAME, 'aside')
open_obs_menu_gcs = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(2)')
open_obs_menu_height = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(3)')
open_obs_menu_weight = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(4)')
open_obs_menu_blood_product = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(5)')
open_obs_menu_blood_sugar = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(6)')
open_obs_menu_bs_scale = (
    By.CSS_SELECTOR, '#obs_menu > div > ul > li:nth-child(7)')
open_obs_menu_postural_pressure = (
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