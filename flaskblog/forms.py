from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import data_required,length,Email,equal_to

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[data_required(), length(2, 20)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    confirm_password = PasswordField('Confirm_Password', validators=[data_required(),equal_to('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


