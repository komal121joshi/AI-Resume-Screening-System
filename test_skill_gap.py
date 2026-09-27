from modules.skill_gap import analyze_skill_gap


resume = """
Frontend Developer with experience in HTML, CSS,
JavaScript, React and GitHub.
"""


job_description = """
We are looking for a Frontend Developer.

Required skills:
HTML, CSS, JavaScript, React, Git, Python
"""


result = analyze_skill_gap(
    resume,
    job_description
)


print("========== SKILL GAP ANALYSIS ==========")

print("\nResume Skills:")
print(result["resume_skills"])

print("\nRequired Skills:")
print(result["required_skills"])

print("\nMatching Skills:")
print(result["matching_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])

print("\nSkill Coverage:")
print(result["skill_coverage"], "%")