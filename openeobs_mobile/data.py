"""Stores data dictionaries for QA testing"""

NO_RISK_EWS_DATA = {
    'respiration_rate': 18,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 65,
    'body_temperature': 37.5
}

LOW_RISK_SCORE_1_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 65,
    'body_temperature': 37.5
}

LOW_RISK_SCORE_2_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 65,
    'body_temperature': 37.5
}

LOW_RISK_SCORE_3_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 65,
    'body_temperature': 37.5,
    'device_id': 'Nasal Cannula',
    'flow_rate': 8
}

LOW_RISK_SCORE_4_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 65,
    'body_temperature': 37.5,
    'device_id': 'Simple Mask',
    'flow_rate': 4
}

LOW_SCORE_RESPONSE = 'Assess Patient'

MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA = {
    'respiration_rate': 18,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Voice',
    'pulse_rate': 65,
    'body_temperature': 37.5
}

MEDIUM_RISK_SCORE_4_THREE_IN_ONE_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Voice',
    'pulse_rate': 65,
    'body_temperature': 37.5
}

MEDIUM_RISK_SCORE_5_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 50,
    'body_temperature': 37.5,
    'device_id': 'Nasal Cannula',
    'concentration': 40
}

MEDIUM_RISK_SCORE_6_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'Alert',
    'pulse_rate': 50,
    'body_temperature': 37.5,
    'device_id': 'CPAP',
    'concentration': 60,
    'cpap_peep': 2
}

MEDIUM_SCORE_RESPONSE = 'Urgently inform medical team'

HIGH_RISK_SCORE_7_EWS_DATA = [
    {'name': 'respiration_rate',
     'value': 24,
     'type': 'textbox'},

    {'name': 'indirect_oxymetry_spo2',
     'value': 99,
     'type': 'textbox'},

    {'name': 'oxygen_administration_flag',
     'value': 'Yes',
     'type': 'select'},

    {'name': 'blood_pressure_systolic',
     'value': 110,
     'type': 'textbox'},

    {'name': 'blood_pressure_diastolic',
     'value': 80,
     'type': 'textbox'},

    {'name': 'avpu_text',
     'value': 'Alert',
     'type': 'select'},

    {'name': 'pulse_rate',
     'value': 50,
     'type': 'textbox'},

    {'name': 'body_temperature',
     'value': 36.0,
     'type': 'textbox'},

    {'name': 'device_id',
     'value': 'NIV BiPAP',
     'type': 'select'},

    {'name': 'concentration',
     'value': 85,
     'type': 'textbox'},

    {'name': 'niv_ipap',
     'value': 2,
     'type': 'textbox'},

    {'name': 'niv_epap',
     'value': 2,
     'type': 'textbox'},

    {'name': 'niv_backup',
     'value': 4,
     'type': 'textbox'}
]

HIGH_RISK_SCORE_8_EWS_DATA = [
        {'name': 'respiration_rate',
         'value': 24,
         'type': 'textbox'},

        {'name': 'indirect_oxymetry_spo2',
         'value': 99,
         'type': 'textbox'},

        {'name': 'oxygen_administration_flag',
         'value': 'Yes',
         'type': 'select'},

        {'name': 'blood_pressure_systolic',
         'value': 110,
         'type': 'textbox'},

        {'name': 'blood_pressure_diastolic',
         'value': 80,
         'type': 'textbox'},

        {'name': 'avpu_text',
         'value': 'Alert',
         'type': 'select'},

        {'name': 'pulse_rate',
         'value': 50,
         'type': 'textbox'},

        {'name': 'body_temperature',
         'value': 36.0,
         'type': 'textbox'},

        {'name': 'device_id',
         'value': 'With Reservoir',
         'type': 'select'},

        {'name': 'flow_rate',
         'value': 10,
         'type': 'textbox'}
    ]

HIGH_RISK_SCORE_9_EWS_DATA = [
        {'name': 'respiration_rate',
         'value': 24,
         'type': 'textbox'},

        {'name': 'indirect_oxymetry_spo2',
         'value': 99,
         'type': 'textbox'},

        {'name': 'oxygen_administration_flag',
         'value': 'Yes',
         'type': 'select'},

        {'name': 'blood_pressure_systolic',
         'value': 100,
         'type': 'textbox'},

        {'name': 'blood_pressure_diastolic',
         'value': 80,
         'type': 'textbox'},

        {'name': 'avpu_text',
         'value': 'Alert',
         'type': 'select'},

        {'name': 'pulse_rate',
         'value': 130,
         'type': 'textbox'},

        {'name': 'body_temperature',
         'value': 36.0,
         'type': 'textbox'},

        {'name': 'device_id',
         'value': 'Nasal Cannula',
         'type': 'select'},

        {'name': 'flow_rate',
         'value': 10,
         'type': 'textbox'}
    ]

HIGH_RISK_SCORE_10_EWS_DATA = [
        {'name': 'respiration_rate',
         'value': 24,
         'type': 'textbox'},

        {'name': 'indirect_oxymetry_spo2',
         'value': 95,
         'type': 'textbox'},

        {'name': 'oxygen_administration_flag',
         'value': 'Yes',
         'type': 'select'},

        {'name': 'blood_pressure_systolic',
         'value': 100,
         'type': 'textbox'},

        {'name': 'blood_pressure_diastolic',
         'value': 80,
         'type': 'textbox'},

        {'name': 'avpu_text',
         'value': 'Alert',
         'type': 'select'},

        {'name': 'pulse_rate',
         'value': 130,
         'type': 'textbox'},

        {'name': 'body_temperature',
         'value': 36.0,
         'type': 'textbox'},

        {'name': 'device_id',
         'value': 'Intubated',
         'type': 'select'},

        {'name': 'flow_rate',
         'value': 10,
         'type': 'textbox'}
    ]

HIGH_RISK_SCORE_11_EWS_DATA = [
        {'name': 'respiration_rate',
         'value': 24,
         'type': 'textbox'},

        {'name': 'indirect_oxymetry_spo2',
         'value': 93,
         'type': 'textbox'},

        {'name': 'oxygen_administration_flag',
         'value': 'Yes',
         'type': 'select'},

        {'name': 'blood_pressure_systolic',
         'value': 100,
         'type': 'textbox'},

        {'name': 'blood_pressure_diastolic',
         'value': 80,
         'type': 'textbox'},

        {'name': 'avpu_text',
         'value': 'Alert',
         'type': 'select'},

        {'name': 'pulse_rate',
         'value': 130,
         'type': 'textbox'},

        {'name': 'body_temperature',
         'value': 36.0,
         'type': 'textbox'},

        {'name': 'device_id',
         'value': 'Intubated',
         'type': 'select'},

        {'name': 'flow_rate',
         'value': 10,
         'type': 'textbox'}
    ]

HIGH_SCORE_RESPONSE = 'Immediately inform medical team'

INCORRECT_EWS_DATA = {
    'respiration_rate': 9999,
    'indirect_oxymetry_spo2': 9999,
    'blood_pressure_systolic': 9999,
    'blood_pressure_diastolic': 9999,
    'pulse_rate': 9999,
    'body_temperature': 9999,

}

GCS_SCORE_15_DATA = {
    'eyes': 4,
    'verbal': 5,
    'motor': 6
}

HEIGHT_DATA = {
    'height': 1.8
}

WEIGHT_DATA = {
    'weight': 55
}

BLOOD_PRODUCT_DATA = {
    'vol': 15,
    'product': 'rbc'
}

BLOOD_SUGAR_DATA = {
    'blood_sugar': 5
}

BRISTOL_STOOL_DATA = {
    'bowel_open': 'no',
    'nausea': 'no',
    'vomiting': 'no',
    'quantity': 'medium',
    'colour': 'brown',
    'bristol_type': 'type 1',
    'offensive': 'no',
    'strain': 'no',
    'laxatives': 'no',
    'samples': 'none',
    'rectal_exam': 'no'
}

POSTURAL_BLOOD_PRESSURE_DATA = {
    'systolic_sitting': 120,
    'diastolic_sitting': 80,
    'systolic_standing': 130,
    'diastolic_standing': 90
}
