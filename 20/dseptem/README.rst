===========
Rooms
===========

Rooms is a humble and simple Framework to create adventure games with Python.

It involves the use of 3 base classes: Room, Actor and Player.

A player has an inventory and moves between Rooms, interacting with Actors.

Actors display text to the Player and may add items to the Player inventory or remove an item while giving another.

Actors are to be thought as NPCs or immobile objects to be interacted with.

The game ends when the Player's "win" attribute is set to True.

Items are merely strings of text added to the Player's inventory, which is a list of strings.

How to start the game
=========

Execute rooms.py with the level.py you created as an argument.

If no argument is provided, rooms.py will try to play the sample level "Dante's Adventure".

How to play
=========

The actions you can take will be numbered, starting from 1.

Explore the rooms and interact with your environment to win!

Dante's Adventure
=========

Included as an example with the Rooms framework.

It contains:

* Three Rooms

* Two actors

* One item


Note PyBites 
=========

Requires Python 3.6 (uses syntax: {**self.actions, **self.moves} which did not work with < 3.6)

To run tests: 

    $ python -m unittest tests.tests
