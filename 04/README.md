## Code Challenge 04 - Twitter data analysis Part 1: get the data

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Write a class to retrieve tweets from the Twitter API 

In this 3 part challenge your will analyze Twitter Data. In this challenge we will automate the retieval of data. Part 2 we will task you with finding similar tweeters, and Part 3 we will do a full sentiment analysis.

Example output: 

	$ python tweets.py

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
	# if so make sure you update the requirements.txt with pip freeze 

	# add your twitter API tokens in config.py 
	$ cp config-template.py config.py

	# start to code
	$ cp tweets-template.py tweets.py

### The challenge

* Define a class that takes a Twitter handle / user in its constructor. Create an instance variable to hold the last n (100, 200, ...) tweets of this user. Use tweepy (or alternative package) to query the Twitter's API. 

	* New to OOP or bit rusty? You can read [our OOP post](http://pybit.es/oop-primer.html).

	* Optional (but Pythonic): use Python's data model to implement len() and getitem() to create an iterator over the tweets. We did a post on that as well if you need help, see [here](http://pybit.es/python-data-model.html).

* Optional (but recommended): tokenize / clean the data. We leave this one open (we just started NLP ...) so we learn from this week solutions to start with a clean data set next week for Part 2.

* Save the data in data/handle (txt, json, format you find convenient).

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
