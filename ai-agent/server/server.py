from flask import Flask, request, jsonify
from executor import run_agent

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    result = run_agent(data["prompt"])
    return jsonify({"result": result})

app.run(host="0.0.0.0", port=5000)