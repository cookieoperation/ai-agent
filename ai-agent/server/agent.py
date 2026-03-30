def decide_action(prompt):
    prompt = prompt.lower()

    if "create file" in prompt:
        return {
            "action": "create_file",
            "path": "hello.py",
            "content": "print('Hello world')"
        }

    if "list files" in prompt:
        return {
            "action": "run_command",
            "command": "ls"
        }

    return {"action": "none"}