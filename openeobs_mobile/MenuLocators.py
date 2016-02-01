from selenium.webdriver.common.by import By

task_list_el = (By.ID, 'taskNavItem')
patient_list_el = (By.ID, 'patientNavItem')
stand_in_el = (By.LINK_TEXT, 'Stand In')
barcode_scan_el = (By.CSS_SELECTOR, '.header-main li.scan_parent .scan')
barcode_scan_input = (By.CSS_SELECTOR, '#patient_barcode .barcode_scan')
logout_el = (By.CSS_SELECTOR, '.header-main li.logout .button')