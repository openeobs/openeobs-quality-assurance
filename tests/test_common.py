"""Sets up and tears down a test class"""
import unittest
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from erppeek import Client
from environment import DATABASE, URL, ODOO_CLIENT_URL, TEST_DB_NAME


class TestCommon(unittest.TestCase):
    """Setup and teardown methods"""

    @classmethod
    def setUpClass(cls):
        database = DATABASE
        url = URL
        odoo_client_url = ODOO_CLIENT_URL
        test_db = TEST_DB_NAME

        cls.driver = webdriver.Firefox()
        cls.driver.get(url)
        ui.WebDriverWait(cls.driver, 5).until(
            ec.visibility_of_element_located((
                By.CSS_SELECTOR,
                '.oe_single_form_container.modal-content'))
        )
        cls.odoo_client = Client(odoo_client_url, db=database,
                                 user='admin', password='admin')

        cls.test_database_name = test_db

        cls.odoo_client.db.drop('admin', cls.test_database_name)
        cls.odoo_client.db.duplicate_database('admin', database,
                                              cls.test_database_name)

    @classmethod
    def tearDownClass(cls):
        cls.odoo_client.db.drop('admin', cls.test_database_name)
        cls.driver.close()
