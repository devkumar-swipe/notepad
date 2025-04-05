// Copy Link Function
function copyLink() {
  navigator.clipboard.writeText(window.location.href)
    .then(() => alert("Link copied!"));
}

// Color Picker Logic
const colorPicker = document.getElementById('colorPicker');
const content = document.getElementById('content');
if (colorPicker) {
  colorPicker.addEventListener('input', () => {
    content.style.color = colorPicker.value;
  });
}

// Dark/Light Mode Toggle
function toggleTheme() {
  document.body.classList.toggle("dark");
}

// Auto-Save Every 2 Seconds
setInterval(() => {
  fetch("", {
    method: "POST",
    body: new FormData(document.getElementById("noteForm"))
  }).then(() => {
    document.getElementById("status").textContent = "Saved ✔️";
  });
}, 2000);
