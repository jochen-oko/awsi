#The setup.py file is what ties it all together and tells Python how to handle it.

from setuptools import setup

setup(
    name = 'awsi',
    version = '0.1.1',
    packages = ['awsi'],
    entry_points = {
        'console_scripts': [
            'awsi = awsi.awsi:main'
        ]
    })
