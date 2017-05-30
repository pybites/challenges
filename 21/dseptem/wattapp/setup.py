from distutils.core import setup

setup(
    name='wattapp',
    version='0.4',
    author='Dante Septem',
    author_email='d.septem@gmail.com',
    packages=['wattapp', 'tests'],
    scripts=['wattapp/wattapp.py'],
    url='http://127.0.0.1:5000',
    license='LICENSE',
    description='Wattage Consumption Cost Calculator App',
    long_description=open('README.rst').read(),
    install_requires=['flask', 'wtforms', 'flask_sqlalchemy'],
)