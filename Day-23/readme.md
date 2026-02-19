## 📅 Day 23 — Introduction to NLP and Docker-Based NLP Execution

Today was a light session due to exams. The learning focus was on **Natural Language Processing (NLP)** and understanding how NLP tasks can be executed both **locally in Python** and inside **Docker containers**. Practical work was done on Sentiment Analysis, Text Classification, and Text Summarization.

---

## 🧠 What is NLP (Natural Language Processing)?

**Natural Language Processing (NLP)** is a branch of Artificial Intelligence that enables computers to understand, interpret, and generate human language.

NLP is widely used in:
- Chatbots
- Search engines
- Recommendation systems
- Email filtering
- Voice assistants

---

## 🔍 Core NLP Tasks Learned Today

### 😊 Sentiment Analysis
- Determines the emotional tone of text
- Classifies text as **positive**, **negative**, or **neutral**
- Commonly used in:
  - Product reviews
  - Social media analysis
  - Feedback systems

---

### 🏷️ Text Classification
- Assigns predefined categories to text
- Examples:
  - Spam vs non-spam emails
  - Topic classification
  - News categorization

---

### 📝 Text Summarization
- Generates a shorter version of long text
- Preserves the main meaning and key points
- Used in:
  - News summarization
  - Document analysis
  - Research assistance

---

### 🌍 Language Translation (Conceptual)
- Converts text from one language to another
- Uses NLP models trained on multilingual data
- Example: English → Hindi

*(Note: Translation was discussed conceptually but not implemented today)*

---

## 🐳 What is Docker NLP?

**Docker NLP** means running NLP applications inside **Docker containers** instead of running them directly on the local system.

### Why Docker is used for NLP:
- NLP libraries are heavy and dependency-intensive
- Docker ensures:
  - Same environment everywhere
  - No dependency conflicts
  - Easy sharing and deployment
- Models run the same on any machine

---

## 🔗 GitHub Repository Usage
- Sir provided a GitHub repository containing NLP code
- Repository was cloned into VS Code
- Project structure and files were explored before execution

---

## ⚙️ Step-by-Step Workflow Followed Today

### 1️⃣ Running NLP Locally (Normal Python)
- Ran Sentiment Analysis using normal Python
- Tested sentences with:
  - Positive sentiment
  - Negative sentiment
  - Neutral sentiment
- Verified output correctness

---

### 2️⃣ Containerizing Sentiment Analysis with Docker
- Created a Dockerfile specifically for Sentiment Analysis
- Used a lightweight Python base image
- Installed required NLP dependencies
- Copied sentiment analysis code into container
- Defined execution flow inside Docker

---

### 3️⃣ Building and Running Docker Image
- Built Docker image from Dockerfile
- Ran the container
- Verified that Sentiment Analysis runs correctly inside Docker

---

### 4️⃣ Repeating Same Process for Other NLP Tasks
The same workflow was followed for:
- Text Classification
- Text Summarization

Each task was:
- First tested locally in Python
- Then containerized using Docker
- Built and executed as a Docker image

---

## 🔁 Key Learning Comparison

| Aspect | Local Python | Docker |
|------|-------------|--------|
| Environment | System-dependent | Isolated |
| Dependencies | Manual install | Container-managed |
| Portability | Low | High |
| Reproducibility | Medium | Very High |

---

## 🎯 Final Outcome

- Understood basics of NLP and its applications
- Practiced Sentiment Analysis, Text Classification, and Summarization
- Learned how to run NLP tasks locally
- Learned how to containerize NLP applications using Docker
- Verified NLP execution inside Docker containers
- Built foundation for scalable AI/NLP deployment

---

