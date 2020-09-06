from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import PasswordField

from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import DataRequired


class FormBase(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()])

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()])


class RegistrationForm(FormBase):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=20)])

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FormBase):
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
