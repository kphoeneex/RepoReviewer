# Repo Reviewer 

Repo Reviewer is a simple system that evaluates a GitHub repository and converts it into a **score**, a **short summary**, and a **clear improvement roadmap**.  
It helps students and developers understand how their projects look from a recruiter’s or mentor’s point of view.

---

## How to Run the Project

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```


## Frontend Setup

Open the following file directly in your browser:

```text
frontend/index.html
```

## What is Repo Reviewer?

Repo Reviewer analyzes real signals from a GitHub repository instead of focusing on theory or marks.  
It evaluates how complete, clean, and maintainable a project is based on its structure and development practices.

---

## Why Repo Reviewer?

Many students upload projects to GitHub but are unsure:

- Whether their code is well structured  
- What important parts are missing  
- What to improve next to make the project stronger  

Repo Reviewer acts as a **mirror for the repository**, providing honest and actionable feedback.

---

## How the Project Works

1. The user pastes a **public GitHub repository URL** into the frontend.
2. The backend collects repository data using:
   - GitHub APIs for commit and metadata analysis  
   - A temporary clone of the repository for file and structure analysis
3. The system analyzes:
   - File and folder structure  
   - README and documentation presence  
   - Test files  
   - Commit frequency  
   - Languages used
4. A **score out of 100** is calculated using rule-based logic.
5. Based on the analysis:
   - A short summary is generated  
   - A personalized improvement roadmap is created
6. If an OpenAI API key is available, advanced feedback is generated.  
   Otherwise, the system falls back to a normal template-based approach so results are always available.

The system is designed to be **reliable, transparent, and easy to understand**.

---

## Key Features

- GitHub repository evaluation  
- Score (0–100) with skill level  
- Clear written summary  
- Actionable improvement roadmap  
- Works even without AI API keys  
- Clean separation between frontend and backend  

---

## Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

Used to accept the GitHub repository URL and display results.

### Backend
- Python  
- Flask  
- GitPython  
- GitHub REST API  

Used to fetch repository data, analyze it, and generate feedback.

---

## Output Example

- **Score:** 76 / 100 (Advanced)  
- **Summary:** Short evaluation of repository quality  
- **Roadmap:** Step-by-step improvements such as:
  - Add README  
  - Write unit tests  
  - Improve commit practices  

---

## Design Philosophy

- Rule-based scoring for fairness and explainability  
- Optional AI for better wording, not decision-making  
- No dependency on paid APIs  
- Honest feedback over inflated scores  
