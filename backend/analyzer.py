import os
import shutil
import git
import requests
import stat
import time


TEMP_DIR = "temp_repos"

def remove_readonly(func, path, excinfo):
    """
    Windows-safe handler for removing read-only files
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)

def analyze_repository(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]
    local_path = os.path.join(TEMP_DIR, repo_name)

    if os.path.exists(local_path):
        shutil.rmtree(local_path)

    git.Repo.clone_from(repo_url, local_path)

    analysis = {
        "file_count": 0,
        "has_readme": False,
        "readme_length": 0,
        "test_files": 0,
        "languages": set(),
        "commit_count": get_commit_count(repo_url)
    }

    for root, dirs, files in os.walk(local_path):
        for file in files:
            analysis["file_count"] += 1
            analysis["languages"].add(file.split(".")[-1])

            if file.lower().startswith("readme"):
                analysis["has_readme"] = True
                with open(os.path.join(root, file), errors="ignore") as f:
                    analysis["readme_length"] = len(f.read())

            if "test" in file.lower():
                analysis["test_files"] += 1

    analysis["languages"] = list(analysis["languages"])
    time.sleep(1)

    # Safely remove cloned repository
    shutil.rmtree(local_path, onerror=remove_readonly)


    return analysis


def get_commit_count(repo_url):
    parts = repo_url.replace("https://github.com/", "").split("/")
    api_url = f"https://api.github.com/repos/{parts[0]}/{parts[1]}/commits"

    response = requests.get(api_url)
    if response.status_code != 200:
        return 0

    return len(response.json())
