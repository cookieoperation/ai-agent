async function runAgent() {
  const prompt = document.getElementById("prompt").value;

  const res = await fetch("/run", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ prompt })
  });

  const data = await res.json();
  document.getElementById("output").textContent = data.result;
}