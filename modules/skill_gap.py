 # skill_gap.py
# Advanced skill-gap analysis for the resume screening system.

from modules.skill_extractor import extract_skills


def analyze_skill_gap(resume_text, job_description):
    """
    Compare resume skills with the skills required by a job.

    Returns matching skills, missing skills,
    and skill coverage percentage.
    """

    # Extract skills from resume and job description
    resume_skills = set(extract_skills(resume_text))
    required_skills = set(extract_skills(job_description))

    # Skills present in both
    matching_skills = sorted(
        resume_skills.intersection(required_skills)
    )

    # Skills required but missing
    missing_skills = sorted(
        required_skills - resume_skills
    )

    # Calculate skill coverage
    if required_skills:

        skill_coverage = (
            len(matching_skills) /
            len(required_skills)
        ) * 100

    else:
        skill_coverage = 0

    return {
        "resume_skills": sorted(resume_skills),
        "required_skills": sorted(required_skills),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "skill_coverage": round(skill_coverage, 2)
    }