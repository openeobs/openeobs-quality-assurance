"""Test to ensure that the login page works correctly
with multiple databases"""
from openeobs_mobile.login_page import LoginPage
import unittest
from erppeek import Client
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium import webdriver
from tests.environment import MOB_LOGIN, ODOO_CLIENT_URL, DATABASE, \
    USERNAME, PASSWORD


class TestLoginPageWithMultipleDBs(unittest.TestCase):
    """
    Setup a session and test the login page with multiple databases
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(MOB_LOGIN)
        ui.WebDriverWait(cls.driver, 5).until(
            ec.visibility_of_element_located((
                By.CSS_SELECTOR,
                '.oe_single_form_container.modal-content'))
        )
        cls.odoo_client = Client(ODOO_CLIENT_URL, db=DATABASE,
                                 user=USERNAME, password=PASSWORD)
        cls.odoo_client.db.drop('changeme1', 'nhclinical_dupl')
        cls.odoo_client.db.duplicate_database('changeme1', '2701',
                                              'nhclinical_dupl')

    @classmethod
    def tearDownClass(cls):
        cls.odoo_client.db.drop('changeme1', 'nhclinical_dupl')
        super(TestLoginPageWithMultipleDBs, cls).tearDownClass()

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)

    def test_db_dropdown_on_login(self):
        """
        Test that the dropdown of databases is loaded successfully
        on login page
        """
        self.assertTrue(
            self.login_page.show_dropdown_for_databases(),
            'Incorrect page title'
        )
