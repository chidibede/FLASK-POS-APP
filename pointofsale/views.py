''' Application views script'''

# Libraries and imports needed
from pointofsale import app, db, bcrypt
from flask import Flask, render_template, url_for, flash, redirect, request
from pointofsale.forms import RegistrationForm, LoginForm, ProductForm
from pointofsale.models import User, Product, Product_Category
from flask_login import login_user, logout_user, current_user, login_required


# function that renders home page
@app.route('/')
@app.route('/home')
def home():
    '''
     Function that renders the homepage
     of the app
    '''
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
     Function that renders the registration page
     of the app and creates the user that registered
    '''
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
    '''
     Function that renders the Login
     page of the app
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            return redirect('dashboard')
        else:
            flash('Username or Password incorrect, Try again!', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    '''
     Function that logs out user
    '''
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/inventory')
@login_required
def inventory():
    form = ProductForm()
    products = Product.query.all()
    return render_template('inventory.html', form=form, products=products)

@app.route('/employee')
def employee():
    employees = User.query.all()
    return render_template('employee.html', employees=employees)

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@app.route('/details')
def details():
    return render_template('details.html')


@app.route('/add_product', methods=['POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        cost_price = form.cost_price.data
        selling_price = form.selling_price.data
        category = str(form.category.data)
        product = Product(name=name, description=description,
                            cost_price=cost_price, selling_price=selling_price, category=category, staff=current_user )
        db.session.add(product)
        db.session.commit()
        flash(f'Product Added Succesfully', 'success')
        return redirect(url_for('inventory'))
    return render_template('inventory.html',  form=form)

@app.route('/add_category', methods=['GET','POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['category']
        product_category = Product_Category(name=name)
        db.session.add(product_category)
        db.session.commit()
        flash(f'Product Category Added Succesfully', 'success')
        return redirect(url_for('inventory'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method =='POST':
        oldname = request.form['oldname']
        name = request.form['name']
        description = request.form['desc']
        cost_price = request.form['cost_price']
        selling_price = request.form['selling_price']
        category = request.form['category']
        product = Product.query.filter_by(name=oldname).first()
        product.name = name
        product.description = description
        product.cost_price = cost_price
        product.selling_price = selling_price
        product.category = category
        db.session.commit()
        flash(f'Product Updated Succesfully', 'success')
        return redirect(url_for('inventory'))
    
@app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method =='POST':
        oldname = request.form['oldname']
        name = request.form['name']
        quantity_g = int(request.form['quantity_g'])
        quantity_unit = int(request.form['quantity_unit'])
        product = Product.query.filter_by(name=oldname).first()
        product.qty_g = quantity_g
        product.qty_units = quantity_unit
        db.session.commit()
        flash(f'Product Stocked Succesfully', 'success')
        return redirect(url_for('inventory'))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method =='POST':
        name = request.form['name']
        product = Product.query.filter_by(name=name).first()
        db.session.delete(product)
        db.session.commit()
        flash(f'Product Deleted Succesfully', 'success')
        return redirect(url_for('inventory'))

@app.route('/employee_update', methods=['GET', 'POST'])
def employee_update():
    if request.method =='POST':
        oldname = request.form['oldname']
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        role = request.form['role']
        employee = User.query.filter_by(fullname=oldname).first()
        employee.fullname = fullname
        employee.username = username
        employee.email = email
        employee.role = role
        db.session.commit()
        flash(f'Employee Info Updated Succesfully', 'success')
        return redirect(url_for('employee'))

@app.route('/employee_delete', methods=['POST'])
def employee_delete():
    if request.method =='POST':
        name = request.form['name']
        employee = User.query.filter_by(fullname=name).first()
        db.session.delete(employee)
        db.session.commit()
        flash(f'User Deleted Succesfully', 'success')
        return redirect(url_for('employee'))