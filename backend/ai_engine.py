import os
import json
import requests


def generate_feedback(analysis_data, score, level):
    if os.getenv("OPENAI_API_KEY"):
        result = openai_feedback(analysis_data, score, level)
        if result:
            result["mode"] = "openai"
            return result

    # fallback (always works)
    result = normal_feedback(analysis_data, score, level)
    result["mode"] = "normal"
    return result


# ---------------- OPENAI MODE ----------------
def openai_feedback(data, score, level):
    try:
        prompt = build_prompt(data, score, level)

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a senior software mentor reviewing a GitHub repository."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.4
            },
            timeout=15
        )

        content = response.json()["choices"][0]["message"]["content"]
        return json.loads(content)

    except Exception:
        return None


# ---------------- NORMAL MODE ----------------
def normal_feedback(data, score, level):
    summary = (
        f"This repository is evaluated as {level.lower()} with a score of {score}/100. "
        f"It contains {data['file_count']} files and uses {', '.join(data['languages'])}. "
    )

    if data["has_readme"]:
        summary += "Basic documentation is present. "
    else:
        summary += "Documentation is missing. "

    if data["test_files"] == 0:
        summary += "Automated tests are not implemented, which affects maintainability."

    roadmap = []

    if not data["has_readme"]:
        roadmap.append("Add a detailed README with setup and usage instructions.")
    if data["test_files"] == 0:
        roadmap.append("Write unit tests for core functionality.")
    if data["commit_count"] < 10:
        roadmap.append("Commit more frequently with meaningful commit messages.")
    if len(data["languages"]) <= 1:
        roadmap.append("Improve project structure by separating logic into modules.")

    return {
        "summary": summary,
        "roadmap": roadmap
    }


# ---------------- PROMPT ----------------
def build_prompt(data, score, level):
    return f"""
Repository analysis:
{json.dumps(data, indent=2)}

Score: {score}/100
Level: {level}

Generate:
1. A concise 3–4 line summary
2. A personalized improvement roadmap (3–6 bullet points)

Return ONLY valid JSON:
{{
  "summary": "...",
  "roadmap": ["...", "..."]
}}
"""
