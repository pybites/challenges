from flask import Flask, request
from flask import render_template
from flask import redirect
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clamytoe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)

    def __init__(self, task, status=True):
        self.task = task
        self.status = status

    def __repr__(self):
        return '<Task %s>' % self.task


db.create_all()


@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template('clamytoe.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    
    if not task:
        return redirect('/')

    status = int(request.form['status'])

    new_task = Tasks(task, status)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/clear')
def clear_all():
    db.drop_all()
    db.create_all()
    return redirect('/')


@app.route('/close/<int:task_id>')
def close_task(task_id):
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')

    if task.status:
        task.status = False
    else:
        task.status = True

    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
