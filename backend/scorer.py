from ai_engine import generate_feedback


def score_repository(data):
    score = 0

    if data["file_count"] > 10:
        score += 15
    if data["has_readme"]:
        score += 15
    if data["test_files"] > 0:
        score += 20
    if data["commit_count"] > 10:
        score += 15
    if len(data["languages"]) > 1:
        score += 15

    score = min(score, 100)

    if score < 40:
        level = "Beginner"
    elif score < 70:
        level = "Intermediate"
    else:
        level = "Advanced"

    feedback = generate_feedback(data, score, level)

    return {
        "score": score,
        "level": level,
        "summary": feedback["summary"],
        "roadmap": feedback["roadmap"],
        "ai_mode": feedback["mode"]
    }
