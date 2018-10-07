# Pomodoro Timer (*pomodoro*)
> *Simple no frills Pomodoro Timer that I modified and updated for the Pybites coding challenge #52.*

![Python version][python-version]
[![Build Status][travis-image]][travis-url]
[![BCH compliance][bch-image]][bch-url]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

NOTE: This app was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

Since the application plays local system sound files, this project only works for those that are using Linux Mint. I'm using Mint 19 with Cinnamon, so not even sure if it would work on any other setup. If anyone one would like to add support for other platforms, PR's are welcome.

I've added a config file that could be modified with your own sound files and player.

### Initial setup
```bash
cd Projects
git clone https://github.com/clamytoe/pomodoro_timer.git
cd pomodoro_timer
```

#### Anaconda setup
If you are an Anaconda user, this command will get you up to speed with the base installation.
```bash
conda env create
conda activate pomodoro_timer
```

#### Regular Python setup
If you are just using normal Python, this will get you ready, but I highly recommend that you do this in a virtual environment. There are many ways to do this, the simplest using *venv*.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Final setup
```bash
pip install -e .
```

## Usage
The utility is easy to use. For instance, to work on a project for the next 4 hours. You would use the following command.
```bash
pomodoro -d 4
```

## Help
For more options, use the built in help feature:
```bash
pomodoro --help
usage: pomodoro [-h] [-d DURATION] [-b BREAKS] [-i INTERVAL]

Pomodoro Productivity Timer

optional arguments:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        How long you going to work for, in hours
  -b BREAKS, --breaks BREAKS
                        How long the breaks should be
  -i INTERVAL, --interval INTERVAL
                        Minutes to work before taking a break
```
## Contributing
Contributions are very welcome. Tests can be run with with `pytest -v`, please ensure that all tests are passing before submitting a pull request. I have also included the following packages that should be used:
* black
* isort
* mypy
* pyflakes
* pylint

I am not adhering to them strictly, but try to clean up what's reasonable.

## License
Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "pomodoro_timer" is free and open source software.

## Issues
If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog
* **v0.2.1** Modified it to exit the program after 8 work cycles and added type hinting.
* **v0.2.0** FIXED: Bug where config file was not being found when program was not executed from the project's directory.
* **v0.1.9** Modified logging config so that log level INFO messages would not show up in the console.
* **v0.1.8** Started logging all of the steps taken so that I can aggregate a possible report feature later on.
* **v0.1.7** Added default values so that the program can be run without parameters.
* **v0.1.6** Added ability for user to be able to initiate the interval and break cycles.
* **v0.1.5** Enabled BetterCodeHub and Travis CI integration.
* **v0.1.4** Refactored in order to be able to increase test coverage.
* **v0.1.3** Moved system configurable settings to a separate configuration file.
* **v0.1.2** Added argparse in order to be able and modify key variables on the fly.
* **v0.1.1** Modified my initial Jupyter Notebook code to run from the command line.
* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.6.5-brightgreen.svg
[travis-image]:https://travis-ci.org/clamytoe/pomodoro_timer.svg?branch=master
[travis-url]:https://travis-ci.org/clamytoe/pomodoro_timer
[bch-image]:https://bettercodehub.com/edge/badge/clamytoe/pomodoro_timer?branch=master
[bch-url]:https://bettercodehub.com/
[issues-image]:https://img.shields.io/github/issues/clamytoe/pomodoro_timer.svg
[issues-url]:https://github.com/clamytoe/pomodoro_timer/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/pomodoro_timer.svg
[fork-url]:https://github.com/clamytoe/pomodoro_timer/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/pomodoro_timer.svg
[stars-url]:https://github.com/clamytoe/pomodoro_timer/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/pomodoro_timer.svg
[license-url]:https://github.com/clamytoe/pomodoro_timer/blob/master/LICENSE
