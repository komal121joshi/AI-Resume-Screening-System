from modules.resume_matcher import get_match_details


resume = """
Frontend Developer with experience in HTML, CSS,
JavaScript, React and GitHub.
"""


job_description = """
We are looking for a Frontend Developer with experience
in HTML, CSS, JavaScript, React and Git.
"""


result = get_match_details(
    resume,
    job_description
)


print("========== MATCHING RESULTS ==========")

print("TF-IDF Score:", result["tfidf_score"], "%")

print("Skill Score:", result["skill_score"], "%")

print("Final Match Score:", result["final_score"], "%")

print("\nMatching Skills:")
print(result["matching_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])