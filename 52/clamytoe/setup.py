"""
setup.py

Setup for installing the package.
"""
from io import open
from os import path

from setuptools import find_packages, setup

import pomodoro_timer

VERSION = pomodoro_timer.__version__
AUTHOR = pomodoro_timer.__author__
EMAIL = pomodoro_timer.__email__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pomodoro",
    version=VERSION,
    description="Simple no frills Pomodoro Timer that I made for my 100 day coding challenge. (pomodoro_timer)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clamytoe/pomodoro_timer",
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6.5",
    ],
    keywords="python utility",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pytest>=3.6.2"],
    license="MIT",
    entry_points={"console_scripts": ["pomodoro=pomodoro_timer.app:main"]},
    project_urls={
        "Bug Reports": "https://github.com/clamytoe/pomodoro_timer/issues",
        "Source": "https://github.com/clamytoe/pomodoro_timer/",
    },
)
