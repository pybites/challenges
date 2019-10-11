from app import app, db
from flask import render_template, request, redirect
from app.forms import TextForm
from app.models import Something

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/data-enter', methods=['GET', 'POST'])
def data_enter():
    form = TextForm()
    if form.validate_on_submit():
        title = request.form['title']
        text = request.form['text']

        signature = Something(title=title, text=text)
        db.session.add(signature)
        db.session.commit()
        return redirect('/list')
    return render_template('data_enter.html', form=form)

@app.route('/list')
def list():
    list_items = Something.query.all()
    return render_template('list.html', list_items=list_items)

@app.route('/list/<int:post_id>')
def show_post(post_id):
    post = Something.query.filter_by(id=post_id).first()
    return render_template('post.html', post=post)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    post = Something.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/list')




