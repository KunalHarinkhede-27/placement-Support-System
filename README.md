## Placement Support System

A complete AI-powered career planning and mentoring system designed to help users grow professionally through job matching, skill analysis, resume evaluation, and smart career roadmaps.

# Features

1. Authentication (Login/Register, Role-based)
2. Resume Analysis using AI
3. Career Roadmap Generator
4. Job Suggestion Engine
5. Skill Gap Analysis
6. Learning Path Recommendations
7. AI Mentor Chatbot
8. Peer Match System
9. Project Ideas Generator
10. Admin Dashboard (Role: admin)

## Tech Stack Layer

# Technology Used

** Frontend
- React.js, Vite, React Router

** Backend
- Node.js, Express.js

** AI Logic
- Python, Flask

** UI Styling
- CSS3

** API Comm.
- Axios

** Auth
- JWT, LocalStorage

## Complete Project Structure

placement-support-system/

# frontend/

-- client/
- public/
- src/
  - components/
  - context/
  - pages/
  - services/

- App.jsx
- App.css
- main.jsx
- .env
- vite.config.js
- package.json

# backend/

- server.js
- routes/
- controllers/
- models/
- middleware/
- config/
- package.json
- .env

# ai-backend/

# requirements.txt

README.md

** Run the Project Locally

# Step 1: Clone the Repository
- git clone https://github.com/kunalharinkhede-27/Placement-Support-System.git
- cd Placement-Support-System
# Step 2: Frontend (React + Vite)
- cd frontend/client
- npm install
Create a .env file inside frontend/client:
- REACT_APP_NODE_API=http://localhost:8000/api
- REACT_APP_PY_API=http://localhost:5000/api
* Then, run the dev server:
- npm run dev
# Step 3: Backend (Node.js)
- cd backend
- npm install
* Add a .env file with:
- PORT=8000
- MONGO_URI=your_mongodb_connection
- JWT_SECRET=your_jwt_secret
* Run the backend server:
- npm run dev
# Step 4: AI Python Backend (Flask)
- cd ai-engiene
- python -m venv venv
- source venv/bin/activate  # for Windows: venv\Scripts\activate
- pip install -r requirements.txt
* Run the AI API:
- python app.py

## Contributing
- We welcome contributions!

** Fork the repo
- Create a feature branch git checkout -b feature-name
- Commit your changes git commit -m "Added feature"
- Push to your branch git push origin feature-name
- Create a Pull Request

** License
- This project is licensed under the MIT License.

** Developed By
Kunal HarinkhedeFinal Year | MERN Developer | AI + Web Projects | E-Yantra Lab LeaderGitHub: @kunalharinkhede

** Show your support
Give this project a ⭐ if you found it helpful or inspiring!
