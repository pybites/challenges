from datetime import datetime, timedelta

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reading.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    pages = db.Column(db.Integer)
    pages_per_day = db.Column(db.Integer)
    start_page = db.Column(db.Integer)
    add_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, pages, pages_per_day, start_page):
        self.title = title
        self.pages = pages
        self.pages_per_day = pages_per_day
        self.start_page = start_page

    def __repr__(self):
        return '<Book %r>' % self.title


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    date = db.Column(db.DateTime)
    task = db.Column(db.String(20))
    done = db.Column(db.Boolean, default=False)
    complete_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, book_id, date, task):
        self.book_id = book_id
        self.date = date
        self.task = task

    def __repr__(self):
        return '<Task %r>' % self.task


@app.route('/')
def main():
    books = Book.query.all()

    query_progress = db.session.query(Task.book_id,
                                      db.func.count(db.case([(Task.done, 1)])),
                                      db.func.count(Task.book_id)
                                      ).group_by(Task.book_id).all()

    progress = {i[0]: i[1]/i[2] * 100
                for i in query_progress}

    return render_template('list.html', books=books, progress=progress)


@app.route('/book/<int:book_id>')
def show_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return redirect('/')

    book = Book.query.filter_by(id=book_id)[0]
    tasks = Task.query.filter_by(book_id=book_id)

    return render_template('book.html', book=book, tasks=tasks)


@app.route('/book/add', methods=['POST'])
def add_book():
    title = request.form['title'].title()
    title_in_db = Book.query.filter_by(title=title).first()
    if title_in_db:
        err = 'Title already in DB'
        return render_template('list.html', error=err)

    try:
        pages = int(request.form['pages'])
        pages_per_day = int(request.form['pages_per_day'])
        start_page = request.form['start_page']
        if not start_page:
            start_page = 1
        else:
            start_page = int(start_page)
    except ValueError as exc:
        return render_template('list.html', error=exc)

    new_book = Book(title, pages, pages_per_day, start_page)
    db.session.add(new_book)

    # http://stackoverflow.com/questions/28242523/get-inserted-key-before-commit-session
    # get the insert book id
    db.session.flush()
    bookid = new_book.id

    for i, firstpage in enumerate(range(start_page, pages, pages_per_day)):
        date = datetime.utcnow() + timedelta(days=i)
        lastpage = min(firstpage + pages_per_day, pages)
        task = '{}-{}'.format(firstpage, lastpage)
        new_task = Task(bookid, date, task)
        db.session.add(new_task)

    db.session.commit()

    return redirect('/')


@app.route('/book/delete/<int:book_id>')
def delete_book(book_id):
    Book.query.filter(Book.id == book_id).delete()
    # TODO set up relation / cascade
    Task.query.filter(Task.book_id == book_id).delete()

    db.session.commit()
    return redirect('/')


@app.route('/task/done/<int:task_id>')
def close(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect(request.referrer)

    task.done = True
    db.session.commit()
    return redirect(request.referrer)


@app.route('/task/undo/<int:task_id>')
def undo(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect(request.referrer)

    task.done = False
    db.session.commit()
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug=True)
