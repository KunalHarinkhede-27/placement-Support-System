from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your AI modules
from resume_parser import parse_resume_text  # ✅ Correct
from ats_score import evaluate_resume
from jd_matcher import match_report
from roadmap_generator import generate_roadmap
from resume_enhancer import enhance_resume_text
from chatbot_mentor import ask_mentor
from courses_recommender import recommend_courses
from peer_matcher import find_peer_matches
from project_idea_generator import suggest_projects
from skill_gap_estimator import estimate_skill_gap
from voice_transcription import transcribe_audio

app = Flask(__name__)
CORS(app)

# -----------------------
# Resume Parsing + Scoring
# -----------------------
@app.route('/api/parse-resume', methods=['POST'])
def parse_and_score_resume():
    file = request.files['resume']
    resume_text, skills = parse_resume_text(file)
    score_data = evaluate_resume(resume_text)
    return jsonify({
        "text": resume_text,
        "skills": skills,
        "score": score_data
    })

# -----------------------
# Resume vs Job JD Matching
# -----------------------
@app.route('/api/match-jd', methods=['POST'])
def match_jd():
    data = request.json
    resume = data.get("resume_text", "")
    jd = data.get("job_description", "")
    result = match_report(resume, jd)
    return jsonify(result)

# -----------------------
# Roadmap Generator
# -----------------------
@app.route('/api/roadmap', methods=['POST'])
def roadmap():
    data = request.json
    goal = data.get("goal")
    profile = data.get("profile")
    roadmap = generate_roadmap(goal, profile)
    return jsonify(roadmap)

# -----------------------
# Resume Enhancer (GPT)
# -----------------------
@app.route('/api/enhance-resume', methods=['POST'])
def enhance():
    data = request.json
    resume_text = data.get("resume_text", "")
    enhanced = enhance_resume_text(resume_text)
    return jsonify(enhanced)

# -----------------------
# Career Chatbot (Mentor)
# -----------------------
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    query = data.get("query", "")
    user_context = data.get("context", "")
    response = ask_mentor(query, user_context)
    return jsonify({"response": response})

# -----------------------
# Voice Input Transcriber
# -----------------------
@app.route('/api/voice-transcribe', methods=['POST'])
def voice_transcribe():
    audio_file = request.files['audio']
    transcript = transcribe_audio(audio_file)
    return jsonify({"transcript": transcript})

# -----------------------
# Skill Gap Estimator
# -----------------------
@app.route('/api/skill-gap', methods=['POST'])
def skill_gap():
    data = request.json
    resume_skills = data.get("resume_skills", [])
    goal_skills = data.get("goal_skills", [])
    gap = estimate_skill_gap(resume_skills, goal_skills)
    return jsonify(gap)

# -----------------------
# Project Idea Generator
# -----------------------
@app.route('/api/project-ideas', methods=['POST'])
def project_ideas():
    data = request.json
    goal = data.get("goal")
    skills = data.get("skills")
    ideas = suggest_projects(goal, skills)
    return jsonify(ideas)

# -----------------------
# Course Recommender
# -----------------------
@app.route('/api/courses', methods=['POST'])
def courses():
    data = request.json
    skills = data.get("skills")
    results = recommend_courses(skills)
    return jsonify(results)

# -----------------------
# Peer Matcher
# -----------------------
@app.route('/api/peer-match', methods=['POST'])
def peer_match():
    data = request.json
    user = data.get("user")
    peers = data.get("peers")
    matches = find_peer_matches(user, peers)
    return jsonify(matches)

# -----------------------
# Health Check
# -----------------------
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "AI Engine running successfully!"})

# -----------------------
# Run App
# -----------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
