# ChoreInator - Family Chore Management System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-orange.svg)](https://www.sqlalchemy.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4.5.2-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

ChoreInator is a **full-stack web application** designed to help families manage household chores and reward systems through gamification. This project demonstrates proficiency in **Flask development**, **SQLAlchemy ORM**, **user authentication**, **role-based access control**, and **responsive web design** - essential skills for modern software engineering positions.

The application allows parents to assign chores to their children, verify completed chores, and manage a reward system using points. Children can mark chores as complete, view their earned points, and redeem rewards through an intuitive, secure interface.

**🔗 Live Demo**: *Local deployment at http://127.0.0.1:5000*

## 🚀 Features

- **Multi-user roles**: Admin, Parent, and Child accounts with role-based permissions
- **Chore management**: Complete workflow to assign, complete, and verify chores
- **Points system**: Gamified reward system where children earn points for completed chores
- **Reward marketplace**: Children can redeem points for parent-defined rewards
- **Family organization**: Users are organized into family units with data isolation
- **Verification system**: Two-step process where parents must verify chores before points are awarded
- **Responsive Design**: Mobile-friendly interface using Bootstrap framework
- **Secure Authentication**: Password hashing and session management

---

## 🛠️ Technology Stack

| **Component** | **Technology** |
|---------------|----------------|
| **Backend** | Python 3.8+, Flask 2.3.0 |
| **Database** | SQLite with SQLAlchemy ORM |
| **Frontend** | HTML5, CSS3, Bootstrap 4.5.2, Jinja2 |
| **Authentication** | Flask-Login, Werkzeug Security |
| **Architecture** | MVC Pattern, RESTful Design |

---

## 📦 Installation

### **Prerequisites**
- Python 3.8 or higher
- SQLite (included in Python)
- pip (Python package manager)
- Git (for cloning repository)

### **Quick Start**
```bash
# Clone the repository
git clone https://github.com/yourusername/chorinator.git
cd chorinator

# Create and activate virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### **Alternative Setup (Manual Installation)**
```bash
# Navigate to project directory
cd path/to/Final_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Install required packages
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug

# Start the application
python app.py
```

### **Database Initialization**
The SQLite database will be automatically created when you run the application for the first time in the `instance/choreinator.db` location.

---

## 🚀 Running the Application

### **Local Development Server**
```bash
# Method 1: Command line
python app.py

# Method 2: VS Code
# Open app.py in VS Code and run with F5 or "Run Python File"

# Method 3: Flask CLI
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### **Access Points**
- **Main Application**: http://127.0.0.1:5000
- **Registration Page**: http://127.0.0.1:5000/register
- **Admin Dashboard**: http://127.0.0.1:5000/admin (after admin login)

### **Demo Credentials**
- **Admin**: `admin` / `password123`
- **Test Parent**: `parent1` / `password123` (if exists in your DB)
- **Test Child**: `child1` / `password123` (if exists in your DB)

---

## 💻 User Guide

### System Roles

The application has three user roles, each with different permissions:

- **Admin**: Creates families and assigns users to families
- **Parent**: Assigns chores, verifies completed chores, and manages rewards
- **Child**: Completes chores and redeems rewards

### **Initial Setup/Registration**

1. **Access the application** at http://127.0.0.1:5000
2. **Log in as admin**
   - Username: `admin`
   - Password: `password123`
3. **Create a family** from the admin panel
4. **Register new users** (parents and children)
   - Go to http://127.0.0.1:5000/register to create new accounts
   - Choose either "Parent" or "Child" as the role
5. **Assign users to families** from the admin panel
   - Log in as admin, select users from the list, and assign them to a family

### **For Parents**

1. **Log in** with your parent account
2. **Assign chores**
   - Click "Assign Chore" button
   - Fill in the chore details (title, description, reward points)
   - Select the child to assign the chore to
   - Submit the form
3. **View chores**
   - View assigned chores for all children in your family
   - Verify completed chores in the "Chores Pending Verification" section
   - Only after parent verification will points be awarded to the child
4. **Manage rewards**
   - Add new rewards with the "Add New Reward" form (name and point cost)
   - Monitor redeemed rewards in the "Family Rewards" section
   - Remove rewards after fulfilling them by clicking the "Remove" button

### **For Children**

1. **Log in** with your child account
2. **View assigned chores** on the dashboard
3. **Complete chores**
   - View chore details and instructions
   - Click "Mark as Complete" when finished
   - Wait for parent verification
   - After verification, points will be added to your account
4. **Check points** displayed on your dashboard
5. **Redeem rewards**
   - Click "Visit Reward Store"
   - Browse available rewards
   - Redeem rewards by clicking "Redeem" if you have enough points

---

## ⚡ Verification System

ChoreInator implements a sophisticated verification process to ensure chores are properly completed:

1. **Child Action**: Marks a chore as complete
2. **Pending State**: The chore appears in the parent's "Chores Pending Verification" section
3. **Parent Verification**: Parent reviews and verifies the chore completion
4. **Point Award**: Points are awarded to the child only after verification
5. **Reward Redemption**: The child can then use these points to redeem rewards

This system prevents point manipulation and ensures accountability in the chore completion process.

---

## 🔐 Security Features

- **Password Security**: Werkzeug hashing with salts for secure password storage
- **Session Management**: Flask-Login handles secure user sessions
- **Role-Based Access**: `@login_required` decorators protect sensitive routes
- **Data Validation**: Server-side input validation and sanitization
- **Family Isolation**: Proper database relationships prevent cross-family data access

---

## 🏗️ Architecture & File Structure

```
chorinator/
├── app.py                 # Main application file with routes and models
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore configuration
├── templates/           # HTML templates directory
│   ├── index.html       # Home/landing page
│   ├── login.html       # User authentication
│   ├── register.html    # New user registration
│   ├── dashboard.html   # Role-based main interface
│   ├── admin.html       # Admin management panel
│   ├── assign_chore.html # Chore assignment form
│   └── rewards.html     # Rewards marketplace
└── instance/            # Auto-generated directory
    └── choreinator.db   # SQLite database file
```

### **MVC Architecture**
- **Models**: SQLAlchemy ORM classes defined in `app.py`
- **Views**: Jinja2 templates stored in the `templates` directory
- **Controllers**: Flask routes with business logic and error handling

---

## 🔧 Troubleshooting & Common Issues

### **Application Issues**
- **Login issues**: Ensure usernames and passwords are entered correctly
- **Missing rewards or chores**: Verify that users are assigned to the correct family
- **Permission errors**: Ensure proper role assignments in admin panel

### **Database Issues**
If you encounter database errors:
- Delete the `instance/choreinator.db` file
- Restart the application to create a fresh database
- Log in with the default admin account and set up your families again

### **Development Issues**
- **Port conflicts**: If port 5000 is in use, Flask will automatically try port 5001
- **Virtual environment**: Always activate your virtual environment before running
- **Dependencies**: Use `pip install -r requirements.txt` to ensure all packages are installed

---

## 🚀 Advanced Usage

### **Environment Variables**
```bash
# Optional: Set environment variables for production
export FLASK_APP=app.py
export FLASK_ENV=development  # or production
export SECRET_KEY=your-secret-key-here
```

### **Database Management**
```python
# Reset database (run in Python shell)
from app import app, db
with app.app_context():
    db.drop_all()
    db.create_all()
```

---

## 📈 Technical Achievements

- **Full-Stack Development**: Complete web application with frontend and backend
- **Database Design**: Normalized schema with complex relationships
- **Security Implementation**: Authentication, authorization, and data protection
- **User Experience**: Responsive design with role-based interfaces
- **Business Logic**: Complex workflow management and gamification systems

---

## 🔮 Future Enhancements

- [ ] **RESTful API**: JSON endpoints for mobile app integration
- [ ] **Email Notifications**: Alerts for completed chores and rewards
- [ ] **Advanced Analytics**: Family productivity dashboards
- [ ] **Mobile App**: React Native or Flutter companion
- [ ] **Docker Deployment**: Containerization for cloud platforms
- [ ] **Unit Testing**: Comprehensive test suite with pytest

---

## 📊 Development Notes

### **Security Note**
This application is designed for educational purposes and local use. The default admin credentials should be changed for any extended use.

### **Common Tasks**

#### **Resetting a Password**
Currently, there is no built-in password reset functionality. For educational purposes, you can:
1. Delete the database file (`instance/choreinator.db`)
2. Restart the application
3. Set up users again

#### **Adding New Features**
The application is built with Flask and follows a standard MVC architecture:
- Models are defined at the top of `app.py`
- Routes/controllers are defined as Flask routes
- Views are stored in the `templates` directory as HTML files

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

### **Development Guidelines**
- Follow Python PEP 8 style guidelines
- Add comprehensive comments for complex business logic
- Test all new features thoroughly
- Update documentation for any new functionality

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

**Joseph I. Laible 

💼 **LinkedIn**: linkedin.com/in/joelaible  
📧 **Email**: joseph.i.laible@gmail.com

---

## 🎓 Educational Context

This project was developed as part of CSE 682 Software Engineering at Syracuse University, demonstrating practical application of:
- **Software Engineering Principles**: Requirements analysis, design patterns, testing
- **Web Development**: Full-stack development with modern frameworks
- **Database Design**: Relational database modeling and implementation
- **Security**: Authentication, authorization, and secure coding practices
- **Project Management**: Version control, documentation, and professional presentation

---

*Built with ❤️ using Python, Flask, SQLAlchemy, and Bootstrap. This project showcases technical competence in full-stack web development and software engineering best practices.*


