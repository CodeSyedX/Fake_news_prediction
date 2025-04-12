document.getElementById("scanBtn").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        func: () => {
          // Re-inject the scan logic
          const script = document.createElement('script');
          script.src = chrome.runtime.getURL('content.js');
          document.documentElement.appendChild(script);
        }
      });
    });
  });
  