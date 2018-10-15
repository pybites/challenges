from setuptools import setup, find_packages

import cylon

VERSION = cylon.__version__
AUTHOR = cylon.__author__
EMAIL = cylon.__email__

setup(
    name='cylon',
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/clamytoe/Cylon',
    license='MIT',
    author=AUTHOR,
    author_email=EMAIL,
    description='Python object that allows you to access .next() '\
                'and .prev() items from a list.',
)
