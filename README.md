# AI Resume Screening System

An AI-powered resume analysis web application that compares a resume against a job description and returns an intelligent evaluation including:

- Match score (0–100)
- Missing skills
- Feedback summary
- Readability insights

This project demonstrates full-stack AI engineering using FastAPI, Streamlit, and LLM APIs.

---

## Project Overview

Hiring teams manually screen resumes against job descriptions. This project automates that process using natural language processing and AI evaluation logic to provide structured candidate insights.

The system works by:
1. Accepting resume text and job description input
2. Sending both to an AI evaluation service
3. Parsing structured results
4. Displaying them in a clean UI dashboard

---

## Key Features

- Real-time resume analysis
- AI match scoring
- Skill gap detection
- Structured JSON API output
- Interactive web interface
- Automated backend startup script
- Environment-isolated dependency management

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### AI Layer
- OpenAI API

### Language
- Python 3

---

## System Architecture

```
User Input → Streamlit UI → FastAPI API → LLM Service → JSON Response → UI Display
```

---

## Project Structure

```
AI-Resume-Screening-System/
│
├── app.py                 # FastAPI backend
├── ui.py                  # Streamlit frontend
├── run.sh                 # one-command launcher
├── requirements.txt       # dependencies
├── README.md
│
└── services/
      └── llm_service.py   # AI logic
```

---

## Installation Guide

### 1. Clone Repository

```
git clone (https://github.com/Sumageethika31/AI-Resume-Screening-System.git)
cd AI-Resume-Screening-System
```

---

### 2. Create Virtual Environment

Mac/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Run Application

### Recommended (one command)

```
./run.sh
```

Automatically launches:
- Backend server
- UI server
- Browser window

---

### Manual Run (Alternative)

Backend:
```
python -m uvicorn app:app --reload
```

Frontend:
```
streamlit run ui.py
```

Open:
```
http://127.0.0.1:8501
```

---

## API Documentation

### Endpoint
```
POST /analyze
```

### Request Body
```json
{
  "resume_text": "string",
  "job_description": "string"
}
```

### Response
```json
{
  "match_score": 82,
  "missing_skills": ["Docker", "AWS"],
  "feedback": "Strong backend skills but lacks cloud exposure."
}
```

---

## Example Use Case

Input Resume:
```
Python developer with FastAPI and SQL experience
```

Job Description:
```
Looking for backend engineer with Python, FastAPI, SQL, and AWS
```

Output:
```
Score: 75
Missing Skills: AWS
Feedback: Strong backend profile but lacks cloud experience.
```

---

## Development Workflow

Run locally:

```
./run.sh
```

Modify code → Save → Auto reload triggers

---

## Troubleshooting

If port already in use:

```
kill -9 $(lsof -ti :8000)
kill -9 $(lsof -ti :8501)
```

---

## Security Notes

- Never commit `.env`
- Store API keys securely
- Use environment variables

---

## Future Enhancements

Planned improvements:

- Resume PDF upload
- Multi-job comparison
- Skill charts visualization
- Candidate ranking system
- Authentication dashboard
- Recruiter analytics panel

---

## Performance Considerations

- Async backend support
- Structured JSON parsing
- Lightweight frontend
- Background process handling

---

## Why This Project Is Valuable

This repository demonstrates real-world engineering capabilities:

- Backend API design
- Frontend UI development
- AI integration
- Prompt engineering
- Debugging complex environments
- Production-ready architecture

These are core skills required for:

- AI Engineer roles
- Data Scientist roles
- Backend Engineer roles
- Full-Stack Developer roles

---

## Author

Suma Geethika Puvvula


