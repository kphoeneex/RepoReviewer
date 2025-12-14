Repo Reviewer 

Repo Reviewer is a simple system that evaluates a GitHub repository and converts it into a score, short summary, and a clear improvement roadmap.
The goal is to help students and developers understand how their projects look from a recruiter’s or mentor’s point of view. Instead of focusing on theory or marks, Repo Reviewer looks at real project signals like structure, documentation, tests, and commit history.

Why Repo Reviewer?
Many students push projects to GitHub but are unsure:
.Whether their codebase is clean or messy
.What important things are missing
.What to improve next to make the project stronger

Repo Reviewer acts like a mirror for your repository, giving honest and actionable feedback.

How the Project Works (High Level)
.The user pastes a public GitHub repository URL into the frontend.
.The backend fetches repository information using:
  GitHub APIs (for commits and metadata)
  A temporary clone of the repository (for structure and file analysis)
.The system analyzes:
  File and folder structure
  README and documentation presence
  Test files
  Commit frequency
  Languages used
  A score out of 100 is calculated using rule-based logic.
.Based on the analysis:
  A short summary is generated
  A personalized improvement roadmap is created
.If an OpenAI API key is available, advanced feedback is generated. Otherwise, the system falls back to a normal template-based approach so results are always available.

The focus is on keeping the system reliable, transparent, and easy to understand.

Key Features
.GitHub repository evaluation
.Score (0–100) with skill level
.Clear written summary
.Actionable improvement roadmap
.Works even without AI API keys
.Clean separation between frontend and backend

Tech Stack:

Frontend
-HTML
-CSS
-JavaScript

Used to:
Accept GitHub repository URL
Display score, summary, and roadmap

Backend
-Python
-Flask
-GitPython
-GitHub REST API

Used to:
Fetch and analyze repository data
Calculate scores
Generate feedback

**How to Run the Project
Backend Setup
cd backend
pip install -r requirements.txt
python app.py

The backend runs on:
http://127.0.0.1:5000**

Frontend Setup
Open the following file directly in your browser:
frontend/index.html
Output Example
Score: 76 / 100 (Advanced)

Summary: Short evaluation of the repository quality

Roadmap: Step-by-step improvements such as:
Add README
Write unit tests
Improve commit practices
Design Philosophy
Rule-based scoring for fairness and explainability
Optional AI for better wording, not decision-making



Deeper code quality analysis (linting, complexity)

CI/CD detection

Repository comparison

Deployment as a hosted web service
