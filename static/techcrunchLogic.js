document.addEventListener("DOMContentLoaded", function() {
    showLoadingBar();
    fetchTechCrunchData();
});

function showLoadingBar(){
    const loadingBar = document.getElementById('loading-bar');
    loadingBar.style.display = "block";
}
function hideLoadingBar(){
    const loadingBar = document.getElementById('loading-bar');
    loadingBar.style.display = "none";
}

function fetchTechCrunchData() {
    const url = "https://techcrunch-api.vercel.app/";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            hideLoadingBar();
            renderTechcrunchData(data)})
        .catch(error => console.error("Error fetching TechCrunch data:", error));
}

function renderTechcrunchData(data) {
    const techcrunchList = document.getElementById("techcrunch-list");
    // cleaning previous data!
    techcrunchList.innerHTML = ""; 

    for(const [key, value] of Object.entries(data)){
        const listItem = document.createElement("li");
        const anchor = document.createElement("a");
        anchor.textContent = key;
        anchor.href = value;
        anchor.target = "_blank";
        listItem.appendChild(anchor);
        techcrunchList.appendChild(listItem);
    }
}

