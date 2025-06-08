Placement Support System

A complete AI-powered career planning and mentoring system designed to help users grow professionally through job matching, skill analysis, resume evaluation, and smart career roadmaps.

** Features

Authentication (Login/Register, Role-based)
Resume Analysis using AI
Career Roadmap Generator
Job Suggestion Engine
Skill Gap Analysis
Learning Path Recommendations
AI Mentor Chatbot
Peer Match System
Project Ideas Generator
Admin Dashboard (Role: admin)

** Tech Stack Layer

Technology Used

Frontend
React.js, Vite, React Router

Backend
Node.js, Express.js

AI Logic
Python, Flask

UI Styling
CSS3

API Comm.
Axios

Auth
JWT, LocalStorage

Complete Project Structure
ai-career-assistant/
├── frontend/
│   └── client/
│       ├── public/
│       ├── src/
│       │   ├── components/
│       │   │   ├── Navbar.jsx
│       │   │   ├── Sidebar.jsx
│       │   ├── context/
│       │   │   └── authContext.jsx
│       │   ├── pages/
│       │   │   ├── Home.jsx
│       │   │   ├── ProfileForm.jsx
│       │   │   ├── ResumeAnalysis.jsx
│       │   │   ├── CareerRoadmap.jsx
│       │   │   ├── JobSuggestions.jsx
│       │   │   ├── LearningPath.jsx
│       │   │   ├── PeerMatch.jsx
│       │   │   ├── ProjectIdeas.jsx
│       │   │   ├── SkillGap.jsx
│       │   │   ├── DashBoard.jsx
│       │   │   └── ChatbotMentor.jsx
│       │   ├── services/
│       │   │   └── api.js
│       │   ├── App.jsx
│       │   ├── App.css
│       │   └── main.jsx
│       ├── .env
│       ├── vite.config.js
│       └── package.json
│
├── backend/
│   └── server.js
│   └── routes/
│   └── controllers/
│   └── models/
│   └── middleware/
│   └── config/
│   └── package.json
│   └── .env
│
├── ai-backend/
│   └── app.py
│   └── resume_parser.py
│   └── recommendation_engine.py
│   └── chatbot_engine.py
│   └── requirements.txt
│
└── README.md

Run the Project Locally

Step 1: Clone the Repository
git clone https://github.com/kunalharinkhede-27/Placement-Support-System.git
cd Placement-Support-System
Step 2: Frontend (React + Vite)
cd frontend/client
npm install
Create a .env file inside frontend/client:
REACT_APP_NODE_API=http://localhost:8000/api
REACT_APP_PY_API=http://localhost:5000/api
Then, run the dev server:
npm run dev
Step 3: Backend (Node.js)
cd backend
npm install
Add a .env file with:
PORT=8000
MONGO_URI=your_mongodb_connection
JWT_SECRET=your_jwt_secret
Run the backend server:
npm run dev
Step 4: AI Python Backend (Flask)
cd ai-engiene
python -m venv venv
source venv/bin/activate  # for Windows: venv\Scripts\activate
pip install -r requirements.txt
Run the AI API:
python app.py

Contributing
We welcome contributions!

Fork the repo
Create a feature branch git checkout -b feature-name
Commit your changes git commit -m "Added feature"
Push to your branch git push origin feature-name
Create a Pull Request

**License
This project is licensed under the MIT License.

** Developed By
Kunal HarinkhedeFinal Year | MERN Developer | AI + Web Projects | E-Yantra Lab LeaderGitHub: @kunalharinkhede

** Show your support
Give this project a ⭐ if you found it helpful or inspiring!
