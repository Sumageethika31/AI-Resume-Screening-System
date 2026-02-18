import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="🧠",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000"

st.markdown("""
<style>
.block-container { padding-top: 2rem; max-width: 900px; }
h1 { margin-bottom: 0.25rem; }
.small-muted { color: #6b7280; font-size: 0.95rem; }
</style>
""", unsafe_allow_html=True)

st.title("AI Resume Screening Project")
st.markdown(
    '<div class="small-muted">Paste a resume and job description to get a match score, missing skills, and feedback.</div>',
    unsafe_allow_html=True
)
st.write("")

def backend_ok() -> bool:
    try:
        r = requests.get(f"{API_URL}/", timeout=3)
        return r.status_code == 200
    except Exception:
        return False

# Backend status
if backend_ok():
    st.success("Backend is running ✅")
else:
    st.error(
        "Backend is not reachable. Start FastAPI in another terminal:\n"
        "`python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000`"
    )
    st.stop()

# Clear button
if st.button("Clear inputs"):
    st.session_state["resume_text"] = ""
    st.session_state["job_description"] = ""

# Inputs (open by default)
with st.expander("Paste Resume + Job Description", expanded=True):
    resume_text = st.text_area(
        "Paste Resume Text",
        height=180,
        placeholder="Paste your resume content here...",
        key="resume_text"
    )
    job_description = st.text_area(
        "Paste Job Description",
        height=180,
        placeholder="Paste the job description here...",
        key="job_description"
    )

st.write("")

col1, col2 = st.columns([1, 2])
with col1:
    analyze_btn = st.button("Analyze", use_container_width=True)
with col2:
    st.caption("Tip: Use short resume + short JD for testing. Then use your real content.")

if analyze_btn:
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please paste both resume text and job description.")
        st.stop()

    payload = {"resume_text": resume_text, "job_description": job_description}

    with st.spinner("Analyzing… This may take a few seconds."):
        try:
            r = requests.post(f"{API_URL}/analyze", json=payload, timeout=60)
            r.raise_for_status()
            result = r.json()
        except requests.HTTPError:
            st.error(f"API error {r.status_code}: {r.text}")
            st.stop()
        except Exception as e:
            st.error(f"Request failed: {e}")
            st.stop()

    match_score = int(result.get("match_score", 0))
    missing_skills = result.get("missing_skills", [])
    feedback = result.get("feedback", "")

    st.subheader("Results")

    st.markdown("**Match Score**")
    st.progress(max(0, min(match_score, 100)) / 100)
    st.metric(label="Score (0–100)", value=match_score)

    if match_score >= 85:
        st.success("Strong match ✅")
    elif match_score >= 65:
        st.warning("Moderate match ⚠️")
    else:
        st.error("Low match ❌")

    st.markdown("**Skill Gaps**")
    if missing_skills and isinstance(missing_skills, list):
        df = pd.DataFrame({"Missing Skill": missing_skills})
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No missing skills returned (or output format was different).")

    st.markdown("**Feedback**")
    st.markdown(
        f"<div style='border:1px solid #e5e7eb; border-radius:12px; padding:14px; background:#fff;'>"
        f"{feedback if feedback else 'No feedback returned.'}"
        f"</div>",
        unsafe_allow_html=True
    )

    with st.expander("Show raw JSON"):
        st.json(result)
