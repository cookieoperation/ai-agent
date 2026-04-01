from tools import *
from agent import decide_action


def run_agent(prompt):
    decision = decide_action(prompt)

    try:
        if decision["action"] == "create_file":
            return create_file(decision["path"], decision["content"])

        if decision["action"] == "run_command":
            return run_command(decision["command"])
    except (OSError, ValueError) as exc:
        return f"Error: {exc}"

    return decision.get("message", "No action taken")
