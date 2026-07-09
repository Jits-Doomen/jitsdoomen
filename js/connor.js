async function askConnor() {
    const inputField = document.getElementById("connor-query");
    const terminal = document.getElementById("terminal");
    const query = inputField.value.trim();

    if (!query) return;

    const userDiv = document.createElement("div");
    userDiv.className = "message user-msg";
    userDiv.innerText = `You: ${query}`;
    terminal.appendChild(userDiv);

    inputField.value = "";
    terminal.scrollTop = terminal.scrollHeight;

    const loadingDiv = document.createElement("div");
    loadingDiv.className = "message connor-msg";
    loadingDiv.innerText = "Connor: Processing metrics...";
    terminal.appendChild(loadingDiv);
    terminal.scrollTop = terminal.scrollHeight;

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query }),
        });

        if (!response.ok) {
            throw new Error(`Server returned status ${response.status}`);
        }

        const data = await response.json();

        loadingDiv.innerText = `Connor: ${data.response}`;

    } catch (error) {
        loadingDiv.innerText = "Connor: CORE FAULT INTERCEPTED. Unable to sync with processing array.";
        console.error("API Linkage Error:", error);
    }

    terminal.scrollTop = terminal.scrollHeight;
}