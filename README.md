
# AI Resume Screening System

An AI-powered application that evaluates resumes against job descriptions and provides structured analysis including match score, missing skills, and improvement feedback.

---

## Demo Overview
This system simulates how modern ATS and AI recruiters analyze resumes.

---

## Features
- Resume vs Job Description comparison
- Match score (0–100)
- Skill gap detection
- AI feedback generation
- Interactive UI dashboard
- REST API backend

---

## Architecture

User → Streamlit UI → FastAPI → AI Model → JSON Result

---

## Tech Stack
Python • FastAPI • Streamlit • OpenAI API • Pandas

---

## How To Run

### Start Backend
```
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

### Start UI
```
streamlit run ui.py
```

---

## Example Output
Match Score: 82  
Missing Skills: Docker, AWS  
Feedback: Strong backend profile but lacks cloud deployment experience.

---

## Use Cases
- Recruiters screening candidates
- Students improving resumes
- HR automation tools
- AI portfolio demonstration

---

## Future Improvements
- PDF resume upload
- Skill highlighting visualization
- Resume improvement suggestions
- Cloud deployment

---

## Author
Suma Geethika
