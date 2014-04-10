from flask import render_template
from app import app, db
from forms import SignupForm
from models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data,
                    form.email.data)
        db.session.add(user)

        try:
            db.session.commit()

    return render_template('signup.html',
                           form=form)
