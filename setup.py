from setuptools import setup

setup(
    name='flash_flask_python',
    version='1.0.5',
    description='Make Flask Better',
    author='Alex ZALO',
    install_requires=[
        'Flask==3.0.0'
    ],
    extras_require={
        'mysql': ['mysql-connector-python==8.2.0'],
    },
)
