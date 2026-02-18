import os
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def _dummy_response() -> dict:
    return {
        "match_score": 75,
        "missing_skills": ["(Demo mode) Add OPENAI_API_KEY to enable real scoring"],
        "feedback": "Backend is working. Add your OpenAI key in .env and restart to enable LLM analysis."
    }

def evaluate_resume(resume_text: str, job_description: str) -> dict:
    # 1) No key: return dummy so API never crashes
    if not API_KEY:
        return _dummy_response()

    # 2) Lazy import so server still starts even if openai package has issues
    from openai import OpenAI
    client = OpenAI(api_key=API_KEY)

    prompt = f"""
Return ONLY valid JSON with keys:
- match_score: integer 0-100
- missing_skills: list of strings
- feedback: short paragraph

Resume:
{resume_text}

Job Description:
{job_description}
"""

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        content = resp.choices[0].message.content.strip()

        # 3) Defensive JSON parsing
        return json.loads(content)

    except json.JSONDecodeError:
        # If model returns non-JSON, fall back gracefully
        return {
            "match_score": 0,
            "missing_skills": ["Model returned invalid JSON"],
            "feedback": f"Raw output: {content[:300]}"
        }
    except Exception as e:
        return {
            "match_score": 0,
            "missing_skills": ["API error"],
            "feedback": str(e)
        }


