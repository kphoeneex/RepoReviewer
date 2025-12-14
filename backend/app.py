from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import analyze_repository
from scorer import score_repository

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    repo_url = data.get("repo_url")

    if not repo_url or "github.com" not in repo_url:
        return jsonify({"error": "Invalid GitHub URL"}), 400

    try:
        analysis_data = analyze_repository(repo_url)
        final_report = score_repository(analysis_data)
        return jsonify(final_report)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
