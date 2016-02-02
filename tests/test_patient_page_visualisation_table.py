"""Test to ensure that the table data can display correctly"""
from tests.test_visualisation_common import TestVisualisationCommon


class TestPatientPageVisualisationTable(TestVisualisationCommon):
    """
    Setup a session and test that the data displays correctly
    """
    def setUp(self):
        super(TestPatientPageVisualisationTable, self).setUp()

    def test_news_score_title(self):
        """
        Test that the NEWS score title in the table is correct
        """
        self.assertEqual(self.news_row[0], 'NEWS Score',
                         'Incorrect title on news score row')

    def test_respiration_rate_title(self):
        """
        Test that the respiration rate title in the table is correct
        """
        self.assertEqual(self.rr_row[0], 'Respiration Rate',
                         'Incorrect title on respiration rate row')

    def test_o2_saturation_title(self):
        """
        Test that the o2 saturation title in the table is correct
        """
        self.assertEqual(self.os_row[0], 'O2 Saturation',
                         'Incorrect title on o2 sat row')

    def test_body_temperature_title(self):
        """
        Test that the body temperature title in the table is correct
        """
        self.assertEqual(self.bt_row[0], 'Body Temperature',
                         'Incorrect title on Body Temperature row')

    def test_blood_pressure_s_title(self):
        """
        Test that the systolic blood pressure title in the table is correct
        """
        self.assertEqual(self.bps_row[0], 'Blood Pressure Systolic',
                         'Incorrect title on Blood Pressure Systolic row')

    def test_blood_pressure_d_title(self):
        """
        Test that the diastolic blood pressure title in the table is correct
        """
        self.assertEqual(self.bpd_row[0], 'Blood Pressure Diastolic',
                         'Incorrect title on Blood Pressure Diastolic row')

    def test_pulse_rate_title(self):
        """
        Test that the pulse rate title in the table is correct
        """
        self.assertEqual(self.ps_row[0], 'Pulse Rate',
                         'Incorrect title on Pulse Rate row')

    def test_avpu_title(self):
        """
        Test that the avpu title in the table is correct
        """
        self.assertEqual(self.as_row[0], 'AVPU',
                         'Incorrect title on AVPU row')

    def test_supplemental_title(self):
        """
        Test that the supplemental o2 title in the table is correct
        """
        self.assertEqual(self.pos_row[0], 'Patient on Supplemental O2',
                         'Incorrect title on Supplemental O2 row')

    def test_device_title(self):
        """
        Test that the device title in the table is correct
        """
        self.assertEqual(self.ios_row[0], 'Inspired Oxygen',
                         'Incorrect title on Inspired Oxygen row')