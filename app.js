const form = document.getElementById('feedbackForm');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const issue = document.getElementById('issue').value;

    const response = await fetch('http://127.0.0.1:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, issue }),
    });

    const result = await response.json();
    alert(result.message);
    form.reset();
});
