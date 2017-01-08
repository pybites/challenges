# PyBites Challenges

Every Monday we release a challenge [on our blog](http://pybit.es).

If this is your first time around, clone this repo: 

	$ git clone https://github.com/pybites/challenges.git pybites_challenges && cd $_

After that you can pull the exercise branch with. 

I will use ch01_exercise below as an example. 
Change the branch name and test_<name>.py if you are doing this for another exercise.

	$ git pull origin ch01_exercise
	$ git checkout ch01_exercise
	$ cd ch01

Branch off your solution:

	$ git checkout -b ch01_exercise_<github_user>
	# code ...
	# verify: 
	$ python test_wordvalue.py
	$ git add .
	$ git commit -m "my solution blabla ..."

If you want to submit the solution do a pull request:

	$ git request-pull (#TODO)
