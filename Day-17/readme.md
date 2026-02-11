## 📅 Day 17 — Django To-Do List Project with PostgreSQL Integration

Today focused on building a complete To-Do List application using Django, including project and app setup, model design, view logic, URL routing, PostgreSQL integration, and implementing CRUD operations with multi-level task management.

---

### 📁 Project and App Setup
- Created a new Django project named **To-Do List**
- Created a Django app named **To-Do**
- Created a templates directory inside the project to store HTML pages
- Linked templates with the project configuration

---

### 🗄️ Database Configuration
- Removed the default SQLite database
- Integrated **PostgreSQL** as the database backend
- Configured PostgreSQL settings in the project configuration
- Verified database connectivity before running the project

---

### 📦 Model Design for To-Do Application

**Keywords Used:**  
models.py, ORM, relational models, ForeignKey  

**Learning Summary:**
- Created models to represent:
  - To-Do Lists (main categories)
  - To-Do Items (tasks under each list)
- Established relationships where:
  - One To-Do List contains multiple To-Do Items
- Understood hierarchical data modeling in Django

---

### 🏠 Home View (To-Do List Overview)

**Keywords Used:**  
views.py, request handling, rendering  

**Learning Summary:**
- Created a Home view to display all To-Do Lists
- Allowed users to add new To-Do Lists (e.g., Coding, Testing, Debugging)
- Displayed lists dynamically on the homepage
- Handled user input and request data safely

---

### 📄 To-Do Details View (Task Management)

**Keywords Used:**  
detail view, CRUD operations, error handling  

**Learning Summary:**
- Redirected users to a detail page when clicking a To-Do List
- Displayed all tasks related to the selected list
- Enabled users to:
  - Add new tasks
  - Update existing tasks
  - Rename tasks
  - Delete tasks
- Implemented proper error handling for invalid requests

---

### 🔁 Navigation and Page Flow
- Clicking a To-Do List redirects to its task page
- Tasks are managed independently under each list
- Ensured smooth page redirection between:
  - Home page
  - To-Do details page

---

### 🌐 URL Configuration

**Keywords Used:**  
urls.py, include, path  

**Learning Summary:**
- Included app URLs in the project URL configuration
- Defined URL paths for:
  - Home view
  - To-Do details view
- Linked views properly to enable navigation

---

### ▶️ Execution and Testing

**Learning Summary:**
- Applied migrations for PostgreSQL-backed models
- Ran the Django server successfully
- Tested:
  - Adding To-Do Lists
  - Viewing tasks
  - Adding, updating, and deleting tasks
- Verified complete To-Do List workflow

---

### ✅ Final Outcome
- Built a fully functional To-Do List application
- Implemented multi-level task management
- Integrated PostgreSQL database
- Enabled complete CRUD operations
- Achieved smooth user navigation and data handling

---

