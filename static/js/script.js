// Fetch quote based on mood and update UI
async function getQuote(mood) {
  const response = await fetch('/get-quote', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mood: mood })
  });

  const data = await response.json();

  const box = document.getElementById('quoteBox');
  const text = document.getElementById('quoteText');
  const author = document.getElementById('quoteAuthor');

  // Fade out, update, fade in
  box.style.opacity = 0;
  setTimeout(() => {
    text.innerText = `"${data.quote}"`;
    author.innerText = data.author ? `— ${data.author}` : '';
    box.style.opacity = 1;
  }, 300);
}

// Dark mode toggle logic
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('themeSwitch');
  const body = document.body;

  toggle.addEventListener('change', () => {
    body.classList.toggle('dark-mode');
  });
});
