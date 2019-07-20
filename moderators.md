## Moderator doc

THANKS for volunteering to manage [our Blog Code Challenge Pull Requests]([open PR counter](https://github.com/pybites/challenges/pulls)). 

Here is a quick HOWTO:

1. Ping _pybob_ or _clamytoe_ [on our Slack](https://join.slack.com/t/pybites/shared_invite/enQtNDAxODc0MjEyODM2LTNiZjljNTI2NGJiNWI0MTRkNjY4YzQ1ZWU4MmQzNWQyN2Q4ZTQzMTk0NzkyZTRmMThlNmQzYTk5Y2Y5ZDM4NDU) to be added as collaborator to this repo.

2. While on Slack please join our #pull-requests channel: new PRs get posted there and we use it to discuss issues and/or clarify doubts.

3. When you merge a PR there are a few things to verify:

  - does the user have the _community_ branch as destination? We want to keep _master_ pristine, so make sure we're merging into _community_. As a moderator you can change it on the PR.

  - we only accept ONE PR FOR ONE CHALLENGE, so if the user opens a PR for multiple challenges (easy to spot by looking at the numbered directories), they did not follow our platform's procedure so kindly [point them to it](https://codechalleng.es/challenges/).

  - user should not overwrite any template files or pre-delivered tests. If this cannot be fixed on the branch, just deny/close the PR without merging.

  - user should have committed the files in a "PCC number / username" directory to keep their code in the right place and isolated from other submissions, e.g. 62/bbelderbos if I would PR my submission for PCC62 *1

  - user commits big text files (e.g. PCC01 dictionary.txt - might be our bad not telling them), just delete this file from the submission if possible.

  - ideally (but optionally) review the code providing some feedback what is awesome and what could be coded better, people love it and we assume this is the exciting part for you guys ("to be a mentor" is one of the most satisfying things, no?). Look at previous PRs to see examples. If we have a high load, merging trumps review ;)

  - merge the PR into the community branch (if you wonder why not _solutions_, that's legacy, for blog challenges we want community contributions, not one 'right' answer, hence we created a better named branch). Another notification will be posted to the Slack channel and the [open PR counter](https://github.com/pybites/challenges/pulls) will go down, you're awesome! There is also a platform job that syncs PRs back from GH to platform so they show up as _completed_ there. 

*1 we often refer to our Blog Code Challenge as PCC<number>, PCC stands for PyBites Code Challenge (not to confuse with our Bites of Py Exercises)
