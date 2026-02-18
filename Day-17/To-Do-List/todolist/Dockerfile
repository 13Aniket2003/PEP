# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /app

# 4. Install system dependencies (needed for PostgreSQL & SSL)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy project
COPY . /app/