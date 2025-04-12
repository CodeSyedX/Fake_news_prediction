// === CONFIG ===
const API_URL = "http://127.0.0.1:8000/predict"; // Replace with your deployed API

// === FAKE NEWS DETECTION ===
async function detectFakeNews(text) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await response.json();
    return data.prediction === "FAKE";
  } catch (error) {
    console.error("Error calling fake news API:", error);
    return false;
  }
}

// === SCAN POSTS ===
async function scanPage() {
  const elements = document.querySelectorAll("p, h1, h2, h3, span"); // Add or remove tags based on your needs

  for (const el of elements) {
    const text = el.innerText;
    if (text && text.length > 20 && !el.classList.contains("flagged-fake-news")) {
      const isFake = await detectFakeNews(text);
      if (isFake) {
        el.style.border = "2px solid red";
        el.style.backgroundColor = "#ffdddd";
        el.title = "⚠️ Possibly Fake News Detected!";
        el.classList.add("flagged-fake-news");
      }
    }
  }
}

// Run when content loads
scanPage();
