# ChoreInator - Family Chore Management System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-orange.svg)](https://www.sqlalchemy.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4.5.2-purple.svg)](https://getbootstrap.com/)

## 🎯 Project Overview

A **full-stack web application** designed to streamline family chore management through gamification and reward systems. This project demonstrates proficiency in **backend development**, **database design**, **user authentication**, **role-based access control**, and **responsive UI development** - key skills sought by employers for entry-level software engineering positions.

**🔗 Live Demo**: *Local deployment at http://127.0.0.1:5000*

---

## 💼 Professional Skills Demonstrated

### **Backend Development**
- **Python & Flask Framework**: RESTful API design, server-side logic, and MVC architecture
- **Database Design & ORM**: SQLAlchemy for complex relationships, query optimization, and data integrity
- **Authentication & Security**: Password hashing (Werkzeug), session management, CSRF protection
- **Error Handling**: Comprehensive exception handling with user feedback systems

### **Frontend Development**
- **Responsive Design**: Bootstrap CSS framework for mobile-first, cross-browser compatibility
- **Template Engine**: Jinja2 for dynamic content rendering and data binding
- **User Experience**: Intuitive navigation, form validation, and interactive feedback
- **Modern Web Standards**: HTML5, CSS3, and JavaScript integration

### **Software Engineering Practices**
- **Architecture Patterns**: Clean MVC separation, modular code organization
- **Version Control**: Git workflow with meaningful commits and professional documentation
- **Database Management**: Normalized schema design, foreign key relationships, data migrations
- **Code Quality**: Comprehensive documentation, PEP 8 standards, and maintainable structure

---

## 🚀 Key Features & Technical Implementation

### **Multi-Tier Authentication System**
- Role-based access control (Admin, Parent, Child)
- Secure password hashing with Werkzeug
- Session management with Flask-Login
- Decorator-based route protection

### **Dynamic Role-Based Dashboards**
- Customized interfaces based on user permissions
- Real-time data updates and state management
- Conditional rendering with Jinja2 templates

### **Gamification & Business Logic**
- Points-based reward system with transaction tracking
- Two-step verification workflow (complete → verify → award points)
- Complex business rules and validation

### **Database Architecture**
```sql
Users ←→ Families ←→ Chores
  ↓         ↓        ↓
Points   Rewards   Verification
