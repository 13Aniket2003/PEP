## 📅 Day 14 — Multiple Django Models, Interconnection, and Authentication System

Today focused on creating multiple models, connecting them together, handling user input through views, building login and signup systems, and managing authentication with database integration.

---

### 📦 Creating and Connecting Multiple Models

Keywords Used:  
models.py, multiple models, ORM, database relationships  

Learning Summary:
- Created separate models for:
  - Form data storage (title and description)  
  - User login information  
  - User signup information  

- Learned how multiple models can work together inside one application  
- Stored different types of data in separate tables while keeping them connected  

---

### 📝 Form Model for Backend Storage

Keywords Used:  
FormModel, database entry, backend storage  

Learning Summary:
- Created a model to store form inputs such as title and description  
- Connected form submission from frontend to backend database  
- Rendered form page and saved input directly in database  

---

### 🔐 Login System Implementation

Keywords Used:  
login view, authentication, password hashing, redirect, messages  

Learning Summary:
- Created a login page for user authentication  
- Verified user credentials by comparing with database records  
- Used password hashing for security  
- Redirected users to home page after successful login  
- Displayed success and error messages  

---

### 📝 Signup System Implementation

Keywords Used:  
signup view, user creation, authentication flow, password encryption  

Learning Summary:
- Created signup page for new users  
- Stored user details in database  
- Checked for duplicate usernames and emails  
- Redirected users to login page after successful signup  

---

### 🔄 Interconnection Between Signup and Login Models

Keywords Used:  
model synchronization, data linking, auto creation  

Learning Summary:
- Connected signup model with login model  
- Automatically created login records when new user signed up  
- Ensured authentication data stayed updated across models  

---

### 🌐 URL Routing for All Views

Keywords Used:  
urls.py, path routing, view mapping  

Learning Summary:
- Created URL paths for:
  - Home page  
  - Registration page  
  - Form page  
  - Login page  
  - Signup page  

- Linked all views properly for navigation  

---

### 🔐 Admin Panel Model Management

Keywords Used:  
admin.py, model registration, admin dashboard  

Learning Summary:
- Registered all models in Django admin panel  
- Managed user data, form data, and authentication data from admin interface  

---

### 📄 Templates Integration

Learning Summary:
- Created HTML pages for:
  - Signup  
  - Login  
  - Home  
  - Forms  

- Linked templates with views and URL paths  
- Enabled page redirection and navigation  

---

### ▶️ Running and Testing the System

Learning Summary:
- Applied migrations for new models  
- Created database tables  
- Ran the server  
- Tested signup, login, form submission, and redirection  

---
