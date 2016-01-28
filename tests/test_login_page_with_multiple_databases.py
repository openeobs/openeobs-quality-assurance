"""Test to ensure that the login page works correctly
with multiple databases"""
from openeobs_mobile.login_page import LoginPage
import unittest
from erppeek import Client
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestLoginPageWithMultipleDBs(unittest.TestCase):
    """
    Setup a session and test the login page with multiple databases
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://localhost:8069/web?db=nhclinical')
        ui.WebDriverWait(cls.driver, 5).until(
            ec.visibility_of_element_located((
                By.CSS_SELECTOR,
                '.oe_single_form_container.modal-content'))
        )
        cls.odoo_client = Client('http://localhost:8069', db='nhclinical',
                                 user='admin', password='admin')
        cls.odoo_client.db.drop('changeme1', 'nhclinical_dupl')
        cls.odoo_client.db.duplicate_database('changeme1', 'nhclinical',
                                              'nhclinical_dupl')

    @classmethod
    def tearDownClass(cls):
        cls.odoo_client.db.drop('changeme1', 'nhclinical_dupl')
        super(TestLoginPageWithMultipleDBs, cls).tearDownClass()

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)

    def test_login_page_shows_dropdown_for_multiple_dbs(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.assertTrue(
            self.login_page.shows_dropdown_for_multiple_databases(),
            'Incorrect page title'
        )
