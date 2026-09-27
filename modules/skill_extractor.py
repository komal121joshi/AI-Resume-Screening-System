# skill_extractor.py
# Advanced skill extraction for the AI Resume Screening System.
# Skills are organized into different categories.

SKILL_DATABASE = {

    "Programming Languages": [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "typescript",
        "php"
    ],

    "Frontend": [
        "html",
        "css",
        "javascript",
        "react",
        "angular",
        "vue",
        "bootstrap",
        "tailwind"
    ],

    "Backend": [
        "django",
        "flask",
        "node.js",
        "nodejs",
        "express",
        "spring boot",
        "rest api"
    ],

    "Data Science": [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "power bi",
        "excel",
        "data analysis",
        "data visualization"
    ],

    "Machine Learning & AI": [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "scikit-learn",
        "tensorflow",
        "keras",
        "pytorch",
        "natural language processing",
        "nlp"
    ],

    "Databases": [
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "sqlite",
        "oracle"
    ],

    "Tools & Technologies": [
        "git",
        "github",
        "docker",
        "streamlit",
        "aws",
        "linux"
    ]
}


def extract_skills(text):
    """
    Extract skills from resume text.

    Returns:
        List of detected skills.
    """

    text = text.lower()

    found_skills = []

    for category, skills in SKILL_DATABASE.items():

        for skill in skills:

            if skill.lower() in text:

                if skill not in found_skills:
                    found_skills.append(skill)

    return found_skills


def extract_skills_by_category(text):
    """
    Extract skills and organize them by category.
    """

    text = text.lower()

    categorized_skills = {}

    for category, skills in SKILL_DATABASE.items():

        found = []

        for skill in skills:

            if skill.lower() in text:

                if skill not in found:
                    found.append(skill)

        if found:
            categorized_skills[category] = found

    return categorized_skills