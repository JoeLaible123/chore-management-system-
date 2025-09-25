%#Joseph I Laible 


# It also contains the database models and the main logic for the application.
# The application is a web-based application that allows parents to assign chores to their children and reward them with points.
# The application is built using Flask, SQLAlchemy, and Flask-Login.
# The application uses SQLite as the database.
# The application is designed to be run on a local server using Flask's built-in server.
#Note: Ref lines309-315 for the default admin user creation. 

#References for creation and future adjustments:
# Using sqlite databases with flask-  
# https://flask.palletsprojects.com/en/stable/patterns/sqlite3/ 
# https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/
# https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
# https://flask.palletsprojects.com/en/stable/tutorial/database/ 

#using flask and HTML integration for the web application-
#https://flask.palletsprojects.com/en/stable/tutorial/templates/
#https://www.geeksforgeeks.org/template-inheritance-in-flask/

#main flask reference documentation- 
# https://flask.palletsprojects.com/en/stable/quickstart/
# https://flask.palletsprojects.com/en/stable/



#demo logins -in current DB(s)
#Admin: admin/password123
#Parent: Parent1/password123
#Child: child1/password123

# http://127.0.0.1:5000  -# This is the main URL for the application -login page
# http://127.0.0.1:5000/register  #-# This is the registration page for new users 

from flask import Flask, render_template, request, redirect, url_for, flash, session  # Import necessary modules and classes from flask import jsonify 
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database interactions 
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user # Import necessary classes and functions from flask_login
from werkzeug.security import generate_password_hash, check_password_hash # Import password hashing functions 

# Initialize Flask app - Flask is a lightweight, flexible, and easy-to-use Python microframework for building web applications and APIs
app = Flask(__name__) # Create Flask app instance
app.config['SECRET_KEY'] = 'supersecretkey' # Set a secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///choreinator.db' # Database URI for SQLite database
db = SQLAlchemy(app) # Initialize SQLAlchemy with the Flask app 
login_manager = LoginManager() # Initialize LoginManager for user session management 
login_manager.init_app(app) # Initialize the login manager with the Flask app 
login_manager.login_view = 'login' # Set the login view for unauthorized access 

#using db.models to create the database tables for the application
# This is a base class from the Flask-SQLAlchemy.
# It represents a database table. By inheriting from db.Model, the follow on class' are mapped to a table in the database.
# User Model 
class User(UserMixin, db.Model): # Inherit from UserMixin for session management 
    id = db.Column(db.Integer, primary_key=True) # Primary key for the user table
    username = db.Column(db.String(150), unique=True, nullable=False) # Unique username for the user
    password_hash = db.Column(db.String(256), nullable=False) # Password hash for security
    role = db.Column(db.String(20), nullable=False)  # Admin, Parent, Child # User role
    family_id = db.Column(db.Integer, db.ForeignKey('family.id')) # Foreign key to link to the Family table 
    points = db.Column(db.Integer, default=0) # Points for the user 

    def set_password(self, password): # Method to set the password hash 
        self.password_hash = generate_password_hash(password)

    def check_password(self, password): # Method to check the password hash 
        return check_password_hash(self.password_hash, password)

# Family Model
class Family(db.Model): # Inherit from db.Model for database table representation 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    members = db.relationship('User', backref='family', lazy=True)

# Chore Model
class Chore(db.Model): # Inherit from db.Model for database table representation 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    reward_points = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    verified = db.Column(db.Boolean, default=False)  
    user = db.relationship('User', backref='chores')


# Reward Model
class Reward(db.Model): #@ Inherit from db.Model for database table representation 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    point_cost = db.Column(db.Integer, nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'))
    redeemed_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    redeemer = db.relationship('User', foreign_keys=[redeemed_by])  # Add this line


@login_manager.user_loader #@ This decorator loads the user from the user ID stored in the session
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/') #@ This route handles the home page of the application
def home():
    return render_template('index.html')

@app.route('/create_family', methods=['POST']) #@ This route handles the creation of a new family
@login_required #@ This decorator ensures that the user is logged in before accessing this route 
def create_family(): #@ This function creates a new family in the database
    if current_user.role != 'Admin':
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('admin'))

    family_name = request.form['family_name']
    if Family.query.filter_by(name=family_name).first():
        flash('Family name already exists!', 'danger')
    else:
        new_family = Family(name=family_name)
        db.session.add(new_family)
        db.session.commit()
        flash(f'Family "{family_name}" created successfully!', 'success')

    return redirect(url_for('admin'))


@app.route('/assign_family', methods=['POST']) #@ This route handles the assignment of a user to a family
@login_required #@ This decorator ensures that the user is logged in before accessing this route
def assign_family(): #@ This function assigns a user to a family in the database
    if current_user.role != 'Admin':
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('admin'))

    user_id = request.form['user_id']
    family_id = request.form['family_id']

    user = User.query.get(user_id)
    family = Family.query.get(family_id)

    if user and family:
        user.family_id = family.id 
        db.session.commit() #@ Commit the changes to the database
        flash(f'User {user.username} assigned to {family.name}!', 'success')
    else:
        flash('Invalid user or family selection.', 'danger')

    return redirect(url_for('admin'))


@app.route('/complete_chore/<int:chore_id>') #@ This route handles the completion of a chore by a child
@login_required #@ This decorator ensures that the user is logged in before accessing this route
def complete_chore(chore_id): #@ This function marks a chore as completed in the database 
    chore = Chore.query.get(chore_id)
    if chore and chore.assigned_to == current_user.id:
        chore.completed = True
        db.session.commit()
        flash('Chore marked as completed! Waiting for parent verification.', 'success')
    else:
        flash('Unauthorized action!', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/admin') #@ This route handles the admin dashboard where admin can manage families and users
@login_required
def admin():
    if current_user.role != 'Admin':
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('dashboard'))

    families = Family.query.all()
    users = User.query.all()
    return render_template('admin.html', families=families, users=users)



@app.route('/assign_chore', methods=['GET', 'POST'])
@login_required #@ This route handles the assignment of chores to children by parents 
def assign_chore():
    if current_user.role != 'Parent':
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        reward_points = int(request.form['reward_points'])
        assigned_to = int(request.form['assigned_to'])
        
        chore = Chore(title=title, description=description, reward_points=reward_points, assigned_to=assigned_to)
        db.session.add(chore)
        db.session.commit()
        flash('Chore assigned successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    children = User.query.filter_by(family_id=current_user.family_id, role='Child').all()
    return render_template('assign_chore.html', children=children)


@app.route('/register', methods=['GET', 'POST']) #@ This route handles the registration of new users 
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        family_id = request.form.get('family_id', None)
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, role=role, family_id=family_id)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST']) #@ This route handles the login of users
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')

            # Redirect based on role
            if user.role == 'Admin':
                return redirect(url_for('admin'))
            return redirect(url_for('dashboard'))
        
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


@app.route('/logout') #@ This route handles the logout of users
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard') #@ This route handles the dashboard for users
@login_required
def dashboard():
    if current_user.role == "Child":
        # Fetch only chores assigned to the logged-in child
        chores = Chore.query.filter_by(assigned_to=current_user.id).all()
        return render_template('dashboard.html', user=current_user, chores=chores)

    elif current_user.role == "Parent":
        family_children = User.query.filter_by(family_id=current_user.family_id, role='Child').all()
        rewards = Reward.query.filter_by(family_id=current_user.family_id).all()
        return render_template('dashboard.html', user=current_user, family_children=family_children, rewards=rewards)

    return redirect(url_for('home'))

@app.route('/rewards', methods=['GET']) ##@ This route handles the rewards page for users
@login_required
def rewards():
    if current_user.role == 'Child':
        rewards = Reward.query.filter_by(family_id=current_user.family_id).all()
        return render_template('rewards.html', user=current_user, rewards=rewards)
    return redirect(url_for('dashboard'))

@app.route('/redeem_reward/<int:reward_id>') #@ This route handles the redemption of rewards by children
@login_required
def redeem_reward(reward_id):
    reward = Reward.query.get(reward_id)
    if reward and current_user.points >= reward.point_cost:
        current_user.points -= reward.point_cost
        reward.redeemed_by = current_user.id
        db.session.commit()
        flash(f'Reward "{reward.name}" redeemed!', 'success')
    else:
        flash('Not enough points to redeem this reward.', 'danger')
    return redirect(url_for('rewards'))

@app.route('/remove_redeemed_reward/<int:reward_id>', methods=['POST'])
@login_required
def remove_redeemed_reward(reward_id):
    if current_user.role == 'Parent':
        reward = Reward.query.get(reward_id)
        if reward and reward.redeemed_by:
            db.session.delete(reward)
            db.session.commit()
            flash('Redeemed reward removed successfully!', 'success')
        else:
            flash('Invalid reward or not redeemed.', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/add_reward', methods=['POST']) #@ This route handles the addition of new rewards by parents
@login_required
def add_reward():
    if current_user.role == 'Parent':
        name = request.form['name']
        point_cost = int(request.form['point_cost'])
        reward = Reward(name=name, point_cost=point_cost, family_id=current_user.family_id)
        db.session.add(reward)
        db.session.commit()
        flash('Reward added successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/verify_chore/<int:chore_id>', methods=['POST']) #@ This route handles the verification of completed chores by parents
@login_required
def verify_chore(chore_id):
    if current_user.role != 'Parent':
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('dashboard'))

    chore = Chore.query.get(chore_id)
    if chore and chore.completed and chore.user.family_id == current_user.family_id: #@ Check if the chore is completed and belongs to the same family
        chore.verified = True #@ Mark the chore as verified
        chore.user.points += chore.reward_points  # Award points to the child
        db.session.commit()
        flash(f'Chore "{chore.title}" verified! Points awarded to {chore.user.username}.', 'success')
    else:
        flash('Invalid chore or unauthorized action.', 'danger')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context(): #@ This context manager is used to run the app in a context where the database is available
        db.create_all() ## Create the database tables if they don't exist
        # Create default admin user if not exists
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', role='Admin', family_id=None)
            admin.set_password('password123') ## Set a default password for the admin user********
            db.session.add(admin)
            db.session.commit()
            print("Admin account created: Username: admin, Password: password123")
    app.run(debug=True)
