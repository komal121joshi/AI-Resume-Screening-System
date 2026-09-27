from modules.skill_extractor import (
    extract_skills,
    extract_skills_by_category
)


resume_text = """
Frontend Developer with experience in HTML, CSS,
JavaScript, React and GitHub.

I also have knowledge of Python, SQL and MongoDB.
"""


# Extract all skills
skills = extract_skills(resume_text)

print("========== ALL SKILLS ==========")
print(skills)


# Extract skills by category
categorized_skills = extract_skills_by_category(resume_text)

print("\n========== SKILLS BY CATEGORY ==========")

for category, skill_list in categorized_skills.items():

    print(f"\n{category}:")
    print(skill_list)