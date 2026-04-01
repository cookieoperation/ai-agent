def decide_action(prompt):
    normalized = prompt.strip().lower()

    if not normalized:
        return {
            "action": "unknown",
            "message": "Please enter a prompt. Try 'list files' or 'run ls'.",
        }

    if "create" in normalized and "file" in normalized:
        return {
            "action": "create_file",
            "path": "hello.py",
            "content": "print('Hello world')",
        }

    if any(keyword in normalized for keyword in ("list files", "show files", "files in")):
        return {
            "action": "run_command",
            "command": "ls",
        }

    for prefix in ("run ", "exec ", "execute "):
        if normalized.startswith(prefix):
            command = prompt.strip()[len(prefix):].strip()
            if command:
                return {
                    "action": "run_command",
                    "command": command,
                }

    if normalized in {"ls", "pwd", "whoami"}:
        return {
            "action": "run_command",
            "command": normalized,
        }

    return {
        "action": "unknown",
        "message": "I couldn't determine an action. Try 'list files', 'create file', or 'run <command>'.",
    }
