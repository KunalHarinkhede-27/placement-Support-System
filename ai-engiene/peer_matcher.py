# /ai-engine/peer_matcher.py

from typing import List, Dict
from difflib import SequenceMatcher

# Example peer database (replace with MongoDB or external DB queries in production)
PEERS_DB = [
    {"id": "1", "name": "Aarav", "skills": ["python", "machine learning"], "goal": "data scientist"},
    {"id": "2", "name": "Meera", "skills": ["react", "nodejs"], "goal": "full stack developer"},
    {"id": "3", "name": "Ravi", "skills": ["java", "system design"], "goal": "backend developer"},
    {"id": "4", "name": "Sara", "skills": ["ui/ux", "figma", "frontend"], "goal": "frontend developer"},
    {"id": "5", "name": "Raj", "skills": ["python", "data science"], "goal": "data scientist"},
]

def calculate_similarity(goal1: str, goal2: str) -> float:
    return SequenceMatcher(None, goal1.lower(), goal2.lower()).ratio()

def find_peer_matches(user_skills: List[str], user_goal: str) -> List[Dict]:
    matches = []

    for peer in PEERS_DB:
        skill_overlap = len(set(peer["skills"]) & set([s.lower() for s in user_skills]))
        goal_similarity = calculate_similarity(peer["goal"], user_goal)

        score = (skill_overlap * 2) + (goal_similarity * 3)  # Weighted scoring

        matches.append({
            "peer_id": peer["id"],
            "name": peer["name"],
            "shared_skills": list(set(peer["skills"]) & set([s.lower() for s in user_skills])),
            "goal": peer["goal"],
            "match_score": round(score, 2)
        })

    # Return top 3 sorted by match_score
    return sorted(matches, key=lambda x: x["match_score"], reverse=True)[:3]

# Test run
if __name__ == "__main__":
    test_skills = ["Python", "Data Science"]
    test_goal = "Data Scientist"
    results = find_peer_matches(test_skills, test_goal)
    for r in results:
        print(r)
