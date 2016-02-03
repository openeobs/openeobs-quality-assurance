"""Test to ensure that the patient data can display correctly"""
from tests.test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationStructure(TestVisualisationCommon):
    """
    Setup a session and test that the data displays correctly
    """
    def setUp(self):
        self.risk = 'high'
        super(TestPatientPageVisualisationStructure, self).setUp()

        # Tabular Values table
        self.tabular_values_table = self.patient_page.get_tabular_values()

        self.tabular_values_headers = \
            self.patient_page.get_table_headers(self.tabular_values_table)

    def test_doesnt_show_no_obs_message(self):
        """
        Test that the No observation data available for patient message is
        shown on no obs being available
        """
        self.assertFalse(self.patient_page.has_no_patient_data(),
                         'No Observation Data Available message not found')

    def test_shows_tabs(self):
        """
        Test that the tabs are shown
        """
        self.assertTrue(self.patient_page.tabs_are_shown(),
                        'Tabs to switch between chart and table are not shown')

    def test_shows_chart(self):
        """
        Test that the chart is displayed with a single data point present
        """
        self.assertTrue(self.patient_page.chart_is_shown(),
                        'Chart is not shown')

    def test_shows_tabular_values(self):
        """
        Test that shows the tabular values table
        """
        self.assertTrue(self.patient_page.tabular_values_are_shown(),
                        'Tabular values aren\'t shown')

    def test_shows_table(self):
        """
        Test that pressing the table tab shows the table
        """
        self.patient_page.change_to_table()
        self.assertTrue(self.patient_page.obs_table_is_shown(),
                        'Observation table is not shown')

    def test_shows_obs_menu(self):
        """
        Test that pressing the take Observation button still works
        """
        self.patient_page.open_adhoc_obs_menu()
        self.assertTrue(self.patient_page.adhoc_obs_menu_is_open(),
                        'Adhoc observation menu is not open')

    def test_show_chart_after_table(self):
        """
        Test that pressing the chart tab after being on table tab works
        """
        self.patient_page.change_to_table()
        self.patient_page_graph.change_to_chart()
        self.assertTrue(self.patient_page.chart_is_shown(),
                        'Chart does not display when returning from table')

    def test_show_ranged_values_control(self):
        """
        Test that the ranged values control is shown
        """
        self.assertTrue(self.patient_page_graph.rangify_control_is_shown(),
                        'Rangify control not shown')

    def test_chart_resp_rate_label(self):
        """
        Test that the resp rate label on focus chart says RR
        """
        rr_label = self.get_focus_chart_labels()['resp_rate']
        self.assertEqual(rr_label, 'RR', 'Incorrect Respiration Rate Label')

    def test_chart_oxy_sat_label(self):
        """
        TEst that the oxygen saturation label on focus chart is correct
        """
        os_label = self.get_focus_chart_labels()['oxy_sat']
        self.assertEqual(os_label, 'Spo2', 'Incorrect O2 Saturation Label')

    def test_chart_body_temp_label(self):
        """
        Test that the body temperature label on focus chart is correct
        """
        bt_label = self.get_focus_chart_labels()['body_temp']
        self.assertEqual(bt_label, 'Temp', 'Incorrect Body Temperature Label')

    def test_chart_pulse_rate_label(self):
        """
        Test that the pulse rrate label for focus chart is correct
        """
        hr_label = self.get_focus_chart_labels()['pulse_rate']
        self.assertEqual(hr_label, 'HR', 'Incorrect Pulse Rate Label')

    def test_chart_blood_pressure_label(self):
        """
        Test that the blood pressure label for focus chart is correct
        """
        bp_label = self.get_focus_chart_labels()['blood_press']
        self.assertEqual(bp_label, 'BP', 'Incorrect Blood Pressure Label')

    def test_correct_tabular_headers(self):
        """
        Test that the tabular values have the correct headers
        """
        self.assertEqual(len(self.tabular_values_headers), 4,
                         'Incorrect number of headers')
        self.assertEqual(self.tabular_values_headers,
                         ['Date', 'AVPU', 'On Supplemental O2',
                          'Inspired Oxygen'],
                         'Incorrect table headers')

    def test_correct_number_of_headers(self):
        """
        Test that the table of obs has the correct number of headers
        """
        self.patient_page.change_to_table()
        self.assertEqual(len(self.patient_page.get_table_headers
                             (self.patient_page.get_obs_table())), 2,
                         'Incorrect number of headers')

    def test_date_header(self):
        """
        Test the date header
        """

        self.assertEqual(self.patient_page.get_table_headers
                         (self.patient_page.get_obs_table())[0],
                         'Date', 'Incorrect header')

    def test_number_of_rows(self):
        """
        Test that the number of rows is correct
        """
        self.assertEqual(len(self.patient_page.get_table_rows
                             (self.patient_page.get_obs_table())[1:]), 10,
                         'Incorrect number of rows')
