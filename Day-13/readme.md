## 📅 Day 13 — Django Forms, User Input Handling, and Database Updates

Today focused on taking user input directly from web forms, updating the database without using Python shell, working with Django forms, models, admin integration, GET and POST methods, and handling migration issues.

---

### 📝 Creating Django Forms for User Input

Keywords Used:  
forms.py, Django Forms, CharField, IntegerField, PasswordInput  

Learning Summary:
- Created a form file inside the app to take user input  
- Designed input fields for:
  - First name  
  - Last name  
  - Roll number  
  - Password  
- Learned how Django forms simplify input handling and validation  

---

### 📦 Creating Models for Storing Form Data

Keywords Used:  
models.py, database models, fields, ORM  

Learning Summary:
- Created a user model to store personal information  
- Created another model to store form-related data  
- Learned how models represent database tables in Django  

---

### 🔐 Registering Models in Admin Panel

Keywords Used:  
admin.py, model registration, admin interface  

Learning Summary:
- Registered all models in admin panel  
- Enabled viewing and managing database entries through admin dashboard  

---

### 🌐 Rendering Forms in Views

Keywords Used:  
views.py, render(), context data  

Learning Summary:
- Displayed forms on web pages using views  
- Passed form objects to templates  
- Connected backend forms with frontend HTML pages  

---

### 🔗 URL Configuration for Forms

Keywords Used:  
urls.py, path routing  

Learning Summary:
- Created URL routes to access form pages  
- Connected form views with browser URLs  

---

### 📥 Handling User Input with GET and POST Methods

Keywords Used:  
GET method, POST method, request handling  

Learning Summary:
- Learned how GET method captures data from URL parameters  
- Learned how POST method securely sends form data  
- Extracted user input from request objects  

---

### 💾 Saving User Data to Database Without Python Shell

Keywords Used:  
ORM save(), database entry, backend storage  

Learning Summary:
- Stored form input directly into database models  
- Updated database records using backend logic  
- Removed dependency on Python shell for data operations  

---

### 📄 Templates Integration

Learning Summary:
- Created required HTML templates for forms and display pages  
- Linked templates with views and models  
- Displayed input forms and stored data on web pages  

---

### 🧾 Database Migration Handling

Keywords Used:  
makemigrations, migrate, migration files  

Learning Summary:
- Applied migrations after model changes  
- Learned how migration files track database updates  
- Understood how to fix migration errors by cleaning migration files and re-migrating specific apps  

---

### ▶️ Running the Updated Project

Learning Summary:
- Migrated database changes properly  
- Restarted server after updates  
- Verified form submission and database updates through browser  

---
