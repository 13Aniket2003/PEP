## 📅 Day 22 — Dockerized Django Project with Environment Variables and Docker Compose

Today focused on building a **production-ready Django application using Docker**, securing sensitive data using **environment variables**, separating **development and production configurations**, and running Django with **Docker Compose** and **Gunicorn**.

---

## 🐳 Django Project Setup for Docker

### 📁 Project and App Creation
- Created a Django project named **Docker Project**
- Created a Django app named **app**
- Verified project and app structure

---

## 🔐 Why Environment Variables Are Important

**Problem:**
- Secret keys, database passwords, and credentials should **never be hardcoded**
- Exposing them can lead to security breaches

**Solution:**
- Use **environment variables** (`.env` files)
- Load them dynamically inside `settings.py`

---

## ⚙️ Configuring settings.py with Environment Variables

### What was changed:
- **SECRET_KEY** loaded from environment
- **DEBUG** controlled via environment variable
- **ALLOWED_HOSTS** loaded from environment
- **DATABASE configuration** moved completely to environment variables

**Keywords Used:**  
os.getenv, environment variables, secure configuration  

### Result:
- Same codebase works for **development** and **production**
- No sensitive information stored in source code

---

## 📄 Environment Files

### 🧪 `.env` (Development)
Used for local development.

Contains:
- Secret key
- Debug enabled
- Localhost allowed
- Database credentials
- PostgreSQL configuration

---

### 🚀 `.env.production` (Production)
Used for deployment.

Key differences:
- Debug disabled
- Multiple allowed hosts
- Stronger security
- Production database configuration

**Why separate env files are needed:**
- Development needs flexibility
- Production needs security
- Prevents accidental misuse of production secrets

---

## 🗄️ Database Configuration with Docker

**What was done:**
- Removed default SQLite usage
- Configured Django to work with PostgreSQL
- Database credentials provided via environment variables
- Database runs as a **separate Docker service**

**Keywords Used:**  
PostgreSQL, database container, service isolation  

---

## 📦 requirements.txt

Created a requirements file to:
- List all Python dependencies
- Ensure Docker installs exact packages
- Maintain consistency across environments

---

## 🐳 Dockerfile — Multi-Stage Build (Important Concept)

### 🔹 Why Multi-Stage Docker Build?

**Problem with single-stage Dockerfile:**
- Large image size
- Unnecessary build tools included
- Slower deployments

**Solution: Multi-Stage Build**

---

### 🧱 Stage 1 — Builder Stage
Purpose:
- Install Python dependencies
- Prepare environment

Key ideas:
- Lightweight Python image
- Dependency installation
- Faster builds

---

### 🚀 Stage 2 — Production Stage
Purpose:
- Run Django application safely

Key ideas:
- Copy only required files
- Use non-root user (security)
- Optimize Python runtime
- Run application using **Gunicorn**
- Expose application port

**Why Gunicorn is used:**
- Production-grade WSGI server
- Faster and more reliable than Django’s dev server
- Handles multiple requests efficiently

---

## 🧩 What is Docker Compose?

**Docker Compose** allows running **multiple containers together**.

### Why it is needed:
- Django needs:
  - Web server
  - Database
- Compose connects them automatically

**docker-compose.yml handles:**
- Django service
- PostgreSQL service
- Environment variables
- Ports
- Volumes
- Network communication

---

## ▶️ Running the Application with Docker

### Commands Learned (text format):
- Build Docker image: `docker build -t docker_project .`
- Run using Docker Compose: `docker-compose up --build`
- Run in background: `docker-compose up -d`
- Stop containers: `Ctrl + C`

---

## 🌐 Application Access
- Application runs inside Docker containers
- Accessible via browser on configured port
- Django runs successfully with:
  - PostgreSQL
  - Environment variables
  - Production server

---

## 🔁 Development vs Production Comparison

| Feature | Development | Production |
|------|------------|------------|
| Debug | Enabled | Disabled |
| Secrets | Local `.env` | `.env.production` |
| Server | Django dev | Gunicorn |
| Security | Basic | Hardened |
| Database | Docker PostgreSQL | Docker PostgreSQL |

---

## 🎯 Final Outcome

- Secured Django application using environment variables
- Removed hardcoded secrets
- Built Docker image using multi-stage build
- Ran Django with Gunicorn
- Connected Django and PostgreSQL using Docker Compose
- Understood real-world deployment workflow
- Application runs reliably and securely in containers

---

