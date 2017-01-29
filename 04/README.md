## Code Challenge 04 - Twitter data analysis Part 1: get the data

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Write a class to retrieve tweets from the Twitter API 

In this 3 part challenge you will analyze Twitter Data. This week we will automate the retrieval of data. In Part 2 we will task you with finding similar tweeters, and for Part 3 you will do a full sentiment analysis.

### Get ready

Start coding by [forking our challenges repo](https://github.com/pybites/challenges):

	$ git clone https://github.com/pybites/challenges
	
If you already forked it [sync it](https://help.github.com/articles/syncing-a-fork/):

	# assuming using ssh key
	$ git remote add upstream git@github.com:pybites/challenges.git 
	$ git fetch upstream
	# if not on master: 
	$ git checkout master 
	$ git merge upstream/master

### Setup virtual environment and install requirements

	$ cd 04
	$ python3 -m venv venv
	# = py3 (might need virtualenv for py2 env)

	$ source venv/bin/activate 
	# install tweepy (and its depencencies)
	$ pip install -r requirements.txt

	# if you want to use another package like twython, feel free to do so

	# get your API keys from Twitter - https://apps.twitter.com 
	$ cp config-template.py config.py
	# paste the keys in config.py

	# choose a template
	$ cp usertweets-help.py usertweets.py
	# or 
	$ cp usertweets-nohelp.py usertweets.py
	# code

### The challenge

* Define a class called UserTweets that takes a Twitter handle / user in its constructor. it also receives an optional max_id parameter to start from a particular tweet id. 
* Create a tweepy API object using the tokens imported from config.py (again, you can use another package if you prefer).

* Create an instance variable to hold the last 100 tweets of the user. 

* Implement len() and getitem() magic (dunder) methods to make the UserTweets object iterable.

* Save the generated data as CSV in the data subdirectory: data/some_handle.csv, columns: id_str,created_at,text

### Background

* We posted two articles this week you might find useful in this context: [oop primer](http://pybit.es/oop-primer.html) and [Python's data model](http://pybit.es/python-data-model.html). 

* If you decide to use Tweepy, you might want to check its [API reference](http://docs.tweepy.org/en/v3.5.0/api.html).

### Tests

For developers that like to work towards tests we included test_usertweets.py:

	$ python test_usertweets.py
	...
	----------------------------------------------------------------------
	Ran 3 tests in 0.001s

	OK

### Example output

We used a namedtuple here, this is not required. Also note the tweets can differ, yet in the unittests we test a fix set (using the optional max_id parameter in the constructor):

	$ python
	>>> from usertweets import UserTweets
	>>> pybites = UserTweets('pybites')
	>>> len(pybites)
	100
	>>> pybites[0]
	Tweet(id_str='825629570992726017', created_at=datetime.datetime(2017, 1, 29, 9, 0, 3), text='Twitter digest 2017 week 04 https://t.co/L3njBuBats #python')
	>>> ^D
	(venv) [bbelderb@macbook 04 (master)]$ ls -lrth data/
	...
	-rw-r--r--  1 bbelderb  staff    14K Jan 29 21:49 pybites.csv
	(venv) [bbelderb@macbook 04 (master)]$ head -3 data/pybites.csv
	id_str,created_at,text
	825629570992726017,2017-01-29 09:00:03,Twitter digest 2017 week 04 https://t.co/L3njBuBats #python
	825267189162733569,2017-01-28 09:00:05,Code Challenge 03 - PyBites blog tag analysis - Review https://t.co/xvcLQBbvup #python

### Good luck!

Remember: there is no best solution, only learning more and better Python.

Enjoy and we're looking forward reviewing on Friday all the cool / creative / Pythonic stuff you come up with.

Have fun!

---

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/).

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared on our blog as [this article](http://pybit.es/codechallenge04.html).
