## 📅 Day 6 — Advanced Python, Dataclasses, OOP Concepts, and Django Architecture


---

### 🔤 String Analysis Problem
- Given a company name in lowercase letters, identified the top three most common characters  
- Displayed each character with its occurrence count  
- Sorted results in descending order of frequency  
- Applied alphabetical order when counts were the same  

---

### 📦 Python Dataclass Decorator
- Learned about the `@dataclass` feature for creating data-focused classes  
- Understood how it simplifies class creation by auto-generating special methods  

Automatically generated methods include:
- `__init__()` for initializing objects  
- `__repr__()` for readable object representation  
- `__eq__()` for comparing objects  

---

### ❄️ Frozen Dataclasses
- Learned how the `frozen` argument makes dataclass objects immutable  
- Understood that modifying frozen objects raises an error  

---

### 🧬 Advanced Dataclass Concepts
- Dataclass inheritance  
- Nested dataclasses  

---

### 🎓 Student Performance Mapping (OOP Practice)
- Created a Student class with personal details  
- Created a Marks class storing semester results  
- Created an Interview Score class storing:
  - Interview score  
  - Resume score  
  - Technical score  
  - Knowledge score  
- Mapped end-semester marks with interview performance  
- Compared marks to determine:
  - Pass if marks greater than 70  
  - Fail if below 70  
  - Absent if marks equal to 0  

---

### 🏗️ Object-Oriented Programming Concepts
- Inheritance  
- Class variables and class methods  
- Access specifiers:
  - Public  
  - Protected  
  - Private  

---

### ✔️ Assert Statement
- Learned how `assert` is used to validate logical expressions  
- Program continues if condition is true  
- Raises `AssertionError` when condition is false  

---

### 🌐 Introduction to Django Framework
- Understood Django’s “batteries included” approach  
- Learned about built-in features such as:
  - User authentication  
  - Routing and views  
  - Templates  
  - Admin interface  
  - Strong security features  
- Learned about Django’s default database (SQLite3) and support for multiple databases  
- Explored Django’s focus on speed, security, and rapid development  

---

### 🏛️ Django MTV Architecture

#### 📊 Model (Data Layer)
- Handles data access, validation, and relationships  
- Uses Python classes connected through Django ORM  

#### 🎨 Template (Presentation Layer)
- Manages how data is displayed to users  

#### 🔧 View (Business Logic Layer)
- Acts as a bridge between Models and Templates  
- Retrieves data and sends it for presentation  

---

### 🔗 Django ORM (Object Relational Mapping)
- Provides a connection between:
  - Database tables  
  - Python objects  
- Allows interaction with databases using Python instead of SQL  

---

### 🏛️ Django MTV Architecture

```text

       ----------------------------------------------------------------------  
       |       Model --------------------------------------> Template       |
       |   (object,relational,mapping,orm)                  (display,logic) |
       |       ^                                                    |       |
       |       |   (create,update,delete)                           |       |
       |       |                                 View               |       |
       |       |--------------------------- business,logic <--------|       |
       ----------------------------------------------------------------------

       ----------------------------------------------
       |               ---------->  SQL             |
       |               |                            |
       |           Databases                        |
       |               |                            |
       |               ------------> Django ORM     |
       ----------------------------------------------

---