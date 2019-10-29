#!/usr/bin/env python

from setuptools import setup

setup(
    name='ansible-toolset',
    version='0.7.0',
    description='Useful Ansible toolset',
    url='https://github.com/krzysztof-magosa/ansible-toolset',
    author='Krzysztof Magosa',
    author_email='krzysztof@magosa.pl',
    license='GPLv3',
    packages=[
        'ansible_toolset',
        'ansible_toolset/ansible'
    ],
    scripts=[
        'bin/ats-vault'
    ],
    install_requires=[
        'peewee>=2.8.5'
    ]
)
