## Code Challenge 07 - Twitter data analysis Part 3: sentiment analysis

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Perform a sentiment analysis on a popular topic on Twitter

A new week, more coding! You are free to pick a topic. This can be a trend, news or movie. We will take latter:

> How do Tweeters react on [Fifty Shades Darker](http://www.imdb.com/title/tt4465564/?ref_=nv_sr_1), positive or negative?

### Getting ready

* Register an Twitter app if not done already to get keys, put those in config.py (copying the config-template.py)

* Make a virtual environment and pip install Twython (to follow along with our approach just do pip install -r requirements.txt)

* We have provided a getting_data.py script (from [Joel Grus](https://github.com/joelgrus/data-science-from-scratch/blob/master/code-python3/getting_data.py)) that uses the Twitter [Streaming APIs](https://dev.twitter.com/streaming/overview) to collect tweets, run it as follows. It takes 1000 tweets, adjust as necessary (this is also an experiment for us!)

		$ python getting_data.py Fifty Shades Darker
		# replacing with your topic of interest
		# generates data_unix_timestamp.json

* If you prefer Tweepy, you can use this [article/ script](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/) (and pip install that library ...)

* The script you will write is sentiment.py, it contains some code to read the stored json back in memory:

		$ python sentiment.py data_1487544849.json

* Clean up the data, we did some of this in [part 2](http://pybit.es/codechallenge05_review.html) of this challenge series.

* The sentiment analysis ... is the audience positive or negative? We will try [TextBlob](https://textblob.readthedocs.io/en/dev/) for this, use any (Python) tools you prefer ...

### To follow along with our challenges

Start coding by [forking our challenges repo](https://github.com/pybites/challenges):

    $ git clone https://github.com/pybites/challenges

If you already forked it [sync it](https://help.github.com/articles/syncing-a-fork/):

    # assuming using ssh key
    $ git remote add upstream git@github.com:pybites/challenges.git
    $ git fetch upstream
    # if not on master:
    $ git checkout master
    $ git merge upstream/master
    $ cd 07
	$ cp sentiment-template.py sentiment.py
    # if you want to follow along with our recommended libraries (assuming py >= 3.3)
    $ python -m venv venv
    $ source venv/bin/activate'
    $ pip install -r requirements.txt
    # code

Remember: there is no best solution, only learning more/ better Python. We're looking forward reviewing our and your solutions end of this week. Good luck and have fun!

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared on our blog as [this article](http://pybit.es/codechallenge07.html).
