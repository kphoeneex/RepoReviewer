def score_repository(data):
    score = 0
    roadmap = []

    if data["file_count"] > 10:
        score += 15
    else:
        roadmap.append("Increase project complexity by adding more features")

    if data["has_readme"]:
        score += 15
        if data["readme_length"] < 300:
            roadmap.append("Expand README with setup and usage instructions")
    else:
        roadmap.append("Add a README.md explaining the project")

    if data["test_files"] > 0:
        score += 20
    else:
        roadmap.append("Add unit or integration tests")

    if data["commit_count"] > 10:
        score += 15
    else:
        roadmap.append("Commit more frequently with meaningful messages")

    if len(data["languages"]) > 1:
        score += 15
    else:
        roadmap.append("Structure code better by separating concerns")

    score = min(score, 100)

    if score < 40:
        level = "Beginner"
    elif score < 70:
        level = "Intermediate"
    else:
        level = "Advanced"

    summary = generate_summary(score, data)

    return {
        "score": score,
        "level": level,
        "summary": summary,
        "roadmap": roadmap
    }


def generate_summary(score, data):
    if score >= 80:
        return "Excellent project structure with strong development practices. Minor improvements can make it production-ready."
    elif score >= 50:
        return "The project has a solid foundation but lacks some best practices such as testing and documentation."
    else:
        return "This is a basic project with limited structure and missing best practices. Significant improvements are recommended."
