# using https://github.com/PyGithub/PyGithub
from collections import defaultdict
import os
from pprint import pprint as pp
import re
import sys

from github import Github

GH_USER = os.environ.get('GH_USER')
GH_PW = os.environ.get('GH_PW')
if not GH_USER or not GH_PW:
    print('Please set GH_USER and GH_PW env vars')
    sys.exit(1)

CHALLENGES_REPO = 'challenges'
ATTENTION = 'ATTENTION: before clicking "Create Pull Request"'
TEMPLATE_LINE = 'Difficulty level (1-10)'
START_PR = 46  # here we implemented the template


def get_challenge_repo():
    gh = Github(GH_USER, GH_PW)
    user = gh.get_user()
    return user.get_repo(CHALLENGES_REPO)


def _parse_template_response(resp):
    if TEMPLATE_LINE not in resp:
        raise ValueError('No "{}" in response'.format(TEMPLATE_LINE))

    booleans = dict(y=True, n=False)
    ret = {}

    for line in resp.split('\n'):
        if not line.strip() or ATTENTION in line or ':' not in line:
            continue

        key, value = line.split(':', 1)

        key = re.sub(r'(.*)\s?[:(].*', r'\1', key.lower())
        key = '_'.join(key.split()[:2])

        value = re.sub(r'.*?\[(.*?)\].*', r'\1', value.lower()).strip()
        if value[0] in 'y n'.split():
            value = booleans.get(value[0])

        ret[key] = value

    return ret


def _get_challenge_number(pr):
    files = [file_.filename for file_ in pr.get_files()
             if re.match(r'^\d+/.*', file_.filename)]
    try:
        return files[0].split('/')[0]
    except:
        raise AttributeError('Cannot get challenge number')


def get_submissions(challenge_repo):
    submissions = defaultdict(dict)

    for pr in challenge_repo.get_pulls('all'):

        pr_number = int(pr.number)
        user = pr.user.login

        if pr_number < START_PR:
            print('{} did not implement template yet'.format(pr_number))
            continue

        try:
            challenge_number = _get_challenge_number(pr)
        except AttributeError as exc:
            print(exc)
            continue

        try:
            response = _parse_template_response(pr.body)
        except ValueError as exc:
            print(exc)
            continue

        # make sure each challenge is only recorded once per user
        submissions[challenge_number][user] = response

        return submissions


if __name__ == '__main__':
    challenge_repo = get_challenge_repo()
    submissions = get_submissions(challenge_repo)
    pp(submissions)
