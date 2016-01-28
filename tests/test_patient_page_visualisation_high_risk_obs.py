from tests.test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationWithHighRiskObsData(TestVisualisationCommon):

    def setUp(self):
        self.risk = 'high'
        super(TestPatientPageVisualisationWithHighRiskObsData, self).setUp()

    def test_shows_correct_resp_rate_value_on_chart(self):
        """
        Test that the value for resp rate on the chart is correct
        """
        self.assertEqual(self.rr_mes, '24/min',
                         'Incorrect Respiration Rate Measurement')

    def test_shows_correct_oxy_sat_value_on_chart(self):
        """
        Test that the value for oxygen saturation on the chart is correct
        """
        self.assertEqual(self.os_mes, '93%',
                         'Incorrect O2 Saturation Measurement')

    def test_shows_correct_body_temp_value_on_chart(self):
        """
        Test that the value for body temperature on the chart is correct
        """
        self.assertIn('36', self.bt_mes,
                      'Incorrect Body Temperature Measurement')

    def test_shows_correct_pulse_rate_value_on_chart(self):
        """
        Test that the value for pulse rate on the chart is correct
        """
        self.assertEqual(self.hr_mes, '130/min',
                         'Incorrect Pulse Rate Measurement')

    def test_shows_correct_blood_pressure_value_on_chart(self):
        """
        Test that the value for blood pressure on the chart is correct
        """
        self.assertEqual(self.bp_mes[0].text, '100',
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
        self.assertEqual(self.get_tabular_values_value(1, 2), 'Yes',
                         'Incorrect on suppl o2 data in table')

    def test_shows_the_correct_inspired_oxy_value_in_tabular_values(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(
            self.get_tabular_values_value(1, 3),
            'Device: Intubated\nFlow: 10l/hr',
            'Incorrect inspired o2 data in table'
        )

    def test_news_score_value(self):
        """
        Test that the NEWS score value is correct
        """
        self.get_table_values()
        self.assertEqual(self.news_row[1], '11',
                         'Incorrect value on news score row for high risk ob')

    def test_respiration_rate_value(self):
        """
        Test that the respiration rate value is correct
        """
        self.get_table_values()
        self.assertEqual(self.rr_row[1], '24',
                         'Incorrect value on respiration rate row '
                         'for high risk ob')

    def test_o2_saturation_value(self):
        """
        Test that the o2 saturation value is correct
        """
        self.get_table_values()
        self.assertEqual(self.os_row[1], '93', 'Incorrect value on o2 row '
                                               'for high risk ob')

    def test_body_temperature_value(self):
        """
        Test that the body temperature value is correct
        """
        self.get_table_values()
        self.assertEqual(self.bt_row[1], '36',
                         'Incorrect value on Body Temperature row '
                         'for high risk ob')

    def test_blood_pressure_systolic_value(self):
        """
        Test that the systolic blood pressure value is correct
        """
        self.get_table_values()
        self.assertEqual(self.bps_row[1], '100',
                         'Incorrect value on Blood Pressure Systolic row '
                         'for high risk ob')

    def test_blood_pressure_diastolic_value(self):
        """
        Test that the diastolic blood pressure value is correct
        """
        self.get_table_values()
        self.assertEqual(self.bpd_row[1], '80',
                         'Incorrect value on Blood Pressure Diastolic row '
                         'for high risk ob')

    def test_pulse_rate_value(self):
        """
        Test that the pulse rate value is correct
        """
        self.get_table_values()
        self.assertEqual(self.ps_row[1], '130',
                         'Incorrect value on Pulse Rate row '
                         'for high risk ob')

    def test_avpu_value(self):
        """
        Test that the avpu value is correct
        """
        self.get_table_values()
        self.assertEqual(self.as_row[1], 'A', 'Incorrect value on AVPU row '
                                              'for high risk ob')

    def test_supplemental_value(self):
        """
        Test that the supplemental o2 value is correct
        """
        self.get_table_values()
        self.assertEqual(self.pos_row[1], 'Yes',
                         'Incorrect value on Supplemental O2 row '
                         'for high risk ob')

    def test_device_value(self):
        """
        Test that the device value is correct
        """
        self.get_table_values()
        self.assertEqual(self.ios_row[1],
                         'Flow Rate: 10\nDevice: Intubated',
                         'Incorrect value on Inspired Oxygen row '
                         'for high risk ob')
