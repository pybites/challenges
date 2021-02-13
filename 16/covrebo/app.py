from flask import Flask, render_template
import services

app = Flask(__name__)


@app.route('/')
def hello_world():
    # get dad joke
    joke = services.get_dad_joke()
    return render_template('index.html', title='Funny', joke=joke)
