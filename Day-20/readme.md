## 📅 Day 20 — Django REST Framework (DRF), APIs, Serialization, and Assignments

Today focused on learning the **Django REST Framework (DRF)**, understanding REST architecture, working with APIs, serialization and deserialization, testing APIs using Thunder Client, and completing multiple practical assignments related to REST APIs and email functionality.

---

## 🌐 What is REST?

**REST (Representational State Transfer)** is an architectural style used to build scalable and flexible web services.

**Key Characteristics of REST:**
- Uses standard HTTP methods (GET, POST, PUT, DELETE)
- Stateless communication between client and server
- Data is usually exchanged in JSON or XML format
- Resources are accessed via URLs (endpoints)

---

## ❓ Why We Use REST Framework in Django

**Django REST Framework (DRF)** is used to build Web APIs easily and efficiently.

**Why DRF is important:**
- Converts Django applications into API-based systems
- Allows frontend (React, Angular, mobile apps) to communicate with backend
- Provides serializers, authentication, permissions, and validations
- Makes data exchange platform-independent

---

## 🔄 Serialization and Deserialization

### 🔹 Serialization
- Converts complex data types (Django models, QuerySets) into JSON or XML
- Used when sending data from server to client

### 🔹 Deserialization
- Converts JSON or XML data back into complex data types (Django models)
- Used when receiving data from client to server

This process enables APIs to communicate cleanly between different systems.

---

## 🆕 REST Project Setup

### 📁 Project and App Creation
- Created a new Django project named **REST**
- Created a Django app named **app**
- Added **rest_framework** inside **INSTALLED_APPS**
- Registered models in admin panel
- Included app URLs in project URLs

---

## 📦 Model and API Setup

**Learning Summary:**
- Created a model with fields:
  - Title
  - Author
  - Publish Date
- Used serializers to convert model data into JSON
- Created API views to return JSON responses
- Verified API output in browser

---

## 🧪 API Testing Tool

**Tool Used:**  
Thunder Client (VS Code Extension)

**Purpose:**
- Send GET and POST requests
- Test APIs without building a UI
- Verify JSON responses and database updates

---

## 📘 Assignments Overview

Sir provided **multiple assignments** to practice Django REST Framework concepts.

---

## ✅ Assignment 1 — Student List API (GET Request)

**Goal:**  
Create a REST API to return all student records in JSON format.

**What Was Done:**
- Created Student model with:
  - Name
  - Age
  - Course
- Created API endpoint to fetch all students
- Returned student list as JSON

**Expected Output:**
- Visiting `/app/student/` returns student list in JSON

---

## ✅ Assignment 2 — Create Student via API (POST Request)

**Goal:**  
Add new student data using API without UI.

**What Was Done:**
- Created API endpoint to accept POST requests
- Used Thunder Client to send JSON payload
- Added student data directly through API

**Expected Output:**
- New student added via API
- Database updated successfully

---

## ✅ Assignment 3 — Model Serializer for Student API

**Goal:**  
Convert Django model objects into structured JSON.

**What Was Done:**
- Created StudentSerializer using ModelSerializer
- Used serializer in API views
- Returned clean JSON response

**Expected Output:**
- Properly structured JSON output using serializer

---

## ✅ Assignment 4 — Validation in Serializer

**Goal:**  
Apply validation rules inside serializer.

**Validation Rule:**
- Student age must be greater than 5

**What Was Done:**
- Added field-level validation inside serializer
- Tested invalid data using POST request in Thunder Client
- Received proper error response for invalid age

**Concept Learned:**
- Using `validate_<fieldname>` validates a single field
- DRF automatically passes the field value for validation
- Validation errors are returned as JSON responses

---

## ✅ Assignment 5 — Welcome Email on User Registration

**Goal:**  
Send an email after successful user registration.

**What Was Done:**
- Configured SMTP email settings
- Created registration form (name, email)
- Stored user data in database
- Sent welcome email after successful registration

**Expected Output:**
- User registered successfully
- Email delivered to registered email address

---

## ✅ Assignment 6 — Contact Us Form with Email Notification

**Goal:**  
Send an email to admin when a user submits a query.

**What Was Done:**
- Created Contact model (name, email, message)
- Built form and template
- Stored user query in database
- Sent email notification to admin
- Displayed success message to user

**Expected Output:**
- Admin receives query email
- Query stored in database

---

## 🎯 Final Outcome

- Learned REST architecture and DRF fundamentals
- Built and tested multiple REST APIs
- Used serializers for JSON conversion
- Applied validation logic in serializers
- Used Thunder Client for API testing
- Implemented email functionality with Django
- Completed all assignments successfully

---
