## Code Challenge 02 - Word Values Part II - a simple game

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Given a random set of 7 letters build the most valuable word 

Building upon the [last challenge](http://pybit.es/codechallenge01.html) this week part II: a simple game.

### Requirements / steps

* this will be a console game. Import SCRABBLE_POUCH from data.py to get the complete pool of letters

* draw 7 random letters from SCRABBLE_POUCH (see [Scrabble rules](http://www.scrabblepages.com/scrabble/rules/), this will be a lite version, no board and no bonus points, keeping it simple).

* ask the user to form a word with the 7 letters. 
	* check that only letters of the draw are used. 
	* check if a valid word, for that import the DICTIONARY set from data.py (I provided a set for O(1) lookup)

* now the checker side: get all permutations for the 7 letter draw (hint: [itertools.permutations](http://pybit.es/itertools-examples.html))

* cross check the collection built in last step with the dictionary to filter out valid words only.

* calculate the word values of each of the remaining words, you can use code from [last challenge](http://pybit.es/codechallenge01.html) here. Import LETTER_VALUES from data.py to use in your calculations.

* present the user with the highest vs the one he/she created and calculate a simple score (user word value / max word value).
	* optional variation: give the user n attempts (defined as a constant NUM_ATTEMPTS) and feedback each time how far he/she is off from the max score.

### Bonus

This might be quite a challenge, but it is also a highly addictive one I think. If you want to get creative you can further build this out:

* keep scores in a shelve (or sqlite3 db) and feedback each game if user reached a new max score.

* work with hints (penalizing end score).

* convert this in a pygame / web app. / Android app

### Possible console output 

### Good luck!

We can't wait for your inputs! 

Remember: there is no best solution, only learning and getting better Pythonistas.

And above all: have fun!! 

---

* [Corresponding blog post](http://pybit.es/codechallenge02.html)

* [Fork this project and start coding](https://github.com/pybites/challenges)

### About PyBites Code Challenges

Background in [our intro post](http://pybit.es/codechallenge01.html).
