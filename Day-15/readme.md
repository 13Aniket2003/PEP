## 📅 Day 15 — Jinja2 Template Engine Integration with Django

Today focused on using Jinja2 templates in Django, understanding differences between Jinja2 and Django templates, creating a separate Jinja template engine, configuring project settings, and rendering dynamic user-specific content.

---

### 📁 Project and App Setup
- Created a new Django project named **jinja**
- Created a Django app named **demoapp**
- Designed templates inside the project-level folder (not inside the project package)
- Configured project settings and URLs to connect the app correctly

---

### 🎨 Working with Jinja2 Templates
- Designed a simple profile page using **Jinja2 template syntax**
- Used **.jinja** file extension for Jinja templates
- Created another template using **.html** extension for Django templates
- Learned how Django can support multiple template formats in one project

---

### 🔍 Difference Between Jinja2 Templates and Django Templates

Key differences learned:
- Jinja2 is faster and more flexible than Django’s default template engine  
- Jinja2 syntax is closer to Python and more expressive  
- Django templates are more restrictive for security reasons  
- Jinja2 is framework-independent and also used in Flask  
- Django templates are tightly coupled with Django’s ecosystem  

---

### ⚙️ Template Directory and App Configuration
- Added template directories under the **DIRS** section in project settings
- Registered **demoapp** inside **INSTALLED_APPS**
- Included demoapp URLs inside the project URL configuration to render templates

---

### 🧠 Creating a Separate Jinja2 Template Engine

**Keywords Used:**  
Template Engine, Jinja2 Backend, DjangoTemplates Backend  

**Learning Summary:**
- Created a **separate template engine specifically for Jinja2**
- Added it below the default Django template engine in project settings
- Configured the Jinja engine to recognize `.jinja` template files

**Why a separate Jinja template engine is required:**
- Django’s default template engine cannot fully support Jinja2 syntax  
- Separating engines avoids syntax conflicts between Django templates and Jinja templates  
- Allows Django and Jinja templates to work independently in the same project  

---

### 👤 Dynamic User Content in Jinja Templates
- Used variable placeholders in Jinja templates to display user-specific data
- Learned that Jinja replaces placeholders with actual values at runtime
- Enabled personalized content display for different users

---

### 🔁 Passing Data from Views to Jinja Templates

**Keywords Used:**  
views.py, context dictionary, render function  

**Learning Summary:**
- Passed data from views to templates using a context dictionary
- Understood that context is required to send dynamic values to templates
- Used this approach to display a user’s name dynamically on the page

---

### 🌐 URL Routing and Page Rendering
- Configured app-level URLs to render Jinja templates
- Included app URLs in project-level URLs
- Verified navigation and page rendering through browser

---

### ▶️ Migration and Execution
- Applied migrations successfully
- Ran the server after full configuration
- Verified that both Jinja and Django templates rendered correctly
- Toggled pages and confirmed dynamic content worked as expected

---
