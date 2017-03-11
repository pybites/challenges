## To follow along with our challenges

### I. First time around

* Make your own fork of our [challenges repo](https://github.com/pybites/challenges): use the Fork button at the top right of the page.

* Clone your copy:

		$ git clone https://github.com/<your_user>/challenges

### II. You already cloned your fork

* In this case you need to [sync our new challenge(s)](https://help.github.com/articles/syncing-a-fork/), in your fork directory:

		# assuming using ssh key
		$ git remote add upstream git@github.com:pybites/challenges.git
		$ git fetch upstream

		# if not on master:
		$ git checkout master
		$ git merge upstream/master
		# at this point you are asked to commit the merge

* Have fun :)

		$ cd <challenge-number>
		# edit <template>.py file

---

## Feedback

* If you want to share your solution, please use the comments of [our review posts](http://pybit.es/pages/challenges.html).

* If you have ideas for new challenges or issues with existing ones, please use the [issues page](https://github.com/pybites/challenges/issues).

---

Remember: there is no best solution, only learning more/ better Python. We're looking forward reviewing our and your solutions.
Good luck and have fun!

Keep Calm and Code in Python!

-- Bob and Julian
