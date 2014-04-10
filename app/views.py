from flask import render_template
from app import app, db
from app.models import User
from app.forms import SignupForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data,
                    form.name.data,
                    form.email.data,
                    form.password.data)
        db.session.add(user)
        flash('Thanks, have fun shittin!')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html',
                           form=form)
