from test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationWithNoRiskObsData(TestVisualisationCommon):

    def setUp(self):
        self.risk = 'none'
        super(TestPatientPageVisualisationWithNoRiskObsData, self).setUp()

    def test_shows_correct_resp_rate_value_on_chart(self):
        """
        Test that the value for resp rate on the chart is correct
        """
        self.assertEqual(self.rr_mes, '18/min',
                         'Incorrect Respiration Rate Measurement')

    def test_shows_correct_oxy_sat_value_on_chart(self):
        """
        Test that the value for oxygen saturation on the chart is correct
        """
        self.assertEqual(self.os_mes, '99%',
                         'Incorrect O2 Saturation Measurement')

    def test_shows_correct_body_temp_value_on_chart(self):
        """
        Test that the value for body temperature on the chart is correct
        """
        self.assertIn('37.5', self.bt_mes,
                      'Incorrect Body Temperature Measurement')

    def test_shows_correct_pulse_rate_value_on_chart(self):
        """
        Test that the value for pulse rate on the chart is correct
        """
        self.assertEqual(self.hr_mes, '65/min',
                         'Incorrect Pulse Rate Measurement')

    def test_shows_correct_blood_pressure_value_on_chart(self):
        """
        Test that the value for blood pressure on the chart is correct
        """
        self.assertEqual(self.bp_mes[0].text, '120',
                         'Incorrect Blood Pressure Measurement - top')
        self.assertEqual(self.bp_mes[1].text, '80mmHg',
                         'Incorrect Blood Pressure Measurement - bottom')

    def test_shows_the_correct_avpu_value_in_tabular_values(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(self.get_tabular_values_value(1, 1), 'A',
                         'Incorrect avpu data in table')

    def test_shows_the_correct_supple_oxy_value_in_tabular_values(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(self.get_tabular_values_value(1, 2), 'No',
                         'Incorrect on suppl o2 data in table')

    def test_shows_the_correct_inspired_oxy_value_in_tabular_values(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(
            self.get_tabular_values_value(1, 3),
            '',
            'Incorrect inspired o2 data in table'
        )

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
