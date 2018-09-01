#! /usr/bin/env python

import sys
from setuptools import setup

if sys.argv[-1] == "setup.py":
	print("To install, run \'pip install ./toptennews\'")

if __name__ == "__main__":
	setup(
	name = "toptennews",
        author ='Asutosh Sahoo',
        author_email = 'asutoshsahoo786@gmail.com',
        version = '1.0',
        packages = ['toptennews'],
        install_requires = ['praw'],
        entry_points = {
        	'console_scripts' : [
        		'toptennews = toptennews.main:main'
        	]
        }
        )