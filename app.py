import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }

    /* Main container */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* Header */
    .header {
        text-align: center;
        padding: 35px;
        border-radius: 20px;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }

    .header h1 {
        font-size: 42px;
        margin-bottom: 10px;
        color: white;
    }

    .header p {
        font-size: 18px;
        color: #e0e7ff;
    }

    /* Cards */
    .card {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.15);
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    .card h2 {
        color: white;
        margin-bottom: 10px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(124,58,237,0.5);
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 12px;
    }

    /* Text area */
    textarea {
        border-radius: 12px !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 40px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="header">
    <h1>🤖 AI Resume Analyzer</h1>
    <p>Smart Resume Screening & Job Recommendation System</p>
</div>
""", unsafe_allow_html=True)


# ---------------- TWO COLUMNS ----------------

col1, col2 = st.columns(2)


# ---------------- RESUME UPLOAD ----------------

with col1:

    st.markdown("""
    <div class="card">
        <h2>📄 Upload Resume</h2>
        <p>Upload your resume in PDF, DOCX or TXT format.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose your resume",
        type=["pdf", "docx", "txt"],
        label_visibility="collapsed"
    )


# ---------------- JOB DESCRIPTION ----------------

with col2:

    st.markdown("""
    <div class="card">
        <h2>💼 Job Description</h2>
        <p>Enter the job description you want to apply for.</p>
    </div>
    """, unsafe_allow_html=True)

    job_description = st.text_area(
        "Job Description",
        placeholder="Example: Looking for a Frontend Developer skilled in HTML, CSS, JavaScript, React and Git...",
        height=150,
        label_visibility="collapsed"
    )


# ---------------- ANALYZE ----------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Analyze Resume"):

    if uploaded_file is None:

        st.warning("⚠️ Please upload your resume first.")

    elif not job_description.strip():

        st.warning("⚠️ Please enter a job description.")

    else:

        st.success("✅ Resume uploaded successfully!")

        st.markdown("""
        <div class="card">
            <h2>📊 Analysis Result</h2>
            <p>Your resume is ready for AI analysis.</p>
        </div>
        """, unsafe_allow_html=True)

        # Temporary result
        st.metric("Resume Status", "Ready")
        st.metric("Job Description", "Received")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    🤖 AI Resume Analyzer | Smart Recruitment System
</div>
""", unsafe_allow_html=True)