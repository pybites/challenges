import os
from github import Github, Repository, PullRequest
from bottle import run, template, get, post, request
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest


@get('/hacktoberfest')
def form():
    return '''<h2>Check Hacktoberfest PR Count</h2>
              <form method="POST" action="/login">
                Username: <input name="username" type="text" /><br/>
                Password: <input name="password" type="text" />
                <input type="submit" />
              </form>'''


@post('/login')
def submit():
    pr_count = 0
    # grab data from form
    username = request.forms.get('username')
    password = request.forms.get('password')

    github = Github(username, password)
    if github:
        repos = github.get_repos()
        repo: Repository.Repository
        for repo in repos:
            prs = repo.get_pulls()
            pr_count = len(list(prs))

        return template('''
            <h1>Congrats!</h1>
            <div>
                You have: {{pr_count}} Pull Requests!
            </div>
            ''', pr_count)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
