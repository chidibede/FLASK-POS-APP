from app import app, db, bcrypt
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app.models import User


''' App Routes '''
# function that renders home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        fullname = form.fullname.data
        username = form.username.data
        email = form.email.data
        role = form.role.data
        user = User(fullname=fullname, username=username, email=email, role=role, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created Succesfully for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'chidibede' and form.password.data == '111':
            flash('Logged in Successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username or Password incorrect, Try again!', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


