#!/usr/bin/env python
import os

from setuptools import (
    find_packages,
    setup,
)

here = os.path.abspath(os.path.dirname(__file__))


def requirements_copy(requirements_file):
    with open(os.path.join(here, requirements_file)) as rf:
        return [line for line in rf.readlines()]


about = {}
with open(os.path.join(here, 'ja', '__about__.py')) as f:
    exec(f.read(), about)

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name=about.get('__title__'),
    version=about.get('__version__'),
    description=about.get('__description__'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=about.get('__url__'),
    author=about.get('__author__'),
    author_email=about.get('__author_email__'),
    python_requires='>=3.1',
    packages=find_packages(exclude=[
        'docs',
        'tests',
    ]),
    install_requires=requirements_copy('requirements.txt'),
    tests_require=requirements_copy('requirements_test.txt'),
)
