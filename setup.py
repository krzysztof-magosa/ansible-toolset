#!/usr/bin/env python

import pip.download
from pip.req import parse_requirements
from setuptools import setup

setup(
    name='ansible-toolset',
    version='0.1.0',
    description='Useful Ansible toolset',
    url='https://github.com/krzysztof-magosa/ansible-toolset',
    author='Krzysztof Magosa',
    author_email='krzysztof@magosa.pl',
    license='GPLv3',
    install_requires=[
        str(pkg.req) for pkg in parse_requirements(
            'requirements.txt',
            session=pip.download.PipSession()
        )
    ],
#    tests_require=[
#        str(pkg.req) for pkg in parse_requirements(
#            'test-requirements.txt',
#            session=pip.download.PipSession())
#    ],
#    packages=['ansible_toolset'],
    scripts=[
        'bin/ats-vault'
    ]
)
