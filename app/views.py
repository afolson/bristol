from flask import render_template, redirect, url_for, request
from flask.ext import uploads
from app import app, db, login_manager
from app.models import User
from app.forms import SignupForm, PoopForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    form = PoopForm(request.form)
    if request.method == 'POST' and form.validate():
        uploads.save(request.files['upload'])
        return redirect(url_for('index'))
    return render_template('post.html', form=form)
