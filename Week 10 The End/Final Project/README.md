# **Login System with JavaScript, Python, and MySQL**

📽️ **Video Demo**: https://youtu.be/5L4S0YfvxWE

## 📝 **Description**

The **Login System with JavaScript, Python, and MySQL** is a full-stack web application that enables user registration and login with secure authentication. Built using **Python (Flask)** for the backend and **MySQL** for data storage, the system demonstrates how to securely handle user credentials and session management in a web environment.

---

## 🚀 **Features**

- 🔐 **User Registration**  
  Users can sign up by providing a username, email, and password. Passwords are hashed securely using a hashing algorithm (e.g., `bcrypt` or `SHA256`) before being stored.

- 🔑 **User Login**  
  Registered users can log in with their credentials. Valid credentials grant access to a protected area; invalid credentials show an error.

- 🗃️ **MySQL Database**  
  User data is stored in a structured MySQL database. A sample schema is included (`CDatabase.sql`) for setup.

- 📦 **Session Management**  
  User sessions are managed using Flask’s session system. Logged-in users remain authenticated until they log out or the session expires.

- 🖼️ **Front-End Interface**  
  Basic HTML & CSS provide the UI, while JavaScript handles form validation (e.g., required fields, password strength).

---

## 📂 **Files Overview**

| File/Folder            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `main.py`              | Main Flask application (routing, login, signup, sessions).                 |
| `app_test.py`          | Test cases to verify overall application functionality.                     |
| `unit_test.py`         | Unit tests for individual components or functions.                          |
| `CDatabase.sql`        | SQL script to create the user table and database structure.                 |
| `requirements.txt`     | Lists project dependencies (Flask, MySQL connector, etc.).                  |
| `run`                  | Shell script for launching the app.                                         |
| `static/validate.js`   | JavaScript file for client-side form validation.                            |
| `templates/`           | Contains HTML files (e.g., login, signup, home).                            |

---

## ⚙️ **Design Decisions**

- **Flask**: Chosen for its simplicity and minimal boilerplate, perfect for small-to-medium-sized apps.
- **MySQL**: A reliable and well-supported relational database that pairs well with Flask.
- **Security**: Passwords are hashed (e.g., using `bcrypt`) before storage to prevent exposure during data breaches.
- **Sessions**: Flask's built-in session management keeps users logged in securely.

---

## 🛠️ **Setup Instructions**

1. **Clone the Repository**  
   ```bash
   git clone [Your Repository URL]
   cd [Your Project Folder]
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the MySQL Database**  
   - Make sure MySQL is installed and running.
   - Run the SQL script `CDatabase.sql` in your MySQL environment to create the required tables.

4. **Run the Application**  
   ```bash
   python main.py
   ```
   - The app will run on `http://localhost:5000`.

5. **Open in Browser**  
   - Visit `http://localhost:5000/login` to test user registration and login.

---

## 🌱 **Future Improvements**

- ✅ **Email Verification**: Validate user email addresses during registration.
- 🔁 **Password Reset**: Allow users to reset forgotten passwords via email.
- 🛡️ **User Roles**: Implement roles like *admin* and *user* for role-based access control.
- 🔒 **Two-Factor Authentication**: Add an extra layer of security using 2FA.

---

## 📌 **Final Notes**

This project provides a strong foundation for secure login systems in web applications. It can be easily extended with advanced authentication, admin panels, and integration into larger platforms.

Feel free to contribute or fork this repo for your own custom projects!

