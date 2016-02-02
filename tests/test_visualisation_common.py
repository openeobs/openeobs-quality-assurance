"""Methods and helpers for patient data visualisation"""
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from tests.test_common import TestCommon
from openeobs_mobile.patient_page_graph import PatientPageGraphs


class TestVisualisationCommon(TestCommon):
    """
    Setup a session and ensure that patient data displays correctly
    """
    risk = 'none'

    def setUp(self):
        self.driver.get("http://localhost:8069/mobile/login")
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.patient_page = PatientPage(self.driver)
        self.patient_page_graph = PatientPageGraphs(self.driver)

        risk_mapping = {
            'none': self.patient_page.add_no_risk_observation,
            'low': self.patient_page.add_low_risk_observation,
            'medium':
                self.patient_page.add_medium_risk_observation,
            'high': self.patient_page.add_high_risk_observation,
            '3in1': self.patient_page.add_three_in_one_observation
        }

        self.login_page.login('nasir', 'nasir')
        self.list_page.go_to_patient_list()
        patients = self.list_page.get_list_items()
        patient_to_test = patients[0]
        self.patient_url = patient_to_test.get_attribute('href')
        self.patient_id = self.patient_url.replace(
            'http://localhost:8069/mobile/patient/', ''
        )

        self.patient_page.remove_observations_for_patient(int(self.patient_id))
        risk_mapping[self.risk](int(self.patient_id))
        self.driver.get(self.patient_url)
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, '#chart svg')))

        self.patient_page.change_to_table()
        obs_table = self.patient_page.get_obs_table()
        rows = self.patient_page.get_table_rows(obs_table)[1:]

        self.row_data = []
        for row in rows:
            self.row_data.append(self.patient_page.get_table_data(row))


        self.patient_page_graph.change_to_chart()

        # Focus Graphs
        focus_graphs = self.patient_page_graph.get_focus_graphs()
        self.assertEqual(len(focus_graphs), 5, 'Incorrect number of graphs')
        self.resp_rate_graph = focus_graphs[0]
        self.oxy_sat_graph = focus_graphs[1]
        self.temp_graph = focus_graphs[2]
        self.hr_graph = focus_graphs[3]
        self.bp_graph = focus_graphs[4]
        self.rr_mes = \
            self.patient_page_graph.get_graph_measurement(self.resp_rate_graph)
        self.os_mes = \
            self.patient_page_graph.get_graph_measurement(self.oxy_sat_graph)
        self.bt_mes = self.patient_page_graph.get_graph_measurement(self.
                                                                    temp_graph)
        self.hr_mes = self.patient_page_graph.get_graph_measurement(self.
                                                                    hr_graph)
        self.bp_mes = self.patient_page_graph.get_graph_measurements(self.
                                                                     bp_graph)

        # Tabular Values table
        tabular_values_table = self.patient_page.get_tabular_values()
        self.tabular_values_headers = \
            self.patient_page.get_table_headers(tabular_values_table)
        self.tabular_values_rows = \
            self.patient_page.get_table_rows(tabular_values_table)

    def get_focus_chart_labels(self):
        """
        Helper function to get an dict of the focus chart labels
        :return: dict of strings from focus chart labels
        """
        rr_label = self.patient_page_graph.get_graph_label(self.resp_rate_graph
                                                           )
        os_label = self.patient_page_graph.get_graph_label(self.oxy_sat_graph)
        bt_label = self.patient_page_graph.get_graph_label(self.temp_graph)
        hr_label = self.patient_page_graph.get_graph_label(self.hr_graph)
        bp_label = self.patient_page_graph.get_graph_label(self.bp_graph)
        return {
            'resp_rate': rr_label,
            'oxy_sat': os_label,
            'body_temp': bt_label,
            'pulse_rate': hr_label,
            'blood_press': bp_label
        }

    def get_tabular_values_value(self, row, column):
        """
        Helper function to get the value from a row and column in the tabular
        values table
        :param row: Row to get value from
        :param column: Column to get value from
        :return: String from row/column combo
        """
        tabular_values = \
            self.patient_page.get_table_data(self.tabular_values_rows[row])
        self.assertEqual(len(tabular_values), 4, 'Incorrect number of data')
        return tabular_values[column]
