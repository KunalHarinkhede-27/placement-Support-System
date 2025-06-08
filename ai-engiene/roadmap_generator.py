import json

# Sample predefined roadmap templates for popular goals
ROADMAP_TEMPLATES = {
    "backend developer": {
        "skills": [
            "Python", "Django/Flask", "REST APIs", "Databases (SQL/NoSQL)",
            "Docker", "AWS/GCP", "Microservices", "Testing"
        ],
        "timeline_months": 6
    },
    "frontend developer": {
        "skills": [
            "HTML", "CSS", "JavaScript", "React", "Redux",
            "Webpack", "Responsive Design", "Testing"
        ],
        "timeline_months": 5
    },
    "data scientist": {
        "skills": [
            "Python", "Pandas", "NumPy", "Scikit-learn", "Data Visualization",
            "SQL", "Machine Learning", "Deep Learning"
        ],
        "timeline_months": 7
    },
    "machine learning engineer": {
        "skills": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow/PyTorch",
            "Data Preprocessing", "Model Deployment", "AWS Sagemaker"
        ],
        "timeline_months": 8
    }
}

def generate_roadmap(goal: str, current_skills: list):
    """
    Generate skill roadmap based on user goal and current skills.

    Parameters:
        goal (str): Career goal (e.g., 'backend developer')
        current_skills (list): List of skills user already has

    Returns:
        dict: roadmap with skills to learn, timeline, and recommendations
    """
    goal_lower = goal.strip().lower()
    template = ROADMAP_TEMPLATES.get(goal_lower)

    if not template:
        return {
            "error": "Sorry, roadmap for the specified goal is not available yet."
        }

    required_skills = template["skills"]
    timeline_months = template["timeline_months"]

    # Skills missing from user profile
    skills_to_learn = [skill for skill in required_skills if skill.lower() not in map(str.lower, current_skills)]

    roadmap = {
        "goal": goal,
        "totalTimelineMonths": timeline_months,
        "currentSkills": current_skills,
        "skillsToLearn": skills_to_learn,
        "recommendation": f"Focus on mastering these {len(skills_to_learn)} key skills over the next {timeline_months} months."
    }

    return roadmap

if __name__ == "__main__":
    # Example usage
    user_goal = "Backend Developer"
    user_skills = ["Python", "Flask", "Docker"]

    roadmap = generate_roadmap(user_goal, user_skills)
    print(json.dumps(roadmap, indent=2))
