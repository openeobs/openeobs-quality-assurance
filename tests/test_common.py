import unittest
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By


class TestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://localhost:8069/web?db=nhclinical')
        UI.WebDriverWait(cls.driver, 5).until(
            EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                     '.oe_single_form_container.modal-content')
            )
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
