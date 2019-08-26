import os
from github import Github, Repository, PullRequest, NamedUser
from bottle import run, template, get, post, request
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest
from github.Repository import Repository


@get('/hacktoberfest')
def form():
    return '''<h2>Check Hacktoberfest PR Count</h2>
              <form method="POST" action="/login">
                API Token: <input name="token" type="text" /><br/>
                <input type="submit" />
              </form>'''


@post('/login')
def submit():
    pr_count = 0
    # grab data from form
    token = request.forms.get('token')

    github = Github(token)
    if github:
        user: NamedUser.NamedUser = github.get_user()
        repos = user.get_repos()

        repo: Repository.Repository
        for repo in repos:
            print(repo.description)
            prs = repo.get_pulls()
            pr_count += len(list(prs))

        pr_count_str = str(pr_count)
        hacktoberflag: bool = (pr_count > 4)

        if hacktoberflag:
            say = "won"
        else:
            say = "lost"

        return template('''
            <h1>Congrats!</h1>
            <div>
                You have: {{pr_count}} Pull Requests!
            </div>
            <div>
                You have {{say}} Hacktoberfest this month!
            </div>
            ''', pr_count=pr_count_str,  say=say)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
