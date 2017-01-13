## Code Challenge 02 - Word Values Part II - a simple game

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

### Given a random set of 7 letters build the most valuable word 

Using what we've learned [the last challenge](http://pybit.es/codechallenge01.html) this week we build a simple Scrabble-like game (without board):

	Letters drawn: G, A, R, Y, T, E, V
	Form a valid word: gary
	Word chosen: GARY with value: 8
	Max word: garvey with value: 13
	You scored: 61.5

### Get ready

Start coding by [forking our challenges repo](https://github.com/pybites/challenges) (if done already, [sync the fork](https://help.github.com/articles/syncing-a-fork/))

### Requirements / steps

* Last time we provided unittests and a guiding template. We received feedback that this did not allow sufficient freedom. Therefore we provide a basic and more advanced template this challenge.

* We do load in the necessary data structures to focus on the game:

		# Note that DICTIONARY is a set for O(1) lookup
		from data import DICTIONARY, LETTER_VALUES, POUCH

* Draw 7 random letters from POUCH.

	As said the pouch is given and contains a distribution of Scrabble letters so that the player gets enough vowels (A-Z makes it extremely hard because you need more vowels):

		['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 
		'D', 'D', 'D', 'D', ...]

* Ask the player to form a word with one or more of the 7 letters of the draw. Validate input for a) valid letters (= in draw set), b) valid word (in DICTIONARY)

* Calculate the word value. To no re-invent the wheel (and focus on this challenge) 2 methods of the previous challenge are provided in both templates: a) calc_word_value(word) and b) max_word_value(words) 

* (more advanced) calculate the optimal word checking all permutations of the 7 letters of the draw (cross-checking DICTIONARY for valid ones).

* Show the player what the max possible value word (and score) is and the endresult: player_score / optimal_score

### Bonus (not required)

The optimal solution calculation might be a bit difficult for some, that's why we stop here. But if you are feeling creative you might consider adding:

* Keep scores in a shelve (file, db) and notify player when a new record is reached.

* Work with hints and bonuses: hints cost x points, a bonus could be when player uses all letters from the draw.

* Make it in a simple web or mobile app.

### Good luck!

Remember: there is no best solution, only learning and getting better Pythonistas.

Enjoy and we're looking forward seeing all the great stuff you will be building. Have fun!

Again start coding by [forking our challenges repo](https://github.com/pybites/challenges) (if done already, [sync the fork](https://help.github.com/articles/syncing-a-fork/))

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared [here](http://pybit.es/codechallenge02.html).
