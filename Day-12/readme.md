## 📅 Day 12 — Django Models, Database Integration, and User Management

Today focused on configuring Django models, creating database tables, handling user input, storing and retrieving records, setting up admin authentication, and understanding the complete Model–View–Template (MVT) workflow.

---

**Keywords Used:**  
Models, Views, Templates, ORM, Database, Business Logic, Display Logic  

**Learning Summary:**
- Models handle database structure and data storage  
- Views manage business logic and user requests  
- Templates display data to users  
- ORM connects Python objects with database tables  

---

### 📦 Django Model Configuration

**Keywords Used:**  
models.py, fields, ORM, database tables  

**Learning Summary:**
- Created models to define database schema  
- Used different field types such as text and email fields  
- Learned how Django automatically converts models into tables  

---

### 🔐 Admin Authentication Setup

**Keywords Used:**  
Admin panel, superuser, authentication, model registration  

**Learning Summary:**
- Enabled Django admin interface  
- Created admin user for database management  
- Registered models to manage entries through admin panel  

---

### 🧾 Database Creation and Migration

**Keywords Used:**  
makemigrations, migrate, sqlmigrate  

**Learning Summary:**
- Generated migration files for models  
- Created database tables  
- Understood Django’s database workflow  

---

### 🧑‍💻 User Input and Database Operations

**Keywords Used:**  
Django shell, ORM queries, CRUD operations  

**Learning Summary:**
- Inserted user data into the database  
- Retrieved records from tables  
- Updated existing entries  
- Performed create, read, update, and delete operations  

---

### 🌐 Views and Templates Integration

**Keywords Used:**  
views.py, templates, rendering, context data  

**Learning Summary:**
- Connected models with views  
- Passed data from views to templates  
- Displayed user records dynamically on web pages  

---

### 🔗 URL Routing for Model Pages

**Keywords Used:**  
urls.py, path, include  

**Learning Summary:**
- Linked application URLs with project URLs  
- Created routes for:
  - Registration page  
  - User list display page  

---

### 📊 Web-Based Data Storage

**Learning Summary:**
- Stored user entries through web forms  
- Viewed and managed records via browser  
- Understood full flow from input to database and display  

---

### 🏗️ Django Model–View–Template (MVT) Architecture

```text
        --------------------------------------------------------------------------------------------
        |                                                                                          |
        |        ORM                     Business Logic                    Display Logic           |
        |     -----------   Datasets     -----------    Data to Display    -------------           |
        |    |  Models   | ---------->  |   Views   | ----------------->  |  Templates  |          |
        |    |-----------| <----------  |-----------| <-----------------  |-------------|          |
        |         |                         |                                   |                  |
        |     Database                User Input                          Web Output               |
        |                                                                                          |
        --------------------------------------------------------------------------------------------
