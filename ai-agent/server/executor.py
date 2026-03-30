from tools import *
from agent import decide_action

def run_agent(prompt):
    decision = decide_action(prompt)

    if decision["action"] == "create_file":
        return create_file(decision["path"], decision["content"])

    if decision["action"] == "run_command":
        return run_command(decision["command"])

    return "No action taken"