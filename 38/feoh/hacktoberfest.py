import os
import datetime
from github import Github, Repository, PullRequest, NamedUser, BadCredentialsException
from bottle import run, template, get, post, request


def render_login_form(pr_count):
    pr_count_str = str(pr_count)
    hacktoberflag = (pr_count > 4)

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
        ''', pr_count=pr_count_str, say=say)


@get('/hacktoberfest')
def form():
    return '''<h2>Check Hacktoberfest PR Count</h2>
              <form method="POST" action="/login">
                API Token: <input name="token" type="text" /><br/>
                <input type="submit" />
              </form>'''


@post('/login')
def submit():
    try:
        pr_count = 0
        # grab data from form
        token = request.forms.get('token')
        github = Github(token)
        user = github.get_user()
        repos = user.get_repos()

        for repo in repos:
            prs = repo.get_pulls()
            today = datetime.datetime.now()
            one_month = datetime.timedelta(days=30)
            month_ago = today - one_month
            for pr in prs:
                if pr.created_at > month_ago:
                    pr_count += 1

        return(render_login_form(pr_count))
    except BadCredentialsException:
        return("""<h1>Token Invalid, please try again!</h1>""")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
