#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()


if __name__ == "__main__":
    setup(
        name='dailyprogrammer',
        version='0.1',
        author='Shibasis Patel',
        author_email='shibasishpatel@live.in',
        packages=['dailyprogrammer'],
        entry_points={
            'console_scripts': [
                'dailyprogrammer = dailyprogrammer.dailyprogrammers:main',
            ]
        },
        install_requires=['praw']
    )
