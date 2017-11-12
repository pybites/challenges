#! /usr/bin/env python

import sys
from setuptools import setup

if sys.argv[-1] == "setup.py":
	print("To install, run \'pip install ./weeklychallenges\'")

if __name__ == "__main__":
	setup(
	name = "weeklychallenges",
        author ='Asutosh Sahoo',
        author_email = 'asutoshsahoo786@gmail.com',
        version = '1.0',
        packages = ['weeklychallenges'],
        install_requires = ['praw'],
        entry_points = {
        	'console_scripts' : [
        		'weeklychallenges = weeklychallenges.main:main'
        	]
        }
        )