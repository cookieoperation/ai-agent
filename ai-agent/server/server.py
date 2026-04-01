from pathlib import Path

from flask import Flask, request, jsonify, send_from_directory
from executor import run_agent

WEB_DIR = Path(__file__).resolve().parent.parent / "web"

app = Flask(__name__, static_folder=str(WEB_DIR), static_url_path="")


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(WEB_DIR, "index.html")


@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify({"error": "Request must include a non-empty 'prompt' string"}), 400

    result = run_agent(prompt)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
