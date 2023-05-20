chrome.action.onClicked.addListener(() => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["popup.js"],
  });
});