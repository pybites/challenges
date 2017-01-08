## Challenge 01: find the word with the highest (Scrabble) value

### Intro

Welcome to [PyBites challenges](http://pybit.es/category/challenges) where we post a challenge every week on Monday and push a (refactored) solution on Friday. The goal is to learn / improve our Python coding skills. We are firm believers that you have to get your hands on the keyboard as soon as possible. Making mistakes, doing code reviews. Using github we encourage people to take the code challenges and to make pull requests so we can comment each others code and learn even more.

### How does it work?

You clone this repo, then every week you clone the branch of the exercise:

	$ git pull origin ch<sequence>_exercise

You branch off your solution branch:

	$ git checkout -b ch01_exercise_<github_user>

You run the tests I will include and when you have a working solution you can submit a pull request. Pythonic solutions will be mentioned in our Friday review.
	
### This week's challenge

#### Calculate the dictionary word that would have the most value in Scrabble

Read in dictionary.txt (a copy of /usr/share/dict/words on my Mac) and calculate the word that has the most value in Scrabble based on LETTER_SCORES I will import for you in main script. Note that no PyPI modules need to be installed, just use stdlib for this. Run the test_wordvalue.py to verify your methods are correct. Use wordvalue.py where I put some stubs you should use (to make the tests pass).

### Feedback

We are still experimenting with how to best present the challenges and with github collaboration overall. We like the idea of having tests to verify the results, getting closer to TDD. Also Github pull requests make it easy to have the greater community participate, not just Julian and myself. 

Thanks for trying.
