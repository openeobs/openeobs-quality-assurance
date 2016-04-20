"""Stores data dictionaries for QA testing"""

NO_RISK_EWS_DATA = {
    'respiration_rate': 18,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

LOW_RISK_SCORE_1_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

LOW_RISK_SCORE_2_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

LOW_RISK_SCORE_3_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 36,
    'flow_rate': 8,
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

LOW_RISK_SCORE_4_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 37,
    'flow_rate': 4,
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

LOW_SCORE_RESPONSE = 'Assess Patient'

MEDIUM_RISK_SCORE_3_THREE_IN_ONE_EWS_DATA = {
    'respiration_rate': 18,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'V',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

MEDIUM_RISK_SCORE_4_THREE_IN_ONE_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'No',
    'blood_pressure_systolic': 120,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'V',
    'pulse_rate': 65,
    'body_temperature': 37.5,
}

MEDIUM_RISK_SCORE_5_EWS_DATA = {
    'respiration_rate': 11,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 'nasal',
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 50,
    'body_temperature': 37.5,
    'concentration': 40,
}

MEDIUM_RISK_SCORE_6_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 44,
    'concentration': 60,
    'cpap_peep': 2,
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 50,
    'body_temperature': 37.5,
}

MEDIUM_SCORE_RESPONSE = 'Urgently inform medical team'

HIGH_RISK_SCORE_7_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 45,
    'concentration': 85,
    'niv_ipap': 2,
    'niv_epap': 2,
    'niv_backup': 4,
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 50,
    'body_temperature': 36.0,
}

HIGH_RISK_SCORE_8_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 38,
    'flow_rate': 10,
    'blood_pressure_systolic': 110,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 50,
    'body_temperature': 36.0,
}

HIGH_RISK_SCORE_9_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 99,
    'oxygen_administration_flag': 'Yes',
    'device_id': 'Nasal',
    'flow_rate': 10,
    'blood_pressure_systolic': 100,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 130,
    'body_temperature': 36.0,
}

HIGH_RISK_SCORE_10_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 95,
    'oxygen_administration_flag': 'Yes',
    'device_id': 43,
    'flow_rate': 10,
    'blood_pressure_systolic': 100,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 130,
    'body_temperature': 36.0,
}

HIGH_RISK_SCORE_11_EWS_DATA = {
    'respiration_rate': 24,
    'indirect_oxymetry_spo2': 93,
    'oxygen_administration_flag': 'Yes',
    'device_id': 43,
    'flow_rate': 10,
    'blood_pressure_systolic': 100,
    'blood_pressure_diastolic': 80,
    'avpu_text': 'A',
    'pulse_rate': 130,
    'body_temperature': 36.0,
}

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
