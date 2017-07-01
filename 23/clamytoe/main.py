#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv

import click
from peewee import OperationalError

from pytrack import db, Log, Project
from pytrack import get_projects, add_project, select_project, remove_project
from pytrack import start_tracking, stop_tracking, reset_db


def main():
    """Displays all projects

    If command line arguments are used, they are passed on to click to process,
    if not, then all of the projects currently being worked on are displayed.
    """
    try:
        db.connect()
    except OperationalError:
        pass

    try:
        db.create_tables([Log, Project], True)
    except OperationalError:
        pass
    else:
        if len(argv) > 1:
            cli()
        else:
            _ = get_projects(display=True)
    finally:
        db.close()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name', type=click.STRING)
def add(name):
    """Add a new project"""
    add_project(name)


@cli.command()
@click.argument('project_id', type=click.INT)
def select(project_id):
    """Marks the given project ID as selected"""
    select_project(project_id)


@cli.command()
@click.argument('project_id', type=click.INT)
def remove(project_id):
    """Remove the project by the entered ID"""
    remove_project(project_id)


@cli.command()
def reset():
    """Reset the database"""
    reset_db()


@cli.command()
def start():
    """Starts active tracking of project"""
    start_tracking()


@cli.command()
def stop():
    """Stops active tracking of project"""
    stop_tracking()


if __name__ == '__main__':
    main()
