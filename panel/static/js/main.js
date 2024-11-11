async function ShellForm(){
    const id = document.getElementById("bot_id").value;
    const command = document.getElementById("command").value;

    const response = await fetch(`/api/bot/${id}`, {
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            command: command
        })
    });

    const result = await response.json();
    document.getElementById("result").textContent = JSON.stringify(result, null, 2);
}