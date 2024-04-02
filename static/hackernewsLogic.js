document.addEventListener("DOMContentLoaded", function() {
    fetchHackerNewsData();
});

function fetchHackerNewsData() {
    const url = "https://hackernews-api-mu.vercel.app/";
    fetch(url)
        .then(response => response.json())
        .then(data => renderHackerNewsData(data))
        .catch(error => console.error("Error fetching TechCrunch data:", error));
}

function renderHackerNewsData(data) {
    const hackerNewsList = document.getElementById("hackernews-list");
    // cleaning previous data!
    hackerNewsList.innerHTML = ""; 
    
    for(const [key, value] of Object.entries(data)){
        const listItem = document.createElement("li");
        const anchor = document.createElement("a");
        anchor.textContent = key;
        anchor.href = value;
        anchor.target = "_blank"
        listItem.appendChild(anchor)    
        hackerNewsList.appendChild(listItem)
    }
}