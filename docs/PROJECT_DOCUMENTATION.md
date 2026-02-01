# Project Documentation  
University Admissions Assistant Chatbot

---

## 1. Introduction

The University Admissions Assistant Chatbot is a conversational web application designed to help students explore university admission information through natural language interaction.

Unlike traditional FAQ-based systems, this chatbot supports multi-turn conversations, remembers context, and dynamically retrieves accurate information from a structured academic knowledge base.

The project focuses on correctness, scalability, and usability rather than rule-heavy or hard-coded responses.

---

## 2. Objectives

The primary objectives of this project are:

- To simplify access to university admission information
- To allow students to interact using natural language
- To avoid rigid, menu-driven chatbot flows
- To ensure all responses are accurate and data-driven
- To design a scalable system that can grow with additional data

---

## 3. System Overview

The system consists of three main layers:

1. Frontend user interface (chat-based web UI)
2. Backend application server (Flask)
3. Academic knowledge base (JSON)

Each layer is decoupled to ensure maintainability and extensibility.

---

## 4. System Architecture

### 4.1 High-Level Architecture

User (Web Browser)

↓

Frontend (HTML, CSS, JavaScript)

↓

Flask Backend (app.py)

↓

Chatbot Logic (chatbot.py)

↓

Structured Academic Data (JSON)


---

### 4.2 Data Flow

1. User enters a message in the chat interface
2. Message is sent to the backend using a POST request
3. Chatbot logic:
   - Detects user intent
   - Resolves program and school context
   - Retrieves relevant data from JSON
4. Response is formatted and returned to the frontend
5. Frontend renders the response in the chat interface

---

## 5. Knowledge Base Design

### 5.1 Data Format

The academic information is stored in a structured JSON format with the following hierarchy:

- School (e.g., Engineering, Architecture)
  - Programs (e.g., B.Tech, B.Arch)
    - Attributes:
      - Name
      - Duration
      - Eligibility
      - Fees
      - Specializations (if applicable)
      - Entrance Exams (if applicable)
      - Career Scope (if applicable)

### 5.2 Design Rationale

- JSON was chosen for simplicity and readability
- Enables easy modification without changing application logic
- Prevents data duplication
- Ensures a single source of truth

---

## 6. Chatbot Logic Design

### 6.1 Intent Detection

User intent is detected using keyword-based matching for intents such as:

- Fees
- Eligibility
- Duration
- Career scope
- Specializations
- Entrance exams

The intent detection logic is intentionally simple and transparent to ensure predictability and correctness.

---

### 6.2 Context Management

The chatbot retains conversational context using in-memory variables:

- Last selected school
- Last selected program

This allows the chatbot to handle follow-up questions such as:

- "fees?"
- "eligibility?"
- "career scope?"

without requiring the user to repeat program names.

---

### 6.3 Alias Handling

The chatbot supports aliases and abbreviations such as:

- "arch" → Architecture
- "btech" → Bachelor of Technology
- "mba" → Master of Business Administration

This improves usability and mirrors how students naturally type queries.

---

## 7. Frontend Design

### 7.1 User Interface

- Chat-style interface with message bubbles
- Clear visual distinction between user and bot messages
- Typing indicator for realistic interaction
- Keyboard and button-based message submission

---

### 7.2 Responsiveness

The UI is fully responsive and adapts to:

- Mobile devices
- Tablets
- Laptops
- Large displays

Responsive design is implemented using CSS media queries.

---

## 8. Technology Stack

| Component | Technology |
|---------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Data Storage | JSON |
| Version Control | Git, GitHub |

---

## 9. Installation and Execution

### 9.1 Prerequisites

- Python 3.10 or above
- Flask
- Web browser

---

### 9.2 Setup Steps

```bash
git clone https://github.com/itsrajarshi/university-admissions-bot.git
cd university-admissions-bot
pip install flask
python app.py
```
Access the application at:
http://127.0.0.1:5000

## 10. Limitations
The chatbot responds only to information available in the knowledge base

No authentication or user personalization

Context is session-based and resets on refresh

No persistent storage for chat history

## 11. Scalability and Extensibility
The project is designed to be easily extensible:

New programs can be added by updating the JSON file

Additional fields such as scholarships or deadlines can be introduced without modifying chatbot logic

The architecture supports future integration with NLP libraries or databases

## 12. Future Enhancements
Potential future improvements include:

Voice-based interaction

Cloud deployment

Admission deadline reminders

Advanced NLP-based intent detection

Analytics for commonly asked queries

## 13. Conclusion
The University Admissions Assistant Chatbot demonstrates how a simple, data-driven architecture can deliver an effective conversational experience.

By prioritizing correctness, usability, and extensibility, the project provides a strong foundation for real-world academic information systems.

## 14. Author
Rajarshi Ghosh
B.Tech – Computer Science and Engineering

GitHub: https://github.com/itsrajarshi

LinkedIn: https://linkedin.com/in/itsrajarshia