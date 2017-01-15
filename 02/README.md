## Code Challenge 02 - Word Values Part II - a simple game

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Given a random set of 7 letters build the most valuable word

Using what we've learned [the last challenge](http://pybit.es/codechallenge01.html) this week we build a simple Scrabble-like game (without board):

	Letters drawn: G, A, R, Y, T, E, V
	Form a valid word: gary  << user input
	Word chosen: GARY (value: 8)
	Optimal word possible: GARVEY (value: 13)
	You scored: 61.5

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

	$ cd 02
	$ cp game-TEMPLATE.py game.py
	# code

### Requirements / steps

Last time we provided unittests and a guiding template. We received feedback that this was a bit too stringent. Therefore we provide two templates this time: game-help.py and game-nohelp.py

* We load in the necessary data structures to focus on the game:

		# Note that DICTIONARY is a set for O(1) lookups
		from data import DICTIONARY, LETTER_VALUES, POUCH

* Draw 7 random letters from POUCH.

	As said POUCH is given and contains a distribution of Scrabble letters so that the player gets enough vowels (equally drawing A-Z makes it extremely hard because you need more vowels to make words):

		['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C',
		'D', 'D', 'D', 'D', ...]

* Ask the player to form a word with one or more of the 7 letters of the draw. Validate input for:

		1) all letters of word are in draw;
		2) word is in DICTIONARY.

* Calculate the word value and show it to the player.

	To focus on this challenge we re-use two methods from the previous challenge for this: calc_word_value and max_word_value.

* Calculate the optimal word (= max word value) checking all permutations of the 7 letters of the draw, cross-checking the DICTIONARY set for valid ones. This is a bit more advanced, but allows you to score the player (next).

* Show the player what the optimal word and its value is.

* Give the player a score based on the previous steps, basically: player_score / optimal_score.

### Bonus (not required)

The optimal solution calculation might be a bit difficult for some, that's why we stop here. But if you are feeling creative you might consider expanding this game:

* Keep scores in a shelve (file, db) and notify the player when a new record is reached.

* Work with hints and bonuses: hints cost x points, give a bonus of y points, for example when a 7 letter word is created (complete draw exhausted).

* Make a simple web, mobile app or pygame.

### Good luck!

Remember: there is no best solution, only learning more and better Python.

Enjoy and we're looking forward reviewing on Friday all the cool / creative / Pythonic stuff you come up with.

Have fun!

---

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/).

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared on our blog as [this article](http://pybit.es/codechallenge02.html).
