# Chore-Inator: Family Chore Management System

## Overview

Chore-Inator is a web application designed to help families manage household chores and reward systems. The application allows parents to assign chores to their children, verify completed chores, and manage a reward system using points. Children can mark chores as complete, view their earned points, and redeem rewards.

## Features

- **Multi-user roles**: Admin, Parent, and Child accounts
- **Chore management**: Assign, complete, and verify chores
- **Points system**: Children earn points for completed chores
- **Reward marketplace**: Children can redeem points for rewards
- **Family organization**: Users are organized into family units
- **Verification system**: Parents must verify chores before points are awarded

## Installation

### Prerequisites

- Python 3.8 or higher
- SQLite (included in Python)
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the project**

   Download the project files to your computer.

2. **Set up a virtual environment (recommended)**

   Navigate to the project directory
   cd path/to/Final_project

   Create a virtual environment
   python -m venv venv

   Activate the virtual environment
   For Windows:
   venv\Scripts\activate

   For macOS/Linux:
   source venv/bin/activate

3. **Install required packages**
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug

4. **Initialize the database**

The database will be automatically created when you run the application for the first time. (in "project folder name"/instance)

## Running the Application

1. **Start the server**
python app.py 
or run in vs


2. **Access the application**

Open your web browser and go to: http://127.0.0.1:5000

## User Guide

### System Roles

The application has three user roles, each with different permissions:

- **Admin**: Creates families and assigns users to families
- **Parent**: Assigns chores, verifies completed chores, and manages rewards
- **Child**: Completes chores and redeems rewards

### Initial Setup/Registration

1. **Access the application** at http://127.0.0.1:5000
2. **Log in as admin**
- Username: admin
- Password: password123
3. **Create a family** from the admin panel
4. **Register new users** (parents and children)
- Go to http://127.0.0.1:5000/register to create new accounts
- Choose either "Parent" or "Child" as the role
5. **Assign users to families** from the admin panel
- Log in as admin, select users from the list, and assign them to a family

### For Parents

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

### For Children

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

## Verification System

Chore-Inator implements a verification process to ensure chores are properly completed:

1. Child marks a chore as complete
2. The chore appears in the parent's "Chores Pending Verification" section
3. Parent verifies the chore
4. Points are awarded to the child only after verification
5. The child can then use these points to redeem rewards

## Troubleshooting

- **Login issues**: Ensure usernames and passwords are entered correctly
- **Missing rewards or chores**: Verify that users are assigned to the correct family
- **Database errors**: If you encounter database errors:
  - Delete the instance/choreinator.db file
  - Restart the application to create a fresh database
  - Log in with the default admin account and set up your families again

## Security Note

This application is designed for educational purposes and local use. The default admin credentials should be changed for any extended use.

## File Structure

- **app.py**: Main application file with routes and models
- **templates/**: HTML templates for the application views
- **instance/choreinator.db**: SQLite database file (created on first run)

## Common Tasks

### Resetting a Password
Currently, there is no built-in password reset functionality. For educational purposes, you can:
1. Delete the database file
2. Restart the application
3. Set up users again

### Adding New Features
The application is built with Flask and follows a standard MVC architecture:
- Models are defined at the top of app.py
- Routes/controllers are defined as Flask routes
- Views are stored in the templates directory as HTML files


