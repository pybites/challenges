import argparse

from github import Github

parse = argparse.ArgumentParser()
parse.add_argument('user', help="GitHub username")
parse.add_argument('password', help="GiHub password")
args = parse.parse_args()

gh = Github(login_or_token=args.user, password=args.password)
user = gh.get_user()
repos = user.get_repos()
for repo in repos:
    print(f'{repo.name}')
