 # resume_matcher.py
# Advanced resume-job matching using:
# 1. TF-IDF similarity
# 2. Skill matching
# 3. Weighted overall score

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from modules.skill_extractor import extract_skills


def calculate_tfidf_score(resume_text, job_description):
    """
    Calculate similarity between resume and job description
    using TF-IDF and cosine similarity.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return similarity[0][0] * 100


def calculate_skill_score(resume_text, job_description):
    """
    Calculate how many required job skills
    are present in the resume.
    """

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    if not job_skills:
        return 0

    matching_skills = resume_skills.intersection(job_skills)

    skill_score = (
        len(matching_skills) / len(job_skills)
    ) * 100

    return skill_score


def calculate_match_score(resume_text, job_description):
    """
    Calculate the final weighted match score.

    TF-IDF similarity = 60%
    Skill matching    = 40%
    """

    tfidf_score = calculate_tfidf_score(
        resume_text,
        job_description
    )

    skill_score = calculate_skill_score(
        resume_text,
        job_description
    )

    final_score = (
        (tfidf_score * 0.60) +
        (skill_score * 0.40)
    )

    return round(final_score, 2)


def get_match_details(resume_text, job_description):
    """
    Return detailed matching information.
    """

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matching_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills - resume_skills
    )

    tfidf_score = calculate_tfidf_score(
        resume_text,
        job_description
    )

    skill_score = calculate_skill_score(
        resume_text,
        job_description
    )

    final_score = (
        (tfidf_score * 0.60) +
        (skill_score * 0.40)
    )

    return {
        "tfidf_score": round(tfidf_score, 2),
        "skill_score": round(skill_score, 2),
        "final_score": round(final_score, 2),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    }