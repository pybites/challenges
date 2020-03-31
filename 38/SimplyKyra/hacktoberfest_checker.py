import os
import bottle
import github
import collections
import yaml
import datetime

app = bottle.Bottle()


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return bottle.template('hello_template', name=name)


@app.get('/hacktoberfest')
def hacktoberfest():
    return '''
        <p>Enter user(s) you want to search for seperated by a comma.</p>
        <form action="/hacktoberfest" method="post">
            User: <input name="user" type="text"/>
        </form>
    '''


@app.post('/hacktoberfest')
def do_hacktoberfest() -> str:
    """
    Grabs the github personal access token to create a github stream with the token. If this fails it creates
    an non-token github access. Grabs the current date to determine which October the results should be for
    (this year if October or later and last year's date if before October). The gets user entered user names
    (seperated by commas) to search for one+ people and return the results in a string format to print.
    :return:
    """
    try:
        with open(f"{os.environ['HOME']}/.config/python_100days_config.yaml", 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        token = config['github']['personal-access-token']
        gh = github.Github(token)
    except:
        gh = github.Github()

    curr_date = datetime.date.today()
    if curr_date.month < 10:
        curr_year = curr_date.year - 1
    else:
        curr_year = curr_date.year

    users = [x.strip() for x in bottle.request.forms.get('user').split(',')]

    msg = f"For October of {curr_year}: </br>"

    for user in users:
        my_query = (
            f"-label:invalid created:{curr_year}-09-30T00:00:00-12:00..{curr_year}-10-31T23:59:59-12:00 "
            f"type:pr is:public author:{user}"
        )
        resulting_issues = github.Github.search_issues(gh, my_query)
        msg += return_message_for_user(user, resulting_issues)

    return msg


def return_message_for_user(user:str, results:github.PaginatedList.PaginatedList) -> str:
    """
    Creates a string showing the user's name (param user) and how many pull requests they got back
    (param results) along with a helpful message.
    :param user:
    :param results:
    :return:
    """
    return_message = f"</br>Hey {user}. "

    switcher = {
        0:'It\'s not too late to start!',
        1:'Off to a great start, keep going!',
        2:'Half way there, keep it up!',
        3:'So close!',
        4:'Way to go!',
        5:'Now you\'re just showing off!'
    }

    return_message += f"You have {results.totalCount} pull request(s). "

    if results.totalCount > 4:
        return_message += switcher[5]
    else:
        return_message += switcher[results.totalCount]

    return_message += "</br>"
    return return_message


if __name__ == "__main__":
    bottle.TEMPLATE_PATH = [os.path.dirname(os.path.abspath(__file__)) + '/views/']
    gh = github.Github()
    app.run(host='localhost', port=8080, debug=True)


