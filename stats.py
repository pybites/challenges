'''Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs'''
from collections import Counter
import glob
import os

TOP_N = 5
NOT_USERS = 'static templates data'.split()

users = Counter()
popular_challenges = Counter()

for dir_ in glob.glob('*/*'):
    dir_ = dir_.lower()
    if not os.path.isdir(dir_):
        continue
    ch, user = dir_.split('/')
    ch = 'PCC' + ch
    if user in NOT_USERS:
        continue
    users[user] += 1
    popular_challenges[ch] += 1


print('{} users opened {} PRs\n'.format(len(users),
                                        sum(popular_challenges.values())))

print('Top 5 challenges by PR:')
print(popular_challenges.most_common(TOP_N))

print('Die hard users:')
print(users.most_common(TOP_N))

print('\n* new style PRs only = ch<int>/user<str> directory names')
