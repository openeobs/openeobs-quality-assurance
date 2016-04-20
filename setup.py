from setuptools import setup

setup(
    name='openeobs_quality_assurance',
    version='0.1',
    description='Quality assurance helpers for open-eObs',
    author='NeovaHealth',
    author_email='office@neovahealth.co.uk',
    url='https://github.com/NeovaHealth/openeobs-quality-assurance',
    provides=['openeobs_quality_assurance'],
    packages=[
        'openeobs_mobile',
        'openeobs_selenium'
    ],
    include_package_data=True,
    license='GPL',
    zip_safe=True
)