# /ai-engine/project_idea_generator.py

from typing import List, Dict
import random

# Simple project idea pool mapped by domain
PROJECT_IDEAS_DB = {
    "web development": [
        "Build a portfolio website using MERN stack",
        "Create a blogging platform with admin dashboard",
        "Build a hotel or vehicle booking system with React and Node"
    ],
    "machine learning": [
        "Develop a model to detect fake news using NLP",
        "Predict house prices using regression models",
        "Create an animal species classifier from images"
    ],
    "data science": [
        "Analyze IPL match data and visualize trends",
        "Predict student performance from exam scores",
        "Build a COVID-19 trend predictor using time-series"
    ],
    "cybersecurity": [
        "Create a password strength checker tool",
        "Build a phishing URL detection tool",
        "Simulate a brute-force attack for educational purposes"
    ],
    "app development": [
        "Create a personal finance tracker app",
        "Build a habit tracker with notifications",
        "Develop a farming machinery booking app"
    ]
}

def suggest_projects(skills: List[str], goal: str) -> List[Dict]:
    suggestions = []
    goal = goal.lower()

    matched_domains = []
    for domain in PROJECT_IDEAS_DB:
        if any(skill in domain for skill in skills) or domain in goal:
            matched_domains.append(domain)

    if not matched_domains:
        matched_domains = list(PROJECT_IDEAS_DB.keys())  # fallback to all

    for domain in matched_domains:
        ideas = PROJECT_IDEAS_DB[domain]
        selected = random.sample(ideas, min(2, len(ideas)))  # Pick 2 per domain
        for idea in selected:
            suggestions.append({
                "domain": domain.title(),
                "idea": idea
            })

    return suggestions[:6]  # Max 6 ideas

# Test Example
if __name__ == "__main__":
    skills = ["React", "Node", "MongoDB"]
    goal = "web development"
    ideas = suggest_projects(skills, goal)
    for idea in ideas:
        print(idea)
