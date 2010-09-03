#!/usr/bin/env python
from setuptools import setup

setup(
    name='breadpy',
    version='0.1',
    packages=['breadpy'],
    package_dir={'':'src'},
    install_requires=[
        'sqlalchemy',
        'bottle',
        'WTForms',
        ],
    )
    
        

