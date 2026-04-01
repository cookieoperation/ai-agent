from flask import Flask, request, jsonify
from executor import run_agent

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify({"error": "Request must include a non-empty 'prompt' string"}), 400

    result = run_agent(prompt)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
