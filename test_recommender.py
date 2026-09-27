from modules.job_recommender import recommend_jobs


resume = """
Frontend Developer with experience in HTML, CSS,
JavaScript, React and GitHub.
"""


csv_path = "data/jobs.csv"


recommendations = recommend_jobs(
    resume,
    csv_path,
    top_n=5
)


print("========== JOB RECOMMENDATIONS ==========")

for _, job in recommendations.iterrows():

    print("\nJob Title:", job["job_title"])

    print(
        "Match Score:",
        job["match_score"],
        "%"
    )

    print(
        "TF-IDF Score:",
        job["tfidf_score"],
        "%"
    )

    print(
        "Skill Score:",
        job["skill_score"],
        "%"
    )

    print(
        "Matching Skills:",
        job["matching_skills"]
    )

    print(
        "Missing Skills:",
        job["missing_skills"]
    )