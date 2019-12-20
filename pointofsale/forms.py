''' All Application Forms Script '''

# Libraries needed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from pointofsale.models import  User


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

    def validate_username(self, username):
        '''
            Function to add extra validations to username
            to make sure username doesn't already exist
        '''
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists, try a new username')
    
    def validate_fullname(self, fullname):
        '''
            Function to add extra validations to fullname
            to make sure username doesn't already exist
        '''
        user = User.query.filter_by(fullname=fullname.data).first()
        if user:
            raise ValidationError('fullname already exists, try a new fullname')
    
    def validate_email(self, email):
        '''
            Function to add extra validations to email
            to make sure username doesn't already exist
        '''
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists, try a new email')

# Class that creates and validates login of users
class LoginForm(FlaskForm):
    # Form fields for login
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2)])
    login = SubmitField('Login')
