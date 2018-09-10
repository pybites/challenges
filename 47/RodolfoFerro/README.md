# Twitter hashtags visualization

Main goals:

1. Gather Twitter user's hashtags and analyze them.
2. Visualize data in a creative way.

## Setup

First clone the repo. I'm using [Python 3.6](https://www.python.org/downloads/) with the following packages:

* [NumPy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org/)
* [Tweepy](http://www.tweepy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [PIL](https://python-pillow.org/)
* [Wordcloud](http://amueller.github.io/word_cloud/)

To install all dependencies create a virtual env and run:

```bash
pip install -r requirements.txt
```

Now that we have all the requirements, we need to create a Twitter App.

### Creating a Twitter App

In order to extract tweets for a posterior analysis, we need to access to our Twitter account and create an app. The website to do this is [https://apps.twitter.com/](https://apps.twitter.com/). (If you don't know how to do this, you can follow this [quick tutorial video](https://www.youtube.com/watch?v=6wAHcHGgpFU) to create an account and an application.)

From this app that we're creating we will save the following information the [`credentials.py`](https://github.com/RodolfoFerro/TwHashtagsVis/blob/master/scripts/credentials.py) script:
* **Consumer Key (API Key)**
* **Consumer Secret (API Secret)**
* **Access Token**
* **Access Token Secret**

The content of this script is the following:
```python
# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Access keys for Twitter App.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

# Consumer:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Access:
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

```

## How to use it

### Wanna see it in action?

Feel free to check the [demo notebook](https://github.com/RodolfoFerro/TwHashtagsVis/blob/master/scripts/Twitter%20hashtags%20visualization.ipynb) from the repo or directly from [Jupyter nbviewer](https://nbviewer.jupyter.org/github/RodolfoFerro/TwHashtagsVis/blob/master/scripts/Twitter%20hashtags%20visualization.ipynb)!

### Example of visualization (mask/wordcloud)

An example of visualization of hashtags from [@pybites](https://twitter.com/pybites) using a mask of the Twitter bird is the following one:

<img src="https://raw.githubusercontent.com/RodolfoFerro/TwHashtagsVis/master/imgs/twird.png" width="50%"><img src="https://raw.githubusercontent.com/RodolfoFerro/TwHashtagsVis/master/imgs/wordcloud_twird.png" width="50%">
