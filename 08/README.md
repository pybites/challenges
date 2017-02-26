## Code Challenge 08 - House Inventory Tracker 

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

A new week, time for some coding! Here's the idea - we're keeping it simple.

Having home and contents insurance requires you to accurately indicate the value of the items in your house. The idea came to me when doing this for myself. 

What if I could write a simple program that allowed me to create a list of rooms in my house and for each room a list of items along with their dollar values? 

### House Inventory Tracker Requirements

* Create a list of rooms (doesn't have to use the list type).

* Each room in your rooms list needs to contain at least 5 items (ie, TV, couch, table, etc) and the relative dollar value of each item.

* The script you will write will print out each room along with the individual items and values. This needs to be properly formatted, eg: no printing a dict as is.

### Bonus

These are bonus features. Not required but cool to try if you're interested:

* Create some sort of program shell with a menu system around this. ie, "Which room would you like to list out?"

* If you're really game, allow users to create rooms and update information. 

* You could even make an API with Flask or your preferred framework

* Print the total dollar value of each room and the entire house.

* Have persistent storage of the data. sqlite3 = stdlib and light-weight, but feel free to use your preferred DB / module.

### To follow along with our challenges

Start coding by [forking our challenges repo](https://github.com/pybites/challenges):

    $ git clone https://github.com/pybites/challenges

If you already forked it [sync it](https://help.github.com/articles/syncing-a-fork/):

    # assuming using ssh key
    $ git remote add upstream git@github.com:pybites/challenges.git
    $ git fetch upstream
    # if not on master:
    $ git checkout master
    $ git merge upstream/master
    $ cd 08
    # open inventory.py (just a blank file for this challenge)
	# code

Remember: there is no best solution, only learning more/ better Python. We're looking forward reviewing our and your solutions end of this week. Good luck and have fun!

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared on our blog as [this article](http://pybit.es/codechallenge08.html).
