# skill_gap_estimator.py

def estimate_skill_gap(resume_skills, job_required_skills):
    """
    Estimate the gap between resume skills and job-required skills.
    
    Args:
        resume_skills (list): Skills extracted from the resume.
        job_required_skills (list): Skills required for the target job or goal.
        
    Returns:
        dict: {
            'matched_skills': [...],
            'missing_skills': [...],
            'gap_percentage': float
        }
    """
    resume_skills_set = set([skill.lower().strip() for skill in resume_skills])
    job_skills_set = set([skill.lower().strip() for skill in job_required_skills])

    matched = resume_skills_set & job_skills_set
    missing = job_skills_set - resume_skills_set

    gap_percentage = round((len(missing) / len(job_skills_set)) * 100, 2) if job_skills_set else 0.0

    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "gap_percentage": gap_percentage
    }

# Example usage:
if __name__ == "__main__":
    resume = ["Java", "React", "MongoDB", "REST APIs", "Git"]
    target_job = ["Java", "Spring Boot", "MongoDB", "Docker", "CI/CD", "Git"]

    gap_report = estimate_skill_gap(resume, target_job)
    print(gap_report)
