## Code Challenge 09 - Give the With Statement some Love and Create a Context Manager

> This week, each one of you has a homework assignment ... - Tyler Durden (Fight club)

A new week, time for some coding! 

This week we have a free form exercise. After reading [Dan's great article on the with statement](https://dbader.org/blog/python-context-managers-and-with-statement) we thought it would be cool to ask our PyBites community to come up with creative uses of the with statement. This week you get to implement your own Context Manager.

You can either:

* Define a class implementing the \_\_enter\_\_ and \_\_exit\_\_ methods. Dan shows an Indenter class as example in his article.

* Use the nice [@contextmanager decorator](https://docs.python.org/3.6/library/contextlib.html#contextlib.contextmanager) shortcut. 

Have fun!

### Other resources

* [with statement](https://docs.python.org/3.6/reference/compound_stmts.html#with)

* [PEP 343 -- The "with" Statement](https://www.python.org/dev/peps/pep-0343/)

* [contextlib — Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)

* [Python with Context Managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)

* If beginner you might need to read up on some more advanced concepts: [Generators](https://wiki.python.org/moin/Generators) and [Decorators](https://wiki.python.org/moin/PythonDecorators), also covered in chapters 3 and 7 of the [Python tips book](http://book.pythontips.com/en/latest/index.html). 

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
    $ cd 09
    # open withlove.py (just a blank file for this challenge)
    # code

Remember: there is no best solution, only learning more/ better Python. We're looking forward reviewing our and your solutions end of this week. Good luck and have fun!

---

### About PyBites Code Challenges

More background in our [first challenge article](http://pybit.es/codechallenge01.html).

Above challenge appeared on our blog as [this article](http://pybit.es/codechallenge09.html).
