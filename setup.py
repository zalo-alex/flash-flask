from setuptools import setup

setup(
    name='flash_flask',
    version='1.0.0',
    description='Make Flask Better ',
    author='Alex ZALO',
    packages=['flash_flask'],
    install_requires=[
        'Flask==3.0.0'
    ],
    extras_require={
        'mysql': ['mysql-connector-python==8.2.0'],
    },
)
