import unittest
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from erppeek import Client


class TestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://localhost:8069/web?db=test')
        ui.WebDriverWait(cls.driver, 5).until(
            ec.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                     '.oe_single_form_container.modal-content')
            )
        )
        cls.odoo_client = Client('http://localhost:8069', db='test',
                                 user='admin', password='admin')
        cls.test_database_name = 'openeobs_quality_assurance_db'
        cls.odoo_client.db.drop('admin', cls.test_database_name)
        cls.odoo_client.db.duplicate_database('admin', 'test',
                                              cls.test_database_name)

    @classmethod
    def tearDownClass(cls):
        cls.odoo_client.db.drop('admin', cls.test_database_name)
        cls.driver.close()
