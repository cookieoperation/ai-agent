async function runAgent() {
  const output = document.getElementById("output");
  const prompt = document.getElementById("prompt").value;

  try {
    const res = await fetch("/run", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt })
    });

    const data = await res.json();
    if (!res.ok) {
      output.textContent = data.error || "Request failed";
      return;
    }

    output.textContent = data.result || "No output";
  } catch (err) {
    output.textContent = `Network error: ${err.message}`;
  }
}
