from flask import Flask
from inventory import show_inventory

app = Flask(__name__)

@app.route("/")
def hello():
    return show_inventory()

if __name__ == "__main__":
    app.run()