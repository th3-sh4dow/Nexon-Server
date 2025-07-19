# ========== IMPORTS ==========
from dotenv import dotenv_values
from rich import print
from groq import Groq
import os
import re

# ========== ENVIRONMENT ==========
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey") or os.getenv("GROQ_API_KEY")
client = Groq(api_key=GroqAPIKey)

Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Jarvis")

# ========== PC COMMAND MAPPINGS ==========

PC_APP_MAPPINGS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "microsoft edge": "msedge.exe",
    "edge": "msedge.exe",
    "files": "explorer.exe",
    "file explorer": "explorer.exe",
    "control panel": "control.exe",
    "task manager": "taskmgr.exe",
    "settings": "ms-settings:",
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "command prompt": "cmd.exe",
    "cmd": "cmd.exe",
    "camera": "microsoft.windows.camera:",
    "github": "https://github.com",
    "spotify": "spotify.exe",
    "whatsapp": "whatsapp.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "android studio": "studio64.exe"
}

# ========== ENHANCED COMMAND INTERPRETER ==========

def TranslateCommand(command: str) -> dict:
    """
    Enhanced PC command translator that handles intelligent command formats
    """
    if isinstance(command, str):
        commands = [command]
    else:
        commands = command

    processed_commands = []
    
    for cmd in commands:
        cmd_lower = cmd.lower().strip()
        processed_cmd = process_pc_command(cmd_lower)
        if processed_cmd:
            processed_commands.append(processed_cmd)
            print(f"[PC] Processed command: {processed_cmd}")

    return {
        "response": f"Executing {len(processed_commands)} PC command(s)",
        "device_action": {
            "target": "pc",
            "commands": processed_commands
        }
    }

def process_pc_command(cmd):
    """Process individual PC command with intelligent parsing"""
    
    # PC Commands
    if cmd.startswith("pc_"):
        return handle_pc_command(cmd)
    
    # Legacy format support
    else:
        return handle_legacy_pc_command(cmd)

def handle_pc_command(cmd):
    """Handle PC-specific commands"""
    
    # App opening commands
    if "open_" in cmd and "pc" in cmd:
        app_name = extract_app_name_from_pc_command(cmd)
        if app_name:
            return f"pc::open::{app_name}"
    
    # System control commands
    elif "shutdown" in cmd:
        return "pc::shutdown"
    elif "restart" in cmd:
        return "pc::restart"
    elif "lock" in cmd:
        return "pc::lock"
    elif "sleep" in cmd:
        return "pc::sleep"
    elif "desktop" in cmd:
        return "pc::desktop"
    
    # Volume control commands
    elif "volume_up" in cmd:
        return "pc::volume_up"
    elif "volume_down" in cmd:
        return "pc::volume_down"
    elif "mute" in cmd:
        return "pc::mute"
    elif "unmute" in cmd:
        return "pc::unmute"
    
    # Window management commands
    elif "minimize_all" in cmd:
        return "pc::minimize_all"
    elif "maximize_window" in cmd:
        return "pc::maximize_window"
    elif "close_window" in cmd:
        return "pc::close_window"
    elif "close_page" in cmd:
        return "pc::close_page"
    
    # Clipboard commands
    elif "copy" in cmd:
        return "pc::copy"
    elif "paste" in cmd:
        return "pc::paste"
    
    # Navigation commands
    elif "scroll_up" in cmd or "move_upward" in cmd:
        return "pc::scroll_up"
    elif "scroll_down" in cmd or "move_downward" in cmd:
        return "pc::scroll_down"
    
    # Media commands
    elif "capture_photo" in cmd:
        return "pc::capture_photo"
    elif "record" in cmd:
        return "pc::record"
    elif "stop_recording" in cmd:
        return "pc::stop_recording"
    
    # Input commands
    elif "click" in cmd:
        target = extract_parameter_from_command(cmd)
        return f"pc::click::{target}" if target else "pc::click"
    elif "type" in cmd:
        text = extract_parameter_from_command(cmd)
        return f"pc::type::{text}" if text else "pc::type"
    
    # File transfer
    elif "send_file" in cmd:
        return "pc::send_file"
    
    return None

def handle_legacy_pc_command(cmd):
    """Handle legacy PC command format for backward compatibility"""
    
    if cmd.startswith("open "):
        app = cmd.removeprefix("open ").strip()
        if app in PC_APP_MAPPINGS:
            return f"pc::open::{app}"
        else:
            print(f"[PC OPEN] App '{app}' not supported.")
            return None

    elif cmd.startswith("close "):
        return f"pc::close::{cmd.removeprefix('close ').strip()}"

    elif cmd.startswith("play "):
        return f"pc::play::{cmd.removeprefix('play ').strip()}"

    elif cmd.startswith("google search "):
        query = cmd.removeprefix("google search ").strip()
        return f"pc::search_google::{query}"

    elif cmd.startswith("youtube search "):
        query = cmd.removeprefix("youtube search ").strip()
        return f"pc::search_youtube::{query}"

    elif cmd.startswith("system "):
        system_cmd = cmd.removeprefix("system ").strip()
        return f"pc::system::{system_cmd}"

    elif cmd.startswith("content "):
        content_desc = cmd.removeprefix("content ").strip()
        return f"pc::content::{content_desc}"

    else:
        print(f"[PC] Command not handled: {cmd}")
        return None

def extract_app_name_from_pc_command(cmd):
    """Extract app name from PC command string"""
    # Remove command prefix and extract app name
    if "open_" in cmd and "pc" in cmd:
        # Extract app name between "open_" and "_pc"
        parts = cmd.split("_")
        for i, part in enumerate(parts):
            if part == "open" and i + 1 < len(parts):
                app_parts = parts[i+1:]
                # Remove "pc" from the end
                if app_parts and app_parts[-1] == "pc":
                    app_parts = app_parts[:-1]
                return "_".join(app_parts)
    return None

def extract_parameter_from_command(cmd):
    """Extract parameter from command string"""
    # Find the last :: and extract everything after it
    if "::" in cmd:
        return cmd.split("::")[-1].strip()
    return None

def extract_percentage_from_command(cmd):
    """Extract percentage value from command string"""
    percentage_pattern = r'(\d+)\s*%'
    matches = re.findall(percentage_pattern, cmd)
    return int(matches[0]) if matches else None

def extract_number_from_command(cmd):
    """Extract any number from command string"""
    number_pattern = r'(\d+)'
    matches = re.findall(number_pattern, cmd)
    return int(matches[0]) if matches else None

# ========== ADVANCED PC COMMAND PROCESSING ==========

def process_volume_command(text):
    """Process volume commands with percentage/level support"""
    text_lower = text.lower()
    
    if "volume down" in text_lower or "volume up" in text_lower:
        percentage = extract_percentage_from_command(text)
        number = extract_number_from_command(text)
        
        if percentage:
            return f"pc::volume::{text_lower.split()[0]}::{percentage}%"
        elif number:
            return f"pc::volume::{text_lower.split()[0]}::{number}%"
        else:
            # Default values
            if "down" in text_lower:
                return "pc::volume::down::20%"
            else:
                return "pc::volume::up::20%"
    
    return None

def process_brightness_command(text):
    """Process brightness commands with percentage support"""
    text_lower = text.lower()
    
    if "brightness" in text_lower:
        percentage = extract_percentage_from_command(text)
        number = extract_number_from_command(text)
        
        if percentage:
            return f"pc::brightness::{percentage}%"
        elif number:
            return f"pc::brightness::{number}%"
        else:
            return "pc::brightness::50%"  # Default
    
    return None

def process_app_opening_command(text):
    """Process app opening commands with fuzzy matching"""
    text_lower = text.lower()
    
    if "open" in text_lower and "pc" in text_lower:
        # Extract app name
        app_name = None
        for app in PC_APP_MAPPINGS.keys():
            if app in text_lower:
                app_name = app
                break
        
        if app_name:
            return f"pc::open::{app_name}"
    
    return None

# ========== COMMAND VALIDATION ==========

def validate_pc_command(cmd):
    """Validate PC command before execution"""
    if not cmd:
        return False, "Empty command"
    
    if cmd.startswith("pc::"):
        return True, "Valid PC command"
    
    return False, "Invalid command format"

# ========== COMMAND EXECUTION SIMULATION ==========

def simulate_pc_execution(cmd):
    """Simulate PC command execution for testing"""
    if cmd.startswith("pc::open::"):
        app = cmd.split("::")[-1]
        return f"Opening {app} on PC"
    elif cmd.startswith("pc::volume::"):
        parts = cmd.split("::")
        direction = parts[2]
        level = parts[3]
        return f"Setting PC volume {direction} to {level}"
    elif cmd.startswith("pc::brightness::"):
        level = cmd.split("::")[-1]
        return f"Setting PC brightness to {level}"
    else:
        return f"Executing PC command: {cmd}"

# ========== TESTING ====================

if __name__ == "__main__":
    print("🖥️ PC Automation Testing")
    print("=" * 40)
    
    test_commands = [
        "pc_open_notepad",
        "pc_volume_down_30%",
        "pc_brightness_75%",
        "open chrome in pc",
        "volume down 20% in pc",
        "shutdown pc",
        "pc_lock",
        "pc_minimize_all"
    ]
    
    for cmd in test_commands:
        print(f"\n🔍 Command: {cmd}")
        result = process_pc_command(cmd)
        print(f"📤 Result: {result}")
        if result:
            simulation = simulate_pc_execution(result)
            print(f"🎯 Simulation: {simulation}")
        print("-" * 30)
