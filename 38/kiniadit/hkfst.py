from bottle import route, run, get, post, request, template
import github
from github import Github

@get('/')
def login():
    return '''
        <h1> Hacktoberfest Checker! </h1>
        <p>Welcome! Please type in you Github username below to know your progress for Hacktober!</p>
        <form action="/" method="post">
            Github Username: <input name="username" type="text" />
        </form>'''

@post('/')
def find_prs():
    username = request.forms.get('username')
    gh = Github()
    try:
        name=gh.get_user(username).name
    except github.GithubException:
        return template('not_found')
    statements = ['It\'s not too late to start!', 'Off to a great start, keep going!',
     'Half way there, keep it up!','So close!','Way to go!','Now you\'re just showing off!']
    try:
        prs = gh.search_issues('', author=username, type='pr', created='2017-09-30T00:00:00-12:00..2017-10-31T23:59:59-12:00')
    except github.GithubException:
        pass
    pr_data={"urls":[],"titles":[],"dates_of_creation":[]}
    if any(True for _ in prs):
        for pr in prs:
            pr_data["urls"].append(pr.pull_request.html_url)
            pr_data["titles"].append(pr.title)
            pr_data["dates_of_creation"].append(pr.created_at)
        return template('pr_template',pr_data=pr_data,name=prs[0].user.name,prs=pr_data["titles"],
            dates=pr_data["dates_of_creation"],urls=pr_data["urls"],pr_count=len(pr_data["titles"]),statement=statements[len(pr_data["titles"])])
    else:
        return template('pr_template',pr_count=0,name=name,statement=statements[0])
run(host='localhost', port=8080)