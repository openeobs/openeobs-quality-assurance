from selenium.webdriver.common.by import By

username_el = (By.ID, 'username')
password_el = (By.ID, 'password')
login_button_el = (By.ID, 'loginbutton')
database_dropdown_el = (By.ID, 'database')
error_el = (By.CSS_SELECTOR, '.alert.alert-error')