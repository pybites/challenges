"""
setup.py

Setup for installing the package.
"""
from setuptools import find_packages, setup

import comic_snagger

VERSION = comic_snagger.__version__
AUTHOR = comic_snagger.__author__
EMAIL = comic_snagger.__email__

setup(
    name="comic_snagger",
    version=VERSION,
    packages=find_packages(),
    url="https://github.com/clamytoe/comic_snagger",
    license="MIT",
    author=AUTHOR,
    author_email=EMAIL,
    description="Python script for downloading comic book images and "
    "converting them into a compressed comic book format. ("
    "comic_snagger)",
    install_requirements=[],
    entry_points="""
        [console_scripts]
        comic_snagger=comic_snagger.comic_snagger:main
    """,
)
