from test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationWithNoRiskObsData(TestVisualisationCommon):

    def setUp(self):
        self.risk = 'none'
        super(TestPatientPageVisualisationWithNoRiskObsData, self).setUp()

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

    def test_shows_chart_after_viewing_table(self):
        """
        Test that pressing the chart tab after being on table tab works
        """
        self.patient_page.change_to_table()
        self.patient_page.change_to_chart()
        self.assertTrue(self.patient_page.chart_is_shown(),
                        'Chart does not display when returning from table')

    def test_shows_ranged_values_control(self):
        """
        Test that the ranged values control is shown
        """
        self.assertTrue(self.patient_page.rangify_control_is_shown(),
                        'Rangify control not shown')

    def test_shows_correct_labels_on_chart(self):
        """
        Test that the labels on the chart are correct
        """
        graphs = self.patient_page.get_focus_graphs()
        self.assertEqual(len(graphs), 5, 'Incorrect number of graphs')
        resp_rate_graph = graphs[0]
        oxy_sat_graph = graphs[1]
        temp_graph = graphs[2]
        hr_graph = graphs[3]
        bp_graph = graphs[4]

        rr_label = self.patient_page.get_graph_label(resp_rate_graph)
        rr_mes = self.patient_page.get_graph_measurement(resp_rate_graph)
        self.assertEqual(rr_label, 'RR', 'Incorrect Respiration Rate Label')
        self.assertEqual(rr_mes, '18/min',
                         'Incorrect Respiration Rate Measurement')

        os_label = self.patient_page.get_graph_label(oxy_sat_graph)
        os_mes = self.patient_page.get_graph_measurement(oxy_sat_graph)
        self.assertEqual(os_label, 'Spo2', 'Incorrect O2 Saturation Label')
        self.assertEqual(os_mes, '99%', 'Incorrect O2 Saturation Measurement')

        bt_label = self.patient_page.get_graph_label(temp_graph)
        bt_mes = self.patient_page.get_graph_measurement(temp_graph)
        self.assertEqual(bt_label, 'Temp', 'Incorrect Body Temperature Label')
        self.assertIn('37.5', bt_mes,
                      'Incorrect Body Temperature Measurement')

        hr_label = self.patient_page.get_graph_label(hr_graph)
        hr_mes = self.patient_page.get_graph_measurement(hr_graph)
        self.assertEqual(hr_label, 'HR', 'Incorrect Pulse Rate Label')
        self.assertEqual(hr_mes, '65/min', 'Incorrect Pulse Rate Measurement')

        bp_label = self.patient_page.get_graph_label(bp_graph)
        bp_mes = self.patient_page.get_graph_measurements(bp_graph)
        self.assertEqual(bp_label, 'BP', 'Incorrect Blood Pressure Label')
        self.assertEqual(bp_mes[0].text, '120',
                         'Incorrect Blood Pressure Measurement - top')
        self.assertEqual(bp_mes[1].text, '80mmHg',
                         'Incorrect Blood Pressure Measurement - bottom')

    def test_shows_the_correct_values_in_tabular_values(self):
        """
        Test that the tabular values table shows the correct data
        """
        tabular_values_table = self.patient_page.get_tabular_values()
        headers = self.patient_page.get_table_headers(tabular_values_table)
        self.assertEqual(len(headers), 4, 'Incorrect number of headers')
        self.assertEqual(headers, ['Date', 'AVPU', 'On Supplemental O2',
                                   'Inspired Oxygen'],
                         'Incorrect table headers')
        table_rows = self.patient_page.get_table_rows(tabular_values_table)
        tabular_values = self.patient_page.get_table_data(table_rows[1])
        tab_vals = [vals for vals in tabular_values if vals]
        self.assertEqual(len(tab_vals), 3, 'Incorrect number of data')
        # TODO: I'm skipping the date field cos that will make things fragile
        self.assertEqual(tab_vals[1:], ['A', 'No'], 'Incorrect data in table')

    def test_shows_the_correct_values_in_table(self):
        """
        Test that the table of obs shows the correct data
        """
        self.patient_page.change_to_table()
        obs_table = self.patient_page.get_obs_table()
        headers = self.patient_page.get_table_headers(obs_table)
        self.assertEqual(len(headers), 2, 'Incorrect number of headers')
        # TODO: I'm skipping date header due to fragile ness
        self.assertEqual(headers[0], 'Date', 'Incorrect header')
        rows = self.patient_page.get_table_rows(obs_table)[1:]
        self.assertEqual(len(rows), 10, 'Incorrect number of rows')

        news_row = self.patient_page.get_table_data(rows[0])
        self.assertEqual(news_row[0], 'NEWS Score',
                         'Incorrect title on news score row')
        self.assertEqual(news_row[1], '0',
                         'Incorrect value on news score row')

        rr_row = self.patient_page.get_table_data(rows[1])
        self.assertEqual(rr_row[0], 'Respiration Rate',
                         'Incorrect title on respiration rate row')
        self.assertEqual(rr_row[1], '18',
                         'Incorrect value on respiration rate row')

        os_row = self.patient_page.get_table_data(rows[2])
        self.assertEqual(os_row[0], 'O2 Saturation',
                         'Incorrect title on O2 Saturation row')
        self.assertEqual(os_row[1], '99',
                         'Incorrect value on O2 Saturation row')

        bt_row = self.patient_page.get_table_data(rows[3])
        self.assertEqual(bt_row[0], 'Body Temperature',
                         'Incorrect title on Body Temperature row')
        self.assertEqual(bt_row[1], '37.5',
                         'Incorrect value on Body Temperature row')

        bps_row = self.patient_page.get_table_data(rows[4])
        self.assertEqual(bps_row[0], 'Blood Pressure Systolic',
                         'Incorrect title on Blood Pressure Systolic row')
        self.assertEqual(bps_row[1], '120',
                         'Incorrect value on Blood Pressure Systolic row')

        bpd_row = self.patient_page.get_table_data(rows[5])
        self.assertEqual(bpd_row[0], 'Blood Pressure Diastolic',
                         'Incorrect title on Blood Pressure Diastolic row')
        self.assertEqual(bpd_row[1], '80',
                         'Incorrect value on Blood Pressure Diastolic row')

        ps_row = self.patient_page.get_table_data(rows[6])
        self.assertEqual(ps_row[0], 'Pulse Rate',
                         'Incorrect title on Pulse Rate row')
        self.assertEqual(ps_row[1], '65',
                         'Incorrect value on Pulse Rate row')

        as_row = self.patient_page.get_table_data(rows[7])
        self.assertEqual(as_row[0], 'AVPU',
                         'Incorrect title on AVPU row')
        self.assertEqual(as_row[1], 'A',
                         'Incorrect value on AVPU row')

        pos_row = self.patient_page.get_table_data(rows[8])
        self.assertEqual(pos_row[0], 'Patient on Supplemental O2',
                         'Incorrect title on Supplemental O2 row')
        self.assertEqual(pos_row[1], 'No',
                         'Incorrect value on Supplemental O2 row')

        ios_row = self.patient_page.get_table_data(rows[9])
        self.assertEqual(ios_row[0], 'Inspired Oxygen',
                         'Incorrect title on Inspired Oxygen row')
        self.assertEqual(ios_row[1], '',
                         'Incorrect value on Inspired Oxygen row')
