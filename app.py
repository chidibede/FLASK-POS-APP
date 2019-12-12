''' 
Main App Script (Entry Point) for Fruits and Wine 
Retail Point Of Sale.

Author: Chidi Bede Enwereji
Company: Emedia Bay
Client: Nelson Obiem
Client Company: 

'''
# Import Libraries needed
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Instantiate app
app = Flask("__name__")

# form security
app.config['SECRET_KEY'] = '9afddcaac4139568d4d46a6bd0f8127f'

# function that renders home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
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

# Running the app
if __name__ == "__main__":
    app.run(debug=True)