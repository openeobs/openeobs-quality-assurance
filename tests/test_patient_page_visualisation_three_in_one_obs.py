from test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationWith3in1RiskObsData(TestVisualisationCommon):

    def setUp(self):
        self.risk = '3in1'
        super(TestPatientPageVisualisationWith3in1RiskObsData, self).setUp()

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
        self.assertEqual(rr_mes, '11/min',
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
        self.assertEqual(tab_vals[1:], ['V', 'No'], 'Incorrect data in table')

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
        self.assertEqual(news_row[1], '4',
                         'Incorrect value on news score row')

        rr_row = self.patient_page.get_table_data(rows[1])
        self.assertEqual(rr_row[0], 'Respiration Rate',
                         'Incorrect title on respiration rate row')
        self.assertEqual(rr_row[1], '11',
                         'Incorrect value on respiration rate row')

        os_row = self.patient_page.get_table_data(rows[2])
        self.assertEqual(os_row[0], 'O2 Saturation',
                         'Incorrect title on O2 Saturation row')
        self.assertEqual(os_row[1], '99',
                         'Incorrect value on O2 Saturation row')

        bt_row = self.patient_page.get_table_data(rows[3])
        self.assertEqual(bt_row[0], 'Body Temperature',
                         'Incorrect title on body temp row')
        self.assertEqual(bt_row[1], '37.5',
                         'Incorrect value on body temp row')

        bps_row = self.patient_page.get_table_data(rows[4])
        self.assertEqual(bps_row[0], 'Blood Pressure Systolic',
                         'Incorrect title on blood pressure sys row')
        self.assertEqual(bps_row[1], '120',
                         'Incorrect value on BP sys row')

        bpd_row = self.patient_page.get_table_data(rows[5])
        self.assertEqual(bpd_row[0], 'Blood Pressure Diastolic',
                         'Incorrect title on BP dia row')
        self.assertEqual(bpd_row[1], '80',
                         'Incorrect value on Bp dia row')

        ps_row = self.patient_page.get_table_data(rows[6])
        self.assertEqual(ps_row[0], 'Pulse Rate',
                         'Incorrect title on pulse rate row')
        self.assertEqual(ps_row[1], '65',
                         'Incorrect value on pulse rate row')

        as_row = self.patient_page.get_table_data(rows[7])
        self.assertEqual(as_row[0], 'AVPU',
                         'Incorrect title on avpu row')
        self.assertEqual(as_row[1], 'V',
                         'Incorrect value on avpu row')

        pos_row = self.patient_page.get_table_data(rows[8])
        self.assertEqual(pos_row[0], 'Patient on Supplemental O2',
                         'Incorrect title on supplemental o2 row')
        self.assertEqual(pos_row[1], 'No',
                         'Incorrect value on supplemental o2 row')

        ios_row = self.patient_page.get_table_data(rows[9])
        self.assertEqual(ios_row[0], 'Inspired Oxygen',
                         'Incorrect title on inspired o2 row')
        self.assertEqual(ios_row[1], '',
                         'Incorrect value on inspired o2 row')
