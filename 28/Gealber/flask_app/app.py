from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def show_plot():
    return render_template("report.html") 


if __name__ == '__main__':
    app.run(debug=True)