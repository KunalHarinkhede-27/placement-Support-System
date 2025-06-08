import re
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_keywords(text, top_n=50):
    """
    Extract top N keywords by frequency from the given text.
    Returns a set of keywords.
    """
    text = clean_text(text)
    words = text.split()
    stopwords = set([
        "the", "and", "for", "with", "that", "from", "this", "you",
        "your", "are", "have", "will", "can", "all", "our", "has",
        "but", "not", "use", "or", "on", "in", "to", "a", "an",
        "of", "we", "at", "as", "by", "be", "is", "if", "so",
        "it", "they", "their", "which", "these"
    ])
    filtered_words = [w for w in words if w not in stopwords and len(w) > 2]
    freq = Counter(filtered_words)
    common = freq.most_common(top_n)
    keywords = set([k for k, v in common])
    return keywords

def jd_match_score(resume_text, jd_text):
    """
    Compares resume and job description texts to calculate match %.
    """
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    if not jd_keywords:
        return 0

    matched_keywords = resume_keywords.intersection(jd_keywords)
    match_ratio = len(matched_keywords) / len(jd_keywords)

    # Return percentage (0-100)
    return round(match_ratio * 100, 2)

def match_report(resume_text, jd_text):
    score = jd_match_score(resume_text, jd_text)
    report = {
        "matchScore": score,
        "matchedKeywords": list(extract_keywords(resume_text).intersection(extract_keywords(jd_text))),
        "jdKeywords": list(extract_keywords(jd_text)),
    }

    if score > 80:
        report["feedback"] = "Strong match between resume and job description."
    elif score > 50:
        report["feedback"] = "Moderate match; consider adding missing skills."
    else:
        report["feedback"] = "Low match; review job description and update resume accordingly."

    return report

if __name__ == "__main__":
    sample_resume = """
    Skilled in Python, JavaScript, React, Node.js, and AWS Cloud.
    Experience with REST APIs, Docker, and Kubernetes.
    """
    sample_jd = """
    Looking for candidates with experience in React, Node.js, AWS, Docker, and CI/CD pipelines.
    Familiarity with Kubernetes is a plus.
    """
    result = match_report(sample_resume, sample_jd)
    print(f"Match Score: {result['matchScore']}%")
    print("Feedback:", result['feedback'])
    print("Matched Keywords:", result['matchedKeywords'])
