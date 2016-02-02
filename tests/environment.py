"""Configuration file for the database"""

DATABASE = 'mobile_qa_db'
URL = 'http://localhost:8069/web?db={database}'.format(database=DATABASE)
ODOO_CLIENT_URL = 'http://localhost:8069'
TEST_DB_NAME = 'openeobs_quality_assurance_db'
USERNAME = 'admin'
PASSWORD = 'admin'
