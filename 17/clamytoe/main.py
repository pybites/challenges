#!/usr/bin/env python3
from random import choice
from sys import exit

import click
from podcaster import Podcast

FEEDS = ['https://pythonbytes.fm/episodes/rss',
         'https://talkpython.fm/episodes/rss',
         'https://audioboom.com/channels/4567086.rss',
         ]
MANAGER = Podcast(None)
PODS = MANAGER.get_all_podcasts()


@click.group()
def main():
    """Displays the episodes that are in the podcast"""
    pass


@main.command()
@click.option('--pod1', is_flag=True, default=False, 
              help='Preload with first entry')
@click.option('--pod2', is_flag=True, default=False, 
              help='Preload with second entry')
@click.option('--pod3', is_flag=True, default=False, 
              help='Preload with third entry')
@click.option('--all', is_flag=True, default=False, 
              help='Preload with all entries')
def preload(all, pod1, pod2, pod3):
    """Preload the database with defaults"""
    if pod1:
        click.echo(f'Adding {FEEDS[0]}')
        pod = Podcast(FEEDS[0])
    elif pod2:
        click.echo(f'Adding {FEEDS[1]}')
        pod = Podcast(FEEDS[1])
    elif pod3:
        click.echo(f'Adding {FEEDS[2]}')
        pod = Podcast(FEEDS[2])
    elif all:
        click.echo(f'Adding them all, please be patient!')
        for feed in FEEDS:
            pod = Podcast(feed)
    else:
        click.echo('You must enter one of the following choices:')
        click.secho(f'  --pod1', fg='green', bold=True, nl=False)
        click.echo(f' for {FEEDS[0]}')
        click.secho(f'  --pod2', fg='green', bold=True, nl=False)
        click.echo(f' for {FEEDS[1]}')
        click.secho(f'  --pod3', fg='green', bold=True, nl=False)
        click.echo(f' for {FEEDS[2]}')
        click.secho(f'  --all', fg='green', bold=True, nl=False)
        click.echo(' for all of them!')


@main.command()
@click.argument('url')
def feed(url):
    """Downloads feed into the database"""
    pod = Podcast(url)


@main.command()
@click.option('--eid', '-e', default=0, help='ID of the episode to display')
@click.option('--download', '-d', is_flag=True, default=False, 
              help='Download the episode')
@click.argument('podcast_id', type=click.INT)
def episodes(podcast_id, eid, download):
    """Displays the episodes that are in the podcast"""
    click.clear()

    if check_pid(podcast_id):
        for pod in PODS:
            if pod.id == podcast_id:
                selected = Podcast(pod.rss)
                if eid:
                    if check_eid(podcast_id, eid):
                        for show in selected.episodes:
                            if show.id == eid:
                                if download:
                                    selected.download_episode(show)
                                    selected.mark_episode_done(show)
                                    exit(0)
                                else:
                                    click.secho(f'Episode ID: {show.id} ', 
                                                fg='yellow', bg='blue', 
                                                bold=True, nl=False)
                                    click.secho('\t\t\t', nl=False)
                                    click.secho(f' Duration: [{show.duration}] ', 
                                                fg='magenta', bold=True, 
                                                nl=False)
                                    click.secho(f'\t\t Played: {show.done} ', 
                                                fg='green')
                                    click.secho(f'{show.title}', fg='green', 
                                                bold=True)
                                    click.echo('')
                                    click.secho(show.summary, fg='white', 
                                                bg='black')
                                    click.secho(show.file)
                                    click.echo('')
                    else:
                        click.secho(f'{eid} is not a valid Episode ID!'.upper(), 
                                    fg='red', bold=True)
                else:
                    selected.list_episodes()


@main.command()
@click.option('--pid', '-p', type=click.INT, help='ID of the pod to display')
def podcasts(pid):
    """Displays information about the podcasts"""
    click.clear()

    if PODS:
        if pid:
            if check_pid(pid):
                for pod in PODS:
                    if pod.id == pid:
                        selected = Podcast(pod.rss)
                        click.secho(f' Podcast ID: {selected.id} ', 
                                    fg='yellow', bg='blue', bold=True, 
                                    nl=False)
                        click.secho('\t\t\t', nl=False)
                        click.secho(f' Episodes: [{selected.total_episodes}] ', 
                                    fg='magenta', bold=True, nl=False)
                        click.secho('\t\t Progress: ', nl=False)
                        click.secho(f'{selected.status} ', fg='green')
                        click.secho(f'{selected.title}', fg='green', bold=True)
                        click.secho(f'Updated on: {selected.published}')
                        click.secho(f'{selected.author} (', fg='white', 
                                    bg='black', nl=False)
                        click.secho(f'{selected.email}', fg='white', 
                                    bg='black', bold=True, nl=False)
                        click.secho(') ', fg='white', bg='black')
                        click.echo('')
                        click.secho(selected.summary, fg='white', bg='black')
                        click.secho(selected.link)
                        click.echo('')
            else:
                click.secho(f'{pid} is not a valid Podcast ID!'.upper(), 
                            fg='red', bold=True)
        else:
            for pod in PODS:
                p = Podcast(pod.rss)
                click.secho(f' Podcast ID: {p.id} ', fg='yellow', bg='blue', 
                            bold=True, nl=False)
                click.secho(f'\t\tUpdated on: {p.published}', bold=True, 
                            nl=False)
                click.secho('\t\t', nl=False)
                click.secho(f' Episodes: [{p.total_episodes}] ', fg='magenta', 
                            bold=True)
                click.secho(f'{p.title}', fg='green', bold=True)
                click.secho(p.subtitle, fg='white', bg='black')
                click.echo('\n')
    else:
        empty_message()


@main.command()
def random():
    """Randomly selects and downloads an episode"""
    click.clear()
    if PODS:
        pod = choice(PODS)
        podcast = Podcast(pod.rss)
        if not podcast.complete:
            episode = podcast.get_random_episode()
            podcast.download_episode(episode)
            podcast.mark_episode_done(episode)
            exit(0)
    else:
        empty_message()


def check_eid(pid, eid):
    """Check to see if the show id is valid"""
    episode_ids = []
    for pod in PODS:
        if pod.id == pid:
            selected = Podcast(pod.rss)
            episodes = selected.episodes
            for episode in episodes:
                episode_ids.append(episode.id)
    return True if eid in episode_ids else False


def check_pid(pid):
    """Checks to see if the podcast id that was requested is valid"""
    pod_ids = []
    for pod in PODS:
        pod_ids.append(pod.id)
    return True if pid in pod_ids else False


def empty_message():
    click.secho('There are no podcasts in the database!'.upper(), fg='red', 
                bold=True)
    click.secho('Check the help message for further details: ', nl=False)
    click.secho(' --help ', fg='cyan', bold=True)
    exit(0)


if __name__ == '__main__':
    main()
else:
    print('Please do not import this file, run it directly!')
