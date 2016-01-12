from openeobs_selenium.login_page import LoginPage
from test_common import TestCommon
from erppeek import Client


class TestLoginPageWithMultipleDBs(TestCommon):

    @classmethod
    def setUpClass(cls):
        super(TestLoginPageWithMultipleDBs, cls).setUpClass()
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
