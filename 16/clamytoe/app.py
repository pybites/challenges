import requests
import webbrowser
from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from time import localtime, strftime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gh-profiles.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
API_BASE = 'https://api.github.com/users/'
DEBUG = False


class Accounts(db.Model):
    """Accounts schema"""
    login = db.Column(db.String(20), primary_key=True)
    avatar_url = db.Column(db.String(80))
    url = db.Column(db.String(50))
    html_url = db.Column(db.String(50))
    followers_url = db.Column(db.String(80), default=None)
    following_url = db.Column(db.String(80), default=None)
    gists_url = db.Column(db.String(80), default=None)
    starred_url = db.Column(db.String(80), default=None)
    subscriptions_url = db.Column(db.String(80), default=None)
    organizations_url = db.Column(db.String(80), default=None)
    repos_url = db.Column(db.String(80), default=None)
    events_url = db.Column(db.String(80), default=None)
    received_events_url = db.Column(db.String(80), default=None)
    name = db.Column(db.String(40))
    company = db.Column(db.String(40), default=None)
    blog = db.Column(db.String(50), default=None)
    location = db.Column(db.String(40), default=None)
    email = db.Column(db.String(40), default=None)
    hireable = db.Column(db.Boolean, default=False)
    bio = db.Column(db.Text, default=None)
    public_repos = db.Column(db.Integer, default=0)
    public_gists = db.Column(db.Integer, default=0)
    followers = db.Column(db.Integer, default=0)
    following = db.Column(db.Integer, default=0)
    created_at = db.Column(db.String(20))
    updated_at = db.Column(db.String(20))
    etag = db.Column(db.String(32))

    def __init__(self, login, avatar_url, url, html_url, followers_url, 
                 following_url, gists_url, starred_url, subscriptions_url, 
                 organizations_url, repos_url, events_url, received_events_url, 
                 name, company, blog, location, email, hireable, bio, 
                 public_repos, public_gists, followers, following, created_at,
                 updated_at, etag):
        self.login = login
        self.avatar_url = avatar_url
        self.url = url
        self.html_url = html_url
        self.followers_ur = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.name = name
        self.company = company
        self.blog = blog
        self.location = location
        self.email = email
        self.hireable = hireable
        self.bio = bio
        self.public_repos = public_repos
        self.public_gists = public_gists
        self.followers = followers
        self.following = following
        self.created_at = created_at
        self.updated_at = updated_at
        self.etag = etag

    def __repr__(self):
        return f'<GHAccount {self.name} ({self.login})>'


class Repos(db.Model):
    """Repos schema"""
    repos_id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(20), db.ForeignKey('accounts.login'))
    name = db.Column(db.String(40))
    html_url = db.Column(db.String(50))
    description = db.Column(db.Text, default=None)
    fork = db.Column(db.Boolean, default=False)
    language = db.Column(db.String(20))
    created_at = db.Column(db.String(20))
    pushed_at = db.Column(db.String(20))
    etag = db.Column(db.String(32))

    def __init__(self, repos_id, owner, name, html_url, description, fork, 
                 language, created_at, pushed_at, etag):
        self.repos_id = repos_id
        self.owner = owner
        self.name = name
        self.html_url = html_url
        self.description = description
        self.fork = fork
        self.language = language
        self.created_at = created_at
        self.pushed_at = pushed_at
        self.etag = etag

    def __repr__(self):
        return f'<Repo {self.owner}: {self.name}>'


class Gists(db.Model):
    """Gists schema"""
    gist_id = db.Column(db.String(32), primary_key=True)
    owner = db.Column(db.String(20), db.ForeignKey('accounts.login'))
    filename = db.Column(db.String(40))
    html_url = db.Column(db.String(50))
    description = db.Column(db.Text, default=None)
    etag = db.Column(db.String(32))

    def __init__(self, gist_id, owner, filename, html_url, description, etag):
        self.gist_id = gist_id
        self.owner = owner
        self.filename = filename
        self.html_url = html_url
        self.description = description
        self.etag = etag

    def __repr__(self):
        return f'<Gist {self.owner}: {self.filename}>'


# initialize the database
db.create_all()


@app.route('/')
def index():
    """Home page of the app
    
    It loads the index template page.
    """
    return render_template('index.html')


@app.route('/user', methods=['POST'])
def get_account():
    """Access account
    
    Attempts to retrieve account info from the database. If the account is 
    found, it checks to see if the online version has changed. If it has, the 
    info in the database is removed and the new data is pulled from GitHub. If 
    the account does not exist at all in the database, it gets it from GitHub.
    """
    username = request.form['username']
    user = username.lower()
    gh_user = None
    gh_repos = []
    gh_gists = []
    is_account = False
    is_repos = False
    is_gists = False

    if not user:
        return redirect('/')

    # check existing accounts to see if its in there
    accounts = Accounts.query.all()
    for account in accounts:
        if account.login == user:
            if DEBUG: print(f"User already exists: {account.login}")
            if DEBUG: print("Checking for updates to info")
            same = check_etag(user, account.etag)
            if same:
                gh_user = account
                if DEBUG: print(f"Getting info from db: {gh_user.login}")
                is_account = True
            else:
                if DEBUG: print(f'Account etags differ, getting an update')
                Accounts.query.filter(Accounts.login == user).delete()
                db.session.commit()
                break

    # add the account if not in database already
    if not is_account:
        url = API_BASE + user
        if DEBUG: print(f"Checking: {url}")
        # Header info
        response = requests.head(url)
        status = response.headers['Status']
        if DEBUG: print(f'Status: {status}')

        # Handle errors
        if '404' in status:  # 404 Not Found
            err_message = "User not found! Try a different dude!"
            return render_template('index.html', error=err_message)
        elif '403' in status:  # 403 Forbidden
            remaining = int(response.headers['X-RateLimit-Reset'])
            reset_at = strftime("%H:%M:%S", localtime(remaining))
            err_message = "You have exceeded the number of lookups! "\
                          f"Come back after {reset_at}!"
            return render_template('index.html', error=err_message)
        else:
            gh_user = add_profile(user)
            if DEBUG: print(f"Retrived {gh_user}")
            if DEBUG: print(f"Name is {gh_user.name}")
            is_account = True

    if is_account:
        # Check and see if we have a repos for the user
        repos = Repos.query.all()

        for repo in repos:
            if repo.owner == user:
                if not is_repos:
                    # Check to see if the repos in the db are still up to date
                    is_repos = check_etag(user + '/repos', repo.etag)
                    if not is_repos:
                        if DEBUG: print("Repos etags differ, getting an update")
                        Repos.query.filter(Repos.owner == user).delete()
                        db.session.commit()
                        break
                else:
                    gh_repos.append(repo)
                    if DEBUG: print(f"Found existing repo: {repo}")
                    is_repos = True

        # Check and see if we have any gists for the user
        gists = Gists.query.all()

        for gist in gists:
            if gist.owner == user:
                if not is_gists:
                    # Check to see if they are up to date
                    is_gists = check_etag(user + '/gists', gist.etag)
                    if not is_gists:
                        if DEBUG: print(f'Gist etags differ, getting an update')
                        Gists.query.filter(Gists.owner == user).delete()
                        db.session.commit()
                        break
                else:
                    gh_gists.append(gist)
                    if DEBUG: print(f"Found existing gist: {gist}")
                    is_gists = True

    if not is_repos:
        if DEBUG: print("Repos were not found or needs to be updated")
        gh_repos = add_repos(user)
        if DEBUG: print(f"Repos: {gh_repos}")

    if not is_gists:
        if DEBUG: print("Gists were not found or needs to be updated")
        gh_gists = add_gists(user)
        if DEBUG: print(f"Gists: {gh_gists}")

    return render_template('index.html', gh_user=gh_user, gh_repos=gh_repos, 
                           gh_gists=gh_gists)


def check_etag(user, old_etag):
    """Compares the etag from the db to the ones from GitHub"""
    url = API_BASE + user
    response = requests.head(url)
    new_etag = response.headers['ETag']
    matched = True if old_etag == new_etag else False
    if DEBUG: print(f'ETags Match: {matched}')

    return matched


def add_profile(user):
    """Adds account information"""
    url = API_BASE + user
    if DEBUG: print(f"Retrieving: {url}")

    # Header info
    response = requests.get(url)
    status = response.headers['Status']
    limit = response.headers['X-RateLimit-Limit']
    remaining = response.headers['X-RateLimit-Remaining']
    reset = response.headers['X-RateLimit-Reset']
    etag = response.headers['ETag']
    if DEBUG: print(f'Status: {status}')
    if DEBUG: print(f'Limit: {limit}')
    if DEBUG: print(f'Remaining: {remaining}')
    if DEBUG: print(f'Reset: {reset}')
    if DEBUG: print(f'ETag: {etag}')
    if DEBUG: print(f"Retrieved: {url}")

    data = response.json()
    if DEBUG: print(f"Found {data['name']}")

    # add the account
    add_account = Accounts(data['login'].lower(), data['avatar_url'], 
                           data['url'], data['html_url'], data['followers_url'], 
                           data['following_url'], data['gists_url'], 
                           data['starred_url'], data['subscriptions_url'], 
                           data['organizations_url'], data['repos_url'], 
                           data['events_url'], data['received_events_url'], 
                           data['name'], data['company'], data['blog'], 
                           data['location'], data['email'], data['hireable'], 
                           data['bio'], data['public_repos'], 
                           data['public_gists'], data['followers'], 
                           data['following'], data['created_at'], 
                           data['updated_at'], etag)
    db.session.add(add_account)
    db.session.commit()

    account = Accounts.query.get(user)
    if DEBUG: print(f"Returning {account}")

    return account


def add_repos(user):
    """Adds repos information"""
    url = API_BASE + user + '/repos'
    response = requests.get(url)
    etag = response.headers['ETag']
    data = response.json()
    if DEBUG: print(f"Found {len(data)} repos")

    for repo in data:
        add_repo = Repos(repo['id'], user, repo['name'], repo['html_url'], 
                         repo['description'], repo['fork'], repo['language'], 
                         repo['created_at'], repo['pushed_at'], etag)
        db.session.add(add_repo)
        if DEBUG: print(f"Added repo {repo['name']}")
    db.session.commit()

    # Since there might be more than one, a list is used to hold them
    repos = []
    all_repos = Repos.query.all()

    for repo in all_repos:
        if repo.owner == user:
            repos.append(repo)

    if DEBUG: print(f"Returning {repos}")

    return repos


def add_gists(user):
    """Adds gists information"""
    url = API_BASE + user + '/gists'
    response = requests.get(url)
    etag = response.headers['ETag']
    data = response.json()
    if DEBUG: print(f"Found {len(data)} gists")

    for gist in data:
        files = []
        for file in gist['files']:
            files.append(file)
        if DEBUG: print(f'{len(files)} Files: {files}')
        add_gist = Gists(gist['id'], user, files[0], gist['html_url'], 
                         gist['description'], etag)
        db.session.add(add_gist)
        if DEBUG: print(f'Added gist {files[0]}')
    db.session.commit()

    # Since there might be more than one, a list is used to hold them
    gists = []
    all_gists = Gists.query.all()

    for gist in all_gists:
        if gist.owner == user:
            gists.append(gist)

    if DEBUG: print(f"Returning {gists}")

    return gists


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
