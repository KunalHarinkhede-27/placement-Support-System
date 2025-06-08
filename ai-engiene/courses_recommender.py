# /ai-engine/courses_recommender.py

import json

# Example course database (in real-time you can extend this using Coursera, Udemy, edX APIs)
COURSE_DB = {
    "python": [
        {"title": "Python for Everybody", "platform": "Coursera", "type": "free", "url": "https://www.coursera.org/specializations/python"},
        {"title": "Complete Python Bootcamp", "platform": "Udemy", "type": "paid", "url": "https://www.udemy.com/course/complete-python-bootcamp/"},
    ],
    "react": [
        {"title": "React Basics", "platform": "Codecademy", "type": "free", "url": "https://www.codecademy.com/learn/react-101"},
        {"title": "React Front To Back", "platform": "Udemy", "type": "paid", "url": "https://www.udemy.com/course/react-front-to-back-2022/"},
    ],
    "machine learning": [
        {"title": "Machine Learning by Stanford", "platform": "Coursera", "type": "free", "url": "https://www.coursera.org/learn/machine-learning"},
        {"title": "Machine Learning A-Z", "platform": "Udemy", "type": "paid", "url": "https://www.udemy.com/course/machinelearning/"},
    ]
}

def recommend_courses(skills):
    recommendations = []

    for skill in skills:
        key = skill.lower()
        if key in COURSE_DB:
            recommendations.extend(COURSE_DB[key])

    return recommendations

# Example usage (for internal test)
if __name__ == "__main__":
    test_skills = ["Python", "React"]
    recs = recommend_courses(test_skills)
    print(json.dumps(recs, indent=2))
