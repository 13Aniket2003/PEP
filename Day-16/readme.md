## 📅 Day 16 — PostgreSQL Integration with Django and Database Inspection

Today focused on integrating PostgreSQL with Django by replacing the default SQLite database, configuring project and app settings, creating relational models, managing data through the admin panel, and exploring the database using PostgreSQL CLI and DBeaver.

---

### 🛠️ Database Tools Installation
- Installed PostgreSQL as the database server  
- Installed DBeaver as a graphical database management tool  

---

### 📁 Project and App Setup
- Created a new folder named **DB integration**  
- Created a Django project named **DB demo**  
- Created a Django app named **app**  
- Added the app inside **INSTALLED_APPS**  
- Verified app configuration through **apps.py**  

---

### 🗄️ PostgreSQL Database Configuration in Django

**Keywords Used:**  
settings.py, DATABASES, PostgreSQL backend, psycopg2  

**Learning Summary:**
- Commented out the default SQLite database configuration  
- Configured PostgreSQL as the default database backend  
- Defined database credentials such as database name, user, password, host, and port  
- Learned how Django connects Python applications with PostgreSQL  

---

### ⚙️ Default Auto Field Configuration

**Keywords Used:**  
default_auto_field, BigAutoField  

**Learning Summary:**
- Configured the default auto field type for primary keys  
- Ensured consistency across all models  

---

### 📦 Creating Models with Relationships

**Keywords Used:**  
models.py, ORM, ForeignKey, relational mapping  

**Learning Summary:**
- Created a **student** model to store academic information  
- Created an **info** model to store personal details  
- Linked models using a foreign key relationship  
- Understood how Django ORM maps relationships to database tables  

---

### 🔐 Admin Panel Integration

**Keywords Used:**  
admin.py, model registration, admin authentication  

**Learning Summary:**
- Registered all models in the Django admin panel  
- Created a new superuser after PostgreSQL integration  
- Logged into the admin panel using new credentials  
- Verified that all tables were created and initially empty  

---

### ▶️ Migration and Server Execution

**Keywords Used:**  
makemigrations, migrate, runserver  

**Learning Summary:**
- Generated migration files for PostgreSQL-backed models  
- Created database tables successfully  
- Ran the Django server  
- Accessed the admin panel on localhost  

---

### 💻 PostgreSQL Command-Line Interface (psql)

**Keywords / Commands Used:**  
psql -U postgres, \\h, \\l, \\dt  

**Learning Summary:**
- Logged into PostgreSQL using the postgres user  
- Used help command to explore available PostgreSQL operations  
- Listed all available databases  
- Viewed tables created by Django models  
- Verified that student and info tables existed  

---

### 🗂️ Database Exploration Using DBeaver

**Keywords Used:**  
DBeaver, PostgreSQL connection, schema, tables, foreign key  

**Learning Summary:**
- Connected DBeaver with PostgreSQL database  
- Explored database schemas and tables visually  
- Verified that Django-created tables were present  
- Confirmed foreign key relationship between student and info tables  

---

### ✅ End-to-End Verification

**Learning Summary:**
- Verified PostgreSQL integration through:
  - Django Admin Panel  
  - PostgreSQL CLI  
  - DBeaver GUI  

- Confirmed that:
  - Database connection was successful  
  - Tables were created correctly  
  - Relationships were properly mapped  

---

