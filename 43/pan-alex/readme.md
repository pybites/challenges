## BBbot

<img src="bbbot.png" width="256" height = "256"/>

This is a general-purpose Slack chat bot (named BBbot). The bot works by:

- Searching Slack events for messages aimed at the bot (i.e., mentions with the tag @bbbot) and feeds the message to a function that handles commands.

- The function searches a dictionary to see if the command exists. If so, it executes the command. If not, it returns a failure message.



### Calling commands:

The bot searches for messages that contain mentions of its name. The bot interprets the word directly after <@bbbot> as the command. The remaining message may be parsed for additional arguments to the command.

My aim was to make the syntax in calling these commands more "natural." Rather than something like:

> <@bbbot> list_add grocery: apples, pears, bananas 

The bot will accept messages like:

> <@bbbot> add apple, pears, and bananas to my grocery list. And make it snappy!


Likewise, more than one keyword can call the same function in some cases. e.g., `hello` may be called by writing "hi", "hello", or "hey", etc. This is far from perfect, as the syntax is still fairly strict, but it has worked in my experience.

#### Currently available commands:


##### General commands

`hello` - returns hello message back to sender.

> <@bbbot> hello

`thanks` - returns "you're welcome" message back to sender.

> <@bbbot> thanks

`roll` - "rolls" a N-sided die (N is an integer).

> <@bbbot> roll ... {N=20}


###### Key:
 ... - denotes extra text in the message that will not break the bot, but are ignored.

 {X=y} - denotes an optional argument. If not provided, will default to value y.



##### List commands

These are all related commands that deal with "list" functionality (i.e., the same as keeping lists on a notepad)


`add` - Adds items to the provided list. If no list exists, it will create a new one.

> <@bbbot> add [\_], and [\_] to ... (_) list

`remove` Removes items from the provided list. 'ALL' can be provided as the only argument to clear the list.

> <@bbbot> remove [\_], and [\_] from ... (_) list

`read` - Reads all of the items in the provided list. 

> <@bbbot> read .. (_) list

`show` - Shows all of the items in the provided directory. It was intended to be used to show lists, but can be used for any directory in the repository. 

> <@bbbot> show {folder=lists}

`delete` - Deletes the provided list, but only if it is already empty (safety first).

> <@bbbot> delete ... (_) list

###### Key: 
[_] - represents list items (e.g., eggs)

(_) - represents the name of the list (e.g., 'shopping' for a shopping list)

... - denotes extra text in the message that will not break the bot, but are ignored.

{X=y} - denotes an optional argument. If not provided, will default to value y.


***

### Project Directories
- requirements.txt is a list of Python modules used in the project.
- The main script is BBbot.py, which initializes the bot and connects it to the Slack server.
- The Slack bot token is in the main directory and kept as a .c file to keep it out of version control.
- Commands are in the `commands` sub-folder.
- Lists (which are manipulated by the 'list_xyz.py' commands) are in the `lists` sub-folder.
- The remaining sub-folders are a part of the virtual environment.
