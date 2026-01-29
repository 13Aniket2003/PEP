## 📅 Day 7 — Django Project Structure, App structure, Templates, Static Files, and Routing

---

### 📁 Project and App Creation
- Created a main folder named django_project  
- Created a Django project named new_project inside it  
- Created a Django app named portfolio  

---

### 📂 Templates and Static Folder Setup
- Created a templates folder inside django_project  
- Added HTML files inside templates:
  - index.html  
  - about.html  
  - contact.html  

- Created a static folder inside django_project  
- Added a CSS file named style.css  

📌 Learned the importance of separating CSS from HTML to improve performance, reduce load on HTML files, and make large projects easier to manage.

---

### 🔗 Connecting Static Files with Templates
- Used Django static loading keyword  
- Linked CSS file with HTML templates using Django static path  

---

### ⚙️ Project Settings Configuration
- Modified project settings to define static file directories  
- Updated template directory path inside settings to recognize custom HTML templates  

---

### 🌐 URL File Creation
- Created urls file for both:
  - Django project  
  - Portfolio app  

---

### 🔗 URL Routing and Page Navigation
- Configured project-level URLs to include app URLs  
- Created routes for multiple pages such as:
  - Home  
  - About  
  - Contact  
  - Service  
  - Projects  
  - Feedback  

- Learned how URL paths allow switching between different pages in browser.

---

### 📄 Views Configuration
- Created views for rendering HTML templates  
- Used HTTP response to display simple text pages  
- Learned the difference between rendering templates and returning responses  

---

### ▶️ Running the Project
- Used migrate keyword to apply database changes  
- Used runserver keyword to start the Django server  
- Accessed project through local host  

---

