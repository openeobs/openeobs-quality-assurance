"""Methods and helpers for patient data visualisation"""
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.list_page import ListPage
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from tests.test_common import TestCommon
from openeobs_mobile.patient_page_graph import PatientPageGraphs
from tests.environment import NURSE_PWD1, NURSE_USERNM1, PATIENT_PAGE, \
    MOB_LOGIN


class TestVisualisationCommon(TestCommon):
    """
    Setup a session and ensure that patient data displays correctly
    """
    risk = 'none'

    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.patient_page = PatientPage(self.driver)
        self.patient_page_graph = PatientPageGraphs(self.driver)

        risk_mapping = {
            'high': self.patient_page.add_high_risk_observation,
        }
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.list_page.go_to_patient_list()
        patients = self.list_page.get_list_items()
        patient_to_test = patients[0]
        patient_id = patient_to_test.get_attribute('href').replace(
            PATIENT_PAGE, ''
        )

        self.patient_page.remove_observations_for_patient(int(patient_id))

        risk_mapping[self.risk](int(patient_id))

        self.driver.get(patient_to_test.get_attribute('href'))
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
        self.graph_list = []

        for graph in focus_graphs:
            self.graph_list.append(graph)

        self.graph_data = self.get_graph_data()

    def get_graph_data(self):
        """
        Helper function to get an dict of the focus chart data
        :return: dict of strings from focus chart data
        """
        rr_mes = \
            self.patient_page_graph.get_graph_measurement(self.graph_list[0])
        os_mes = \
            self.patient_page_graph.get_graph_measurement(self.graph_list[1])
        bt_mes = \
            self.patient_page_graph.get_graph_measurement(self.graph_list[2])
        hr_mes = \
            self.patient_page_graph.get_graph_measurement(self.graph_list[3])
        bp_mes = \
            self.patient_page_graph.get_graph_measurements(self.graph_list[4])

        return {
            'resp_rate': rr_mes,
            'oxy_sat': os_mes,
            'body_temp': bt_mes,
            'pulse_rate': hr_mes,
            'blood_press': bp_mes
        }

    def get_focus_chart_labels(self):
        """
        Helper function to get an dict of the focus chart labels
        :return: dict of strings from focus chart labels
        """
        rr_label = self.patient_page_graph.get_graph_label(self.graph_list[0])
        os_label = self.patient_page_graph.get_graph_label(self.graph_list[1])
        bt_label = self.patient_page_graph.get_graph_label(self.graph_list[2])
        hr_label = self.patient_page_graph.get_graph_label(self.graph_list[3])
        bp_label = self.patient_page_graph.get_graph_label(self.graph_list[4])
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
        tabular_values_table = self.patient_page.get_tabular_values()

        tabular_values_rows = \
            self.patient_page.get_table_rows(tabular_values_table)

        tabular_values = \
            self.patient_page.get_table_data(tabular_values_rows[row])
        self.assertEqual(len(tabular_values), 4, 'Incorrect number of data')
        return tabular_values[column]
