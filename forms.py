''' 
Login and registration forms script from flask-wtf forms module

'''

# Import Libraries needed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Class that creates and validates registration
class RegistrationForm(FlaskForm):
    # Dropdown lists
    roles = [('dash', '---'),('adm', 'Admin'), ('fm','Financial manager'), ('op','Operator')]

    # The form fields for registration
    fullname = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators=[Email()])
    role = SelectField('Staff Role', choices=roles)
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Class that creates and validates registration
class LoginForm(FlaskForm):
    # Form fields for login
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2)])
    login = SubmitField('Login')
  