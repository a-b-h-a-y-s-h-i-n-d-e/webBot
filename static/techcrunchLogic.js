document.addEventListener("DOMContentLoaded", function() {
    fetchTechCrunchData();
});

function fetchTechCrunchData() {
    const url = "https://techcrunch-api-abhays-projects-bdb1b6d4.vercel.app/";
    fetch(url)
        .then(response => response.json())
        .then(data => renderTechcrunchData(data))
        .catch(error => console.error("Error fetching TechCrunch data:", error));
}

function renderTechcrunchData(data) {
    const techcrunchList = document.getElementById("techcrunch-list");
    techcrunchList.innerHTML = ""; // Clear previous data


    for(const [key, value] of Object.entries(data)){
        const listItem = document.createElement("li");
        listItem.textContent = value; // Assuming the JSON structure has a 'title' property
        techcrunchList.appendChild(listItem);
    }
}