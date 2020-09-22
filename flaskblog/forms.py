from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed

from wtforms import StringField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import TextAreaField

from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

from flaskblog.models import User

from flask_login import current_user


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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken.  '
                                  'Please choose a different one.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('That email is already registered.')


class UpdateAccountForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=20)])

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()])

    picture = FileField(
        'Update Profile Picture',
        validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data == current_user.username:
            return

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken.  '
                                  'Please choose a different one.')

    def validate_email(self, email):
        if email.data == current_user.email:
            return

        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('That email is already registered.')


class LoginForm(FormBase):
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()])

    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user is None:
            raise ValidationError(
                'There is no account with that email.  You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()])

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')])

    submit = SubmitField('Reset Password')
