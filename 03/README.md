## Code Challenge 03 - PyBites blog tag analysis

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Given our RSS feed what tags does PyBites mostly use and which tags should be merged (based on similarity)?

Example output: 

	$ python tags.py

	* Top 10 tags:
	python               10
	learning             7
	tips                 6
	tricks               5
	github               5
	cleancode            5
	best practices       5
	pythonic             4
	collections          4
	beginners            4

	* Similar tags:
	game                 games
	challenge            challenges
	generator            generators

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

Use one of the templates:

	$ cd 03
	$ cp tags-help.py tags.py
	# or:
	$ cp tags-nohelp.py tags.py
	# code

	# run the unittests (optional)
	$ python test_tags.py
	...
	----------------------------------------------------------------------
	Ran 3 tests in 0.155s

	OK


### Requirements / steps

* As we update our blog regularly we provided a recent copy of our feed in the 03 directory: rss.xml. We also provided a copy of tags.html for verification (used by unittests in test_tags.py).

* Both templates provide 3 constants you should use: 

		TOP_NUMBER = 10
		RSS_FEED = 'rss.xml'
		SIMILAR = 0.87

* Rest is documented in the methods docstrings. Again use tags-help.py if you need more guidance, tags-nohelp.py is for the more experienced and/or if you want more freedom. Same goes for tests: use them if you need them.

* Talking about freedom feel free to use our [live feed](http://pybit.es/feeds/all.rss.xml) but then the tests will probably break.

* Hint: for word similarity feel free to use NLTK, or your favorite language processing tool. However, stdlib does provide a nice way to do this. Using this method we came to 0.87 as a threshold to for example not mark 'python' and 'pythonic' as similar. 

### Good luck!

Remember: there is no best solution, only learning more and better Python.

Enjoy and we're looking forward reviewing on Friday all the cool / creative / Pythonic stuff you come up with.

Have fun!

---

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/).

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared on our blog as [this article](http://pybit.es/codechallenge03.html).
