"""Tests to ensure that the values for a high risk NEWS ob are correct"""
from tests.test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationWithHighRiskObsData(TestVisualisationCommon):
    """
    Assert value of ews for high risk observation
    """

    def setUp(self):
        self.risk = 'high'
        super(TestPatientPageVisualisationWithHighRiskObsData, self).setUp()

    def test_chart_resp_rate_value(self):
        """
        Test that the value for resp rate on the chart is correct
        """
        self.assertEqual(self.rr_mes, '24/min',
                         'Incorrect Respiration Rate Measurement')

    def test_chart_oxy_sat_value(self):
        """
        Test that the value for oxygen saturation on the chart is correct
        """
        self.assertEqual(self.os_mes, '93%',
                         'Incorrect O2 Saturation Measurement')

    def test_chart_body_temp_value(self):
        """
        Test that the value for body temperature on the chart is correct
        """
        self.assertIn('36', self.bt_mes,
                      'Incorrect Body Temperature Measurement')

    def test_chart_pulse_rate_value(self):
        """
        Test that the value for pulse rate on the chart is correct
        """
        self.assertEqual(self.hr_mes, '130/min',
                         'Incorrect Pulse Rate Measurement')

    def test_chart_blood_pressure_value(self):
        """
        Test that the value for blood pressure on the chart is correct
        """
        self.assertEqual(self.bp_mes[0].text, '100',
                         'Incorrect Blood Pressure Measurement - top')
        self.assertEqual(self.bp_mes[1].text, '80mmHg',
                         'Incorrect Blood Pressure Measurement - bottom')

    def test_tabular_avpu_value(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(self.get_tabular_values_value(1, 1), 'A',
                         'Incorrect avpu data in table')

    def test_tabular_supple_oxy_value(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(self.get_tabular_values_value(1, 2), 'Yes',
                         'Incorrect on suppl o2 data in table')

    def test_tabular_inspired_oxy_value(self):
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
        self.assertEqual(self.row_data[0][1], '11',
                         'Incorrect value on news score row for high risk ob')

    def test_respiration_rate_value(self):
        """
        Test that the respiration rate value is correct
        """
        self.assertEqual(self.row_data[1][1], '24',
                         'Incorrect value on respiration rate row '
                         'for high risk ob')

    def test_o2_saturation_value(self):
        """
        Test that the o2 saturation value is correct
        """
        self.assertEqual(self.row_data[2][1], '93', 'Incorrect value on o2 row'
                                                    ' for high risk ob')

    def test_body_temperature_value(self):
        """
        Test that the body temperature value is correct
        """
        self.assertEqual(self.row_data[3][1], '36',
                         'Incorrect value on Body Temperature row '
                         'for high risk ob')

    def test_blood_pressure_s_value(self):
        """
        Test that the systolic blood pressure value is correct
        """
        self.assertEqual(self.row_data[4][1], '100',
                         'Incorrect value on Blood Pressure Systolic row '
                         'for high risk ob')

    def test_blood_pressure_d_value(self):
        """
        Test that the diastolic blood pressure value is correct
        """
        self.assertEqual(self.row_data[5][1], '80',
                         'Incorrect value on Blood Pressure Diastolic row '
                         'for high risk ob')

    def test_pulse_rate_value(self):
        """
        Test that the pulse rate value is correct
        """
        self.assertEqual(self.row_data[6][1], '130',
                         'Incorrect value on Pulse Rate row '
                         'for high risk ob')

    def test_avpu_value(self):
        """
        Test that the avpu value is correct
        """
        self.assertEqual(self.row_data[7][1], 'A', 'Incorrect value on AVPU '
                                                   'row for high risk ob')

    def test_supplemental_value(self):
        """
        Test that the supplemental o2 value is correct
        """
        self.assertEqual(self.row_data[8][1], 'Yes',
                         'Incorrect value on Supplemental O2 row '
                         'for high risk ob')

    def test_device_value(self):
        """
        Test that the device value is correct
        """
        self.assertEqual(self.row_data[9][1],
                         'Flow Rate: 10\nDevice: Intubated',
                         'Incorrect value on Inspired Oxygen row '
                         'for high risk ob')
