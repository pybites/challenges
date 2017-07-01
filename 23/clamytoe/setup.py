#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='pyTrack',
    version='0.1.2',
    author='Martin Uribe',
    author_email='clamytoe@gmail.com',
    url='https://github.com/clamytoe/pyTrack',
    description='Simple project/task time tracker for Python 3',
    long_description='Helps you keep track of how much time you spend on your projects and tasks. A sqlite database '
                     'is used to track your time logs, and it is kept simply by only implementing as few commands as '
                     'needed to get a full featured application. You can add/remove multiple projects, start/stop '
                     'tracking any of them, or completely reset the database to start with a clean slate',
    license='MIT',
    packages=['pytrack'],
    keywords='project tracker peewee click maya',
    py_modules=[
        'main',
        'pytrack.models',
        'pytrack.pytrack',
    ],
    install_requires=[
        'click',
        'maya',
        'peewee',
    ],
    entry_points='''
        [console_scripts]
        pytrack=main:main
    ''',
)
