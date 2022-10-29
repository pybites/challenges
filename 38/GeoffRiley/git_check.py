from datetime import date

from bottle import run, template, request, post, get
from github import Github, GithubException


@get('/')
def login():
    return '''
    <h1>HacktoberFest Checker</h1>
    <h2>Login</h2>
    <p>Please enter your Github username</p>
    <form action="/" method="post">
    Github username: <input name="username" type="text" />
    </form>
    '''


@post('/')
def search_prs():
    # Statements taken from https://github.com/pybites/hacktoberfest-checker/blob/master/controllers/index.js
    statements = [
        "It's not too late to start!",
        "Off to a great start, keep going!",
        "Half way there, keep it up!",
        "So close!",
        "Way to go!",
        "Now you're just showing off!"
    ]
    # Extract the username entered in the web form
    username = request.forms.get('username')

    # check with GitHub that the entered username actually exists… if not show the unknown template
    gh = Github()
    try:
        user = gh.get_user(username).name
    except GithubException:
        return template('unknown')

    # Now we're going to grab a list of all the PRs put through by the user… there should be more checking though, ie:
    # for invalid and spam labels at the very least.
    try:
        # Query based upon:
        # const options = {
        #  q: `-label:invalid
        #       +created:2017-09-30T00:00:00-12:00..2017-10-31T23:59:59-12:00
        #       +type:pr
        #       +is:public
        #       +author:${username}`
        # };
        # from https://github.com/pybites/hacktoberfest-checker/blob/master/controllers/index.js
        # The was written for 2017, so it needs to be updated for *this* year,
        # we can automagically pick the current year:
        year = str(date.today().year)
        # Request a list of PRs within the specific date range…
        query = f'{year}-09-30T00:00:00-12:00..{year}-10-31T23:59:59-12:00'
        pr_list = gh.search_issues('', author=username, type='pr', created=query)
    except GithubException:
        # any errors from GitHub at this stage we just assumes means no PRs found
        pr_list = []
        pr_list.totalCount = 0

    # We're going to pick out the details for each PR that we want to display to the user
    pr_detail = {"url": [], "title": [], "date": []}
    # Provided there are PRs, loop through them extracting the url, title and date into the pr_detail arrays
    if pr_list.totalCount > 0:
        for pr in pr_list:
            pr_detail["url"].append(pr.pull_request.html_url)
            pr_detail["title"].append(pr.title)
            pr_detail["date"].append(pr.created_at)

        pr_count = len(pr_detail["title"])
        return template('pr_list', pr_data=pr_detail, name=pr_list[0].user.name,
                        prs=pr_detail["title"], dates=pr_detail["date"], urls=pr_detail["url"],
                        pr_count=pr_count, statement=statements[pr_count])

    return template('pr_list', pr_count=0, name=user, statement=statements[0])


run(host='localhost', port=8080)
