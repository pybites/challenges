First time only setup:
```bash
$ git clone https://github.com/mhered/challenges -b community && cd challenges
$ git remote add upstream https://github.com/pybites/challenges
```
Init for every new challenge:
```bash
$ git checkout community # return to community branch
$ git pull upstream community # pull the latest upstream repo
$ git checkout -b PCC45 # create a branch to work on the challenge
$ mkdir 45/mhered && cd $_ # work on your own subdirectory
```
Commit and push code:
```bash 
$ git add . && git commit -m 'PCC45 mhered' # commit 
$ git push origin PCC45 # push to your fork
```