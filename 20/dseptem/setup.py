from distutils.core import setup

setup(
    name='Rooms',
    version='0.5',
    author='Dante Septem',
    author_email='d.septem@gmail.com',
    packages=['rooms', 'tests'],
    scripts=['rooms/rooms.py'],
    url='http://www.google.com',
    license='LICENSE',
    description='Adventure game framework',
    long_description=open('README.rst').read(),
    install_requires=[],
)