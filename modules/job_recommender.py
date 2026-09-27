
import pandas as pd

from modules.resume_matcher import get_match_details


def recommend_jobs(resume_text, csv_path, top_n=5):
    """
    Recommend the most relevant jobs for a resume.
    """

    jobs = pd.read_csv(csv_path)

    # Clean column names
    jobs.columns = jobs.columns.str.strip()

    # Check required columns
    required_columns = [
        "job_title",
        "job_description",
        "skills"
    ]

    for column in required_columns:
        if column not in jobs.columns:
            raise ValueError(
                f"Missing column '{column}' in jobs.csv. "
                f"Available columns: {jobs.columns.tolist()}"
            )

    recommendations = []

    # Compare resume with every job
    for _, job in jobs.iterrows():

        job_title = str(job["job_title"])
        job_description = str(job["job_description"])

        result = get_match_details(
            resume_text,
            job_description
        )

        recommendations.append({
            "job_title": job_title,
            "match_score": result["final_score"],
            "tfidf_score": result["tfidf_score"],
            "skill_score": result["skill_score"],
            "matching_skills": ", ".join(
                result["matching_skills"]
            ),
            "missing_skills": ", ".join(
                result["missing_skills"]
            )
        })

    recommendations_df = pd.DataFrame(
        recommendations
    )

    recommendations_df = recommendations_df.sort_values(
        by="match_score",
        ascending=False
    )

    return recommendations_df.head(top_n)
 
