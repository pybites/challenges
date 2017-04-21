# Clamytoe's Task Manager App

## Index
* [Introduction](#intro)
* [UI](#ui)
  * [New Project](#newProj)
  * [New Task](#newTask)
  * [Task Status](#status)
  * [Controls](#controls)
  * [Project Tabs](#tabs)
  * [Remove Project](#rProj)
  * [Remove All Tasks](#rTasks)
  * [Status Toggle](#toggle)
  * [Remove Task](#rTask)
* [Installation](#install)

<a name="intro"></a>
## Introduction
This a my submission to the PyBites Coding Challenge. 
It's a no frills task manager that's really intuitive and 
simple application to use.

<a name="ui"></a>
#### UI

<a name="newProj"></a>
##### New Project
![New Project](img/project.png)

Enter the project name that you want to store your tasks
under.

<a name="newTask"></a>
##### New Task
![New Task](img/task.png)

Describe the task that you need to accomplish.

<a name="status"></a>
##### Task Status
![Task Status](img/status.png)

The task can be entered as open or close.

<a name="controls"></a>
##### Controls
![Controls](img/controls.png)

Clicking on the **Add** button will add the new task and create
a new project if it does not already exist.

Clicking on the **Reset** button will reset the fields.

<a name="tabs"></a>
##### Project tabs
![Project Tabs](img/tabs.png)

Any projects that are created will be displayed here in the
tab area. Clickin on the tab switches you to that project.

<a name="rProj"></a>
##### Remove Project
![Remove Project](img/remove_project.png)

Clicking on this will remove the currently active project
along with all of it's corresponding tasks.

<a name="rTasks"></a>
##### Remove all tasks
![Remove Tasks](img/remove_all_tasks.png)

Clicking this will remove all tasks from the active project,
but leave the project active.

<a name="toggle"></a>
##### Status toggle
![Status Toggle](img/status_toggle.png)

Clicking this will toggle the tasks from open to close.

<a name="rTask"></a>
##### Remove task
![Remove Task](img/remove_task.png)

Clicking this will remove that tasks from the project.

<a name="install"></a>
## Installation
First of all you have to prepare your environment. Select
a location where you want to store the files. I will use 
Projects as my example. I'm also on a linux machine, but
you should be able to figure it out for any other platform.

    mkdir Projects
    cd Projects

Then follow along with the [INSTALL](https://github.com/pybites/challenges/blob/master/INSTALL.md)
instructions provided by [PyBites](http://pybit.es/) to
clone the challenges. Once cloned you can do the following:

    cd challenges/15/clamytoe
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app-clamytoe.py

Then simply open up a browser, Chrome/Chromium recommended,
to [localhost:5000](http://localhost:5000/) and play around
with it :).

