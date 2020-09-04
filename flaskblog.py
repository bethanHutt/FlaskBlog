from forms import RegistrationForm
from forms import LoginForm

from flask import flash
from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '5b1853e65ccc65c68c2563b39f4ca974'
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
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.  Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
