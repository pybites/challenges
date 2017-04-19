from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clamytoe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Tasks(db.Model):
    """Database schema"""
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)

    def __init__(self, task, status=True):
        self.task = task
        self.status = status

    def __repr__(self):
        return '<Task %s>' % self.task


# initialize the database
db.create_all()


@app.route('/')
def index():
    """Home page of the app
    
    It loads the template page and passes on any current tasks that exist.
    """
    tasks = Tasks.query.all()
    return render_template('clamytoe.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    """Adds a new task
    
    Redirexts to home page is there is no task.
    """
    task = request.form['task']
    
    if not task:
        return redirect('/')

    status = bool(int(request.form['status']))

    new_task = Tasks(task, status)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Deletes task by its ID
    
    If the task does not exist, redirects to home page.
    """
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/close/<int:task_id>')
def close_task(task_id):
    """Changes the state of a task
    
    If the task is open, it closes it. If it's close, it opens it.
    Redirects to home page if the task does not exists.
    """
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')

    if task.status:
        task.status = False
    else:
        task.status = True

    db.session.commit()
    return redirect('/')


@app.route('/clear')
def clear_all():
    """Dumps all tasks from the database
     
     It then re-initializes the database for continued use.
     """
    db.drop_all()
    db.create_all()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
