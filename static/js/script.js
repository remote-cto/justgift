document.getElementById("sendButton").addEventListener("click", async () => {
    const userMessage = document.getElementById("userMessage").value;
    const responseContainer = document.getElementById("responseContainer");

    if (!userMessage.trim()) {
        responseContainer.textContent = "Please enter a message.";
        return;
    }

    responseContainer.textContent = "Loading...";
    
    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        if (response.ok) {
            responseContainer.textContent = data.response;
        } else {
            responseContainer.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        responseContainer.textContent = `Error: ${error.message}`;
    }
});
