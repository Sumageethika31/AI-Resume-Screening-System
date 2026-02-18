from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from services.llm_service import evaluate_resume

app = FastAPI(title="AI Resume Screening API")

class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str

class ResumeResponse(BaseModel):
    match_score: int
    missing_skills: List[str]
    feedback: str

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=ResumeResponse)
def analyze(data: ResumeRequest):
    return evaluate_resume(data.resume_text, data.job_description)

