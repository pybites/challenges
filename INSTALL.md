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

### III. Optional - Detaching the fork

* One small issue with working with a forked repo is that Github wont actually recognize any of your activity. If you want to see your activity follow these steps. However be warned that it will prevent you from creating pull-requests.

1. On Github go to the settings page of your forked repo.
2. In the Danger Zone click on the Delete this repository button.
3. Type the full name of the repo in the box and click the button.
4. Create a new repo with the same name as the original repo.
5. Push the repo to Github

		$ git push origin master

---

## Feedback

* If you want to share your solution, please use the comments of [our review posts](http://pybit.es/pages/challenges.html).

* If you have ideas for new challenges or issues with existing ones, please use the [issues page](https://github.com/pybites/challenges/issues).

---

Remember: there is no best solution, only learning more/ better Python. We're looking forward reviewing our and your solutions.
Good luck and have fun!

Keep Calm and Code in Python!

-- Bob and Julian
