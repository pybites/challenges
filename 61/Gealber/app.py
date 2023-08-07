from flask import Flask, request, render_template
from string import ascii_letters, digits
import random

app = Flask(__name__)

s = "".join([ascii_letters,digits])

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":        
        url_id = "".join(random.sample(s,5))
        return render_template('index.html', url=f'https://pybit.es/{url_id}')
    else:
        return "Method not allowed"

if __name__ == "__main__":
    app.run(debug=True)