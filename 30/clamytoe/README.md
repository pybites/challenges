# Comic Snagger (*comic_snagger*)
> *Python script for downloading comic book images and converting them into a compressed comic book format.*

![Python version][python-version]
[![Build Status][travis-image]][travis-url]
[![BCH compliance][bch-image]][bch-url]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

This app was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

Python script for downloading comics from [readcomics.io](https://www.readcomics.io). Run the script and respond to the prompts and it will download all of the images for the comic that you want.

### Initial setup
You will need to have **requests** and **BeautifulSoup4** in order to use. It's written for Python 3.6 because I love working with *f-strings* and its about time everyone upgraded.

```bash
cd Projects
git clone https://github.com/clamytoe/comic_snagger.git
cd comic_snagger
```

#### Anaconda setup
```bash
conda env create
```

#### Regular Python setup
```bash
pip install -r requirements.txt
```

#### Final setup
```bash
activate comic_snagger # or source activate comic_snagger
pip install -e .
```

## Usage
```bash
comic_snagger
```

Once you've started downloading a comic, it will continue until it's done. If you stop it at any point, no need to worry. The script will continue where it left off. Just start the same comic once again and let it do its thing.

## Contributing
Contributions are very welcome. Tests can be run with with `pytest -v`, please ensure that all tests are passing before submitting a pull request. I have also included the following packages that should be used:
* black
* isort
* mypy

I am not adhering to them strictly, but try to clean up what's reasonable.

## License
Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "comic_snagger" is free and open source software.

## Issues
If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.


[python-version]:https://img.shields.io/badge/python-3.6.6-brightgreen.svg
[travis-image]:https://travis-ci.org/clamytoe/comic_snagger.svg?branch=master
[travis-url]:https://travis-ci.org/clamytoe/comic_snagger
[bch-image]:https://bettercodehub.com/edge/badge/clamytoe/comic_snagger?branch=master
[bch-url]:https://bettercodehub.com/
[issues-image]:https://img.shields.io/github/issues/clamytoe/comic_snagger.svg
[issues-url]:https://github.com/clamytoe/comic_snagger/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/comic_snagger.svg
[fork-url]:https://github.com/clamytoe/comic_snagger/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/comic_snagger.svg
[stars-url]:https://github.com/clamytoe/comic_snagger/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/comic_snagger.svg
[license-url]:https://github.com/clamytoe/comic_snagger/blob/master/LICENSE
