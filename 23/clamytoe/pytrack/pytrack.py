#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from maya import get_localzone, MayaInterval, now, parse

from pytrack.models import Log, Project

STATE = ('INACTIVE', 'ACTIVE')


def get_projects(display=False):
    projects = []
    in_db = Project.select()
    if in_db:
        for project in Project.select():
            projects.append(project)
            if display:
                if project.selected:
                    print(f'*[{project.id}] {project.duration} {STATE[project.status]}: {project.name}')
                else:
                    print(f' [{project.id}] {project.duration} {STATE[project.status]}: {project.name}')
    else:
        print('You are not currently tracking any projects.')
    return projects


def get_selected(display=True):
    """Returns the currently selected project"""
    selected = None
    projects = get_projects()
    for project in projects:
        if project.selected:
            selected = project
    if display:
        if selected:
            print(f'Selected: {selected.name}')
        else:
            print(f'Selected: {selected}')

    return selected


def get_active():
    """Returns the currently active project"""
    active = None
    projects = get_projects()
    for project in projects:
        if project.status == 1:
            active = project
    return active


def update_project(project):
    """Updates the duration of the project's time"""
    duration = None

    # set local timezone
    timezone = get_localzone()
    local_tz = timezone.zone

    # collect all of the logs that are part of this project
    logs = Log.select().where(Log.project_id == project.id)

    # iterate over the logs and accumulate the duration of each log
    for n, log in enumerate(logs):
        start = parse(log.start_time).datetime(to_timezone=local_tz, naive=True)
        stop = parse(log.stop_time).datetime(to_timezone=local_tz, naive=True)

        if n == 0:
            duration = MayaInterval.from_datetime(start, stop).timedelta
        else:
            duration += MayaInterval.from_datetime(start, stop).timedelta

    # update the project
    project.duration = duration
    project.status = 0
    project.save()
    print(f'Deactivating: {project.name} with total time of {project.duration}')


def add_project(name):
    """Add a new project"""
    # ensure that there are no active projects
    active = get_active()

    if active:
        print(f'There is an active project: [{active.id}] {active.name}')
        print('Please close that out before adding another project.')
    else:
        project = Project.create(name=name)
        project.save()
        print(f'Added Project: [{project.id}] {project.name}')
        select_project(project.id)


def select_project(id):
    """Marks the given project ID as selected"""
    # ensure that there are no active projects
    active = get_active()

    if active:
        print(f'Cannot make project selection while there is an active project!')
        print(f'Currently tracking: {active.name}')
    else:
        projects = get_projects()

        # iterate over projects to see if id is a valid entry
        valid = False
        for project in projects:
            if project.id == id:
                valid = True

        if valid:
            for project in projects:
                if project.id == id:
                    project.selected = True
                    project.save()
                    print(f'Selected: [{project.id}] {project.name}')
                else:
                    # unselect all others
                    project.selected = False
                    project.save()
        else:
            print(f'[{id}] is not a valid entry. \nChoose from the following:\n')
            _ = get_projects(display=True)


def remove_project(id):
    """Remove the project by the entered ID"""
    project = False
    selected = 0
    select = None
    projects = get_projects()

    for proj in projects:
        if proj.id == id:
            project = proj
            selected = proj.selected
        else:
            select = proj.id

    if project:
        print(f'About to remove [{project.id}] {project.name}')
        answer = input('Are you sure (y/n): ')
        if 'y' in answer.lower():
            project.delete_instance()
            print(f'Removed [{project.id}] {project.name}')
            if selected and select:
                select_project(select)
        else:
            print('Aborted')
    else:
        print(f'Project [{id}] does not exists!')


def reset_db():
    """Reset the database"""
    print('WARNING: You are about to delete all records!')
    answer = input('Are you sure (y/n/): ')
    if 'y' in answer.lower():
        p = Project.delete()
        p.execute()
        l = Log.delete()
        l.execute()
        print('All records have been removed.')
    else:
        print('Aborted')


def start_tracking():
    """Starts active tracking of project"""
    # ensure that there are no current active projects
    active = get_active()

    if active:
        print(f'Already tracking {active.name}!')
    else:
        project = get_selected(display=False)
        log = Log.create(project=project, start_time=now().datetime())
        log.save()
        project.status = 1
        project.save()
        print(f'Activating: {project.name}')


def stop_tracking():
    """Stops active tracking of project"""
    # ensure that we are closing an active project
    active = get_active()

    if active:
        logs = Log.select().where(Log.project_id == active.id)

        # close out the log that doesn't have a stop_time entry
        for log in logs:
            if not log.stop_time:
                log.stop_time = now().datetime()
                log.save()
                # update the project's status and duration time
                update_project(active)
    else:
        print(f'There are currently no active projects...')
