GitGrade 🚀

GitGrade is a simple system that evaluates a GitHub repository and converts it into a score, short summary, and a clear improvement roadmap.
The idea is to help students understand how their projects look from a recruiter’s or mentor’s point of view.

Instead of focusing on marks or theory, GitGrade looks at real project signals like code structure, documentation, tests, and commit history.

Why GitGrade?

Many students have GitHub projects but don’t know:

How good their code quality actually is

What is missing in their repository

What to improve next to make the project stronger

GitGrade acts like a mirror for your repository and gives honest, actionable feedback.

How the Project Works (High Level)

The user pastes a public GitHub repository URL into the frontend.

The backend fetches repository information using:

GitHub APIs (for commits and metadata)

A temporary clone of the repository (for file and structure analysis)

The system analyzes:

File and folder structure

README and documentation presence

Test files

Commit frequency

Languages used

A score out of 100 is calculated using rule-based logic.

Based on the analysis:

A short summary is generated

A personalized improvement roadmap is created

If an OpenAI API key is available, advanced feedback is generated.
Otherwise, the system uses a normal template-based fallback so results are always available.

The goal is to keep the system reliable, transparent, and easy to understand.

Key Features

GitHub repository evaluation

Score (0–100) with skill level

Clear written summary

Actionable improvement roadmap

Works even without AI API keys

Clean separation between frontend and backend

Tech Stack
Frontend

HTML

CSS

JavaScript

Used to:

Accept GitHub repository URL

Display score, summary, and roadmap

Backend

Python

Flask

GitPython

GitHub REST API

Used to:

Fetch and analyze repository data

Calculate scores

Generate feedback

How to Run the Project
Backend Setup
cd backend
pip install -r requirements.txt
python app.py


The backend will run on:

http://127.0.0.1:5000

Frontend Setup

Simply open:

frontend/index.html


in your browser.

Output Example

Score: 76 / 100 (Advanced)

Summary: Short evaluation of the repository quality

Roadmap: Step-by-step improvements like:

Add README

Write unit tests

Improve commit practices

Design Philosophy

Rule-based scoring for fairness and explainability

Optional AI for better wording, not decision-making

No dependency on paid APIs

Honest feedback over inflated scores

Hackathon Context

This project was built as part of the GitGrade Hackathon under the theme:

AI + Code Analysis + Developer Profiling

Future Improvements

Deeper code quality analysis (linting, complexity)

CI/CD detection

Project comparison feature

Deployment as a web service