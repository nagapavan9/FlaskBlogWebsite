from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, length, Email, equal_to, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[data_required(), length(2, 20)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    confirm_password = PasswordField('Confirm_Password', validators=[data_required(),equal_to('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a new one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a new one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


