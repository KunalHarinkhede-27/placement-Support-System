import re
from collections import Counter

# Example: list of important keywords typically desired in resumes for tech roles
DEFAULT_KEYWORDS = [
    "python", "java", "javascript", "react", "node.js", "express", "mongodb",
    "sql", "aws", "docker", "kubernetes", "git", "ci/cd", "linux", "rest api",
    "machine learning", "deep learning", "nlp", "data structures", "algorithms"
]

def clean_text(text):
    """Lowercase and remove non-alphanumeric characters except spaces."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def keyword_score(text, keywords=DEFAULT_KEYWORDS):
    """
    Calculates keyword match score based on frequency and presence of keywords.
    Returns score out of 100.
    """
    text = clean_text(text)
    word_counts = Counter(text.split())

    matched_keywords = [kw for kw in keywords if kw in text]
    matched_count = len(matched_keywords)

    # Score is percentage of keywords present
    if not keywords:
        return 0
    keyword_presence_score = (matched_count / len(keywords)) * 100

    # Bonus points for multiple mentions of key skills (frequency based)
    freq_score = 0
    for kw in matched_keywords:
        freq = word_counts[kw]
        freq_score += min(freq, 5)  # max 5 counts per keyword considered

    freq_score = min(freq_score * 2, 30)  # cap frequency bonus to 30 points

    # Combine scores, weighted
    total_score = (0.7 * keyword_presence_score) + (0.3 * freq_score)

    return round(min(total_score, 100), 2)

def evaluate_resume(text, keywords=DEFAULT_KEYWORDS):
    """
    Returns a dictionary with score and feedback messages.
    """
    score = keyword_score(text, keywords)

    feedback = []
    if score > 80:
        feedback.append("Excellent keyword match and relevant skills found.")
    elif score > 50:
        feedback.append("Good match but consider adding more relevant skills or keywords.")
    else:
        feedback.append("Poor match; resume lacks many important keywords.")

    # Additional heuristic checks (basic examples)
    if len(text) < 200:
        feedback.append("Resume looks too short; consider adding more details.")
    if "education" not in text.lower():
        feedback.append("Consider adding an Education section for better clarity.")

    return {
        "score": score,
        "feedback": feedback
    }


if __name__ == "__main__":
    # Simple test
    sample_text = """
    Experienced Python developer skilled in Django, Flask, REST API, and Docker.
    Familiar with AWS cloud services and CI/CD pipelines.
    """
    result = evaluate_resume(sample_text)
    print(f"Score: {result['score']}")
    print("Feedback:")
    for msg in result["feedback"]:
        print("-", msg)
