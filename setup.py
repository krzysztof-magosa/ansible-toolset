#!/usr/bin/env python

import pip.download
from pip.req import parse_requirements
from setuptools import setup

setup(
    name='ansible-toolset',
    version='0.1.1',
    description='Useful Ansible toolset',
    url='https://github.com/krzysztof-magosa/ansible-toolset',
    author='Krzysztof Magosa',
    author_email='krzysztof@magosa.pl',
    license='GPLv3',
    scripts=[
        'bin/ats-vault'
    ]
)
