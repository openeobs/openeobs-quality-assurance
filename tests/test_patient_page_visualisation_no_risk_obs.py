"""Tests to ensure that the values for a no risk NEWS ob are correct"""
from tests.test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationWithNoRiskObsData(TestVisualisationCommon):
    """
        Assert value of ews for no risk observation
    """
    def setUp(self):
        self.risk = 'none'
        super(TestPatientPageVisualisationWithNoRiskObsData, self).setUp()

        self.tabular_values_table = self.patient_page.get_tabular_values()
        self.tabular_values_rows = \
            self.patient_page.get_table_rows(self.tabular_values_table)

    def test_chart_resp_rate_value(self):
        """
        Test that the value for resp rate on the chart is correct
        """
        self.assertEqual(self.graph_data['resp_rate'], '18/min',
                         'Incorrect Respiration Rate Measurement')

    def test_chart_oxy_sat_value(self):
        """
        Test that the value for oxygen saturation on the chart is correct
        """
        self.assertEqual(self.graph_data['oxy_sat'], '99%',
                         'Incorrect O2 Saturation Measurement'
                         )

    def test_chart_body_temp_value(self):
        """
        Test that the value for body temperature on the chart is correct
        """
        self.assertIn('37.5', self.graph_data['body_temp'],
                      'Incorrect Body Temperature Measurement')

    def test_chart_pulse_rate_value(self):
        """
        Test that the value for pulse rate on the chart is correct
        """
        self.assertEqual(self.graph_data['pulse_rate'], '65/min',
                         'Incorrect Pulse Rate Measurement')

    def test_chart_blood_pressure_value(self):
        """
        Test that the value for blood pressure on the chart is correct
        """
        self.assertEqual(self.graph_data['blood_press'][0].text, '120',
                         'Incorrect Blood Pressure Measurement - top')
        self.assertEqual(self.graph_data['blood_press'][1].text, '80mmHg',
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
        self.assertEqual(self.get_tabular_values_value(1, 2), 'No',
                         'Incorrect on suppl o2 data in table')

    def test_tabular_inspired_oxy_value(self):
        """
        Test that the tabular values table shows the correct data
        """
        self.assertEqual(
            self.get_tabular_values_value(1, 3),
            '',
            'Incorrect inspired o2 data in table'
        )

    def test_news_score_value(self):
        """
        Test that the NEWS score value is correct
        """
        self.assertEqual(self.row_data[0][1], '0',
                         'Incorrect value on news score row')

    def test_respiration_rate_value(self):
        """
        Test that the respiration rate value is correct
        """
        self.assertEqual(self.row_data[1][1], '18',
                         'Incorrect value on respiration rate row')

    def test_o2_saturation_value(self):
        """
        Test that the o2 saturation value is correct
        """
        self.assertEqual(self.row_data[2][1], '99',
                         'Incorrect value on o2 row')

    def test_body_temperature_value(self):
        """
        Test that the body temperature value is correct
        """
        self.assertEqual(self.row_data[3][1], '37.5',
                         'Incorrect value on Body Temperature row')

    def test_blood_pressure_s_value(self):
        """
        Test that the systolic blood pressure value is correct
        """
        self.assertEqual(self.row_data[4][1], '120',
                         'Incorrect value on Blood Pressure Systolic row')

    def test_blood_pressure_d_value(self):
        """
        Test that the diastolic blood pressure value is correct
        """
        self.assertEqual(self.row_data[5][1], '80',
                         'Incorrect value on Blood Pressure Diastolic row')

    def test_pulse_rate_value(self):
        """
        Test that the pulse rate value is correct
        """
        self.assertEqual(self.row_data[6][1], '65',
                         'Incorrect value on Pulse Rate row')

    def test_avpu_value(self):
        """
        Test that the avpu value is correct
        """
        self.assertEqual(self.row_data[7][1], 'A',
                         'Incorrect value on AVPU row')

    def test_supplemental_value(self):
        """
        Test that the supplemental o2 value is correct
        """
        self.assertEqual(self.row_data[8][1], 'No',
                         'Incorrect value on Supplemental O2 row')

    def test_device_value(self):
        """
        Test that the device value is correct
        """
        self.assertEqual(self.row_data[9][1],
                         '',
                         'Incorrect value on Inspired Oxygen row')
