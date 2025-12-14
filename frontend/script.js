const analyzeBtn = document.getElementById("analyzeBtn");
const repoUrlInput = document.getElementById("repoUrl");
const loader = document.getElementById("loader");
const results = document.getElementById("results");

const scoreValue = document.getElementById("scoreValue");
const level = document.getElementById("level");
const summaryText = document.getElementById("summaryText");
const roadmapList = document.getElementById("roadmapList");

analyzeBtn.addEventListener("click", () => {
    const repoUrl = repoUrlInput.value.trim();

    if (!repoUrl.startsWith("https://github.com/")) {
        alert("Please enter a valid GitHub repository URL");
        return;
    }

    results.classList.add("hidden");
    loader.classList.remove("hidden");

    // 🔹 REAL BACKEND CALL
    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ repo_url: repoUrl })
    })
    .then(response => response.json())
    .then(data => {
        loader.classList.add("hidden");

        if (data.error) {
            alert(data.error);
            return;
        }

        displayResults(data);
    })
    .catch(() => {
        loader.classList.add("hidden");
        alert("Failed to connect to backend");
    });
});

function displayResults(data) {
    results.classList.remove("hidden");

    scoreValue.textContent = data.score;
    level.textContent = data.level;
    summaryText.textContent = data.summary;

    roadmapList.innerHTML = "";
    data.roadmap.forEach(step => {
        const li = document.createElement("li");
        li.textContent = step;
        roadmapList.appendChild(li);
    });
}
