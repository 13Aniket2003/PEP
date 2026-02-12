## 📅 Day 18 — Authentication Extension in To-Do Project and Slug Project Setup

Today focused on extending the existing To-Do List project by adding authentication (signup & login), and starting a new Django project to understand the concept of Slugs and URL handling using Django models.

---

## 🔐 Extending To-Do List Project with Authentication

Today’s first task was to enhance the previously built To-Do List project by adding authentication flow.

### 🔄 Authentication Flow

Keywords Used:  
Signup, Login, Redirect, Authentication Flow  

Learning Summary:
- Made **Signup page** as the default landing page
- After successful signup, user is redirected to **Login page**
- After successful login, user is redirected to **To-Do List home page**
- Only authenticated users can:
  - View To-Do Lists
  - Add tasks
  - Update tasks
  - Delete tasks  

---

### 🧠 Application Flow (Conceptual)
- Default page → Signup  
- Signup success → Login  
- Login success → To-Do List (Home)   

---

## 🆕 New Django Project: Slug

After extending the To-Do project, a new Django project named **Slug** was created to understand URL handling and slug-related concepts.

### 📁 Project and App Setup
- Created a new Django project named **Slug**
- Created a new app named **Slug app**
- Added the app inside **INSTALLED_APPS**
- Modified the database configuration
- Verified app configuration and initialization

---

### 🧩 What is a Slug? (Concept Understanding)

A **Slug** is a URL-friendly string used to identify a resource in a readable way.

Example:
- Article Title: *Django Models Explained*
- Slug: `django-models-explained`

Why slugs are used:
- Creates clean and readable URLs
- Improves SEO
- Avoids exposing raw database IDs  

⚠️ **Note:**  
In this project, slug is **not yet implemented**. Currently, URLs are generated using **article ID**, not slug.

---

### 📦 Article Model Creation

Keywords Used:  
models.py, Article model, CharField, TextField  

Learning Summary:
- Created an **Article** model
- Stored article data using:
  - Title
  - Body
- Implemented string representation to display article title in admin panel

---

### 🔗 URL Generation Using Model Method

Keywords Used:  
get_absolute_url, reverse, ID-based routing  

Learning Summary:
- Implemented `get_absolute_url()` inside the model
- Used Django’s `reverse()` function to generate URLs
- Article detail pages are currently identified using **article ID**
- Prepared the foundation for future slug-based URLs

---

### 🔐 Admin Panel Integration

Keywords Used:  
admin.py, model registration  

Learning Summary:
- Registered the Article model in Django admin
- Verified that articles appear in admin panel
- Confirmed that model entries can be created and managed

---

### 📄 Templates Setup

Keywords Used:  
templates, home.html  

Learning Summary:
- Created a `home.html` template
- Template is currently **not linked with any view**
- Prepared frontend structure for future rendering

---

### ▶️ Current Status

Learning Summary:
- To-Do project successfully extended with authentication
- Slug project and app created successfully
- Database configuration updated
- Article model created and registered
- URL generation using ID implemented
- Template created but pending linkage

---

