from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# personal email account secrets not in repo
from flaskblog.config_secrets import Secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b1853e65ccc65c68c2563b39f4ca974'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = Secrets.username
app.config['MAIL_PASSWORD'] = Secrets.password
mail = Mail(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# function name for login route
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes
