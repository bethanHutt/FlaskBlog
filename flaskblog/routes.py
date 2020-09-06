from flask import flash
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from flaskblog import app
from flaskblog import db
from flaskblog import bcrypt

from flaskblog.forms import LoginForm
from flaskblog.forms import RegistrationForm

from flaskblog.models import Post
from flaskblog.models import User


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'April 20 2018'
    },
    {
        'author': 'Beth Hutt',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'April 21 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created!  You are now able to log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@ app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash('Login Unsuccessful.  Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@ app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@ app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
