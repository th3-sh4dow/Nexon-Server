# ========== IMPORTS ==========
from dotenv import dotenv_values
from rich import print
from groq import Groq
import os

# ========== ENVIRONMENT ==========
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey") or os.getenv("GROQ_API_KEY")
client = Groq(api_key=GroqAPIKey)

Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Jarvis")

SystemChatBot = [
    {
        "role": "system",
        "content": f"Hello, I am {Username}, You're a command decision agent. You do not execute commands — you only translate user input into structured command format."
    }
]

messages = []

# ========== COMMAND INTERPRETER ==========

def TranslateCommand(command: str) -> dict:
    """
    Translates user input into a structured command dictionary for the client.
    """
    cmd = command.lower().strip()

    if cmd.startswith("open "):
        app = cmd.removeprefix("open ").strip()
        return {
            "response": f"Opening {app.capitalize()}",
            "device_action": {
                "target": "android" if app in ["whatsapp", "youtube", "gmail", "chrome"] else "pc",
                "command": f"open {app}"
            }
        }

    elif cmd.startswith("close "):
        return {
            "response": f"Closing {cmd.removeprefix('close ').strip()} on PC.",
            "device_action": {
                "target": "pc",
                "command": cmd
            }
        }

    elif cmd.startswith("play "):
        return {
            "response": "Playing on YouTube.",
            "device_action": {
                "target": "pc",
                "command": cmd
            }
        }

    elif cmd.startswith("google search "):
        return {
            "response": "Searching Google...",
            "device_action": {
                "target": "pc",
                "command": cmd
            }
        }

    elif cmd.startswith("youtube search "):
        return {
            "response": "Searching YouTube...",
            "device_action": {
                "target": "pc",
                "command": cmd
            }
        }

    elif cmd.startswith("system "):
        return {
            "response": "System command queued.",
            "device_action": {
                "target": "pc",
                "command": cmd
            }
        }

    elif cmd.startswith("content "):
        return {
            "response": "Generating content on device.",
            "device_action": {
                "target": "pc",
                "command": cmd
            }
        }

    else:
        return {
            "response": f"Sorry, I don't recognize this command: {cmd}",
            "device_action": None
        }

# ========== (Optional) TEST MODE ==========
if __name__ == "__main__":
    while True:
        user_input = input("Enter command: ")
        result = TranslateCommand(user_input)
        print(result)
