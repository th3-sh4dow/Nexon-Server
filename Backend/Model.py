import cohere
from rich import print
from dotenv import dotenv_values
import random
import re
import spacy
from fuzzywuzzy import process
from datetime import datetime
import json

# Load environment variables
env_vars = dotenv_values(".env")
CohereAPIKey = env_vars.get("CohereAPIKey")

co = cohere.Client()  # Will automatically use CO_API_KEY

# Load NLP model for better understanding
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

# ==================== COMMAND CATEGORIES & PATTERNS ====================

# Core Commands
CORE_COMMANDS = {
    "nexon": "core_activate",
    "stop service": "core_stop_service", 
    "your name": "core_name",
    "how are you": "core_health",
    "current version": "core_version",
    "joke": "core_joke",
    "today's date": "core_date",
    "tell me the time": "core_time"
}

# App Commands
APP_COMMANDS = {
    "open": "app_open",
    "start": "app_start", 
    "delete": "app_delete",
    "lock": "app_lock",
    "unlock": "app_unlock"
}

# Media Commands
MEDIA_COMMANDS = {
    "capture photo": "media_capture_photo",
    "take screenshot": "media_screenshot",
    "record video": "media_record_video",
    "change camera": "media_change_camera",
    "skip 5 sec": "media_skip_5sec",
    "play song": "media_play_song",
    "play": "media_play_song",
    "play spotify": "media_play_spotify",
    "change song": "media_change_song",
    "stop recording": "media_stop_recording"
}

# Communication Commands
COMMS_COMMANDS = {
    "call": "comms_call",
    "video call": "comms_video_call",
    "send whatsapp": "comms_whatsapp",
    "send sms": "comms_sms"
}

# Device Commands with percentage/level support
DEVICE_COMMANDS = {
    "battery percentage": "device_battery",
    "turn on flashlight": "device_flashlight_on",
    "turn off flashlight": "device_flashlight_off",
    "turn on screen": "device_screen_on",
    "turn off screen": "device_screen_off",
    "back to home": "device_home",
    "set brightness": "device_brightness",
    "set reminder": "device_reminder",
    "set alarm": "device_alarm",
    "remove water": "device_water_ejection",
    "turn on silent": "device_silent_on",
    "turn off silent": "device_silent_off",
    "turn on wi-fi": "device_wifi_on",
    "turn off wi-fi": "device_wifi_off",
    "connect to wi-fi": "device_wifi_connect",
    "disconnect wi-fi": "device_wifi_disconnect",
    "turn on bluetooth": "device_bluetooth_on",
    "turn off bluetooth": "device_bluetooth_off",
    "turn on mobile data": "device_mobile_data_on",
    "turn off mobile data": "device_mobile_data_off",
    "scroll up": "device_scroll_up",
    "scroll down": "device_scroll_down",
    "scroll left": "device_scroll_left",
    "scroll right": "device_scroll_right"
}

# PC Commands
PC_COMMANDS = {
    "open notepad in pc": "pc_open_notepad",
    "back to desktop": "pc_desktop",
    "open calculator in pc": "pc_open_calculator",
    "open microsoft edge in pc": "pc_open_edge",
    "shutdown pc": "pc_shutdown",
    "open files in pc": "pc_open_files",
    "restart pc": "pc_restart",
    "open control panel in pc": "pc_open_control_panel",
    "lock pc": "pc_lock",
    "open task manager in pc": "pc_open_task_manager",
    "open settings in pc": "pc_open_settings",
    "volume up in pc": "pc_volume_up",
    "volume down in pc": "pc_volume_down",
    "mute pc": "pc_mute",
    "unmute pc": "pc_unmute",
    "open youtube in pc": "pc_open_youtube",
    "open google in pc": "pc_open_google",
    "open command prompt in pc": "pc_open_cmd",
    "open camera in pc": "pc_open_camera",
    "open github in pc": "pc_open_github",
    "open spotify in pc": "pc_open_spotify",
    "open whatsapp in pc": "pc_open_whatsapp",
    "open word in pc": "pc_open_word",
    "open excel in pc": "pc_open_excel",
    "open powerpoint in pc": "pc_open_powerpoint",
    "minimize all": "pc_minimize_all",
    "maximize window": "pc_maximize_window",
    "close this window": "pc_close_window",
    "close this page": "pc_close_page",
    "copy": "pc_copy",
    "paste": "pc_paste",
    "move upward": "pc_scroll_up",
    "move downward": "pc_scroll_down",
    "turn on sleeping mode on pc": "pc_sleep",
    "open android studio in pc": "pc_open_android_studio",
    "capture photo in laptop": "pc_capture_photo",
    "record in laptop": "pc_record",
    "stop recording": "pc_stop_recording",
    "click on": "pc_click",
    "type": "pc_type",
    "send file to pc": "pc_send_file"
}

# Smart Commands
SMART_COMMANDS = {
    "today's news": "smart_news",
    "weather report": "smart_weather",
    "current location": "smart_location",
    "show me location of": "smart_track_location",
    "translate mode": "smart_translate",
    "trouble": "smart_emergency",
    "search": "smart_search",
    "what is this": "smart_object_detection",
    "scan and explain": "smart_scan_text",
    "new notification": "smart_read_notification",
    "tell me about": "smart_wikipedia"
}

# ==================== UTILITY FUNCTIONS ====================

def extract_percentage(text):
    """Extract percentage values from text"""
    percentage_pattern = r'(\d+)\s*%'
    matches = re.findall(percentage_pattern, text)
    return int(matches[0]) if matches else None

def extract_number(text):
    """Extract any number from text"""
    number_pattern = r'(\d+)'
    matches = re.findall(number_pattern, text)
    return int(matches[0]) if matches else None

def extract_app_name(text):
    """Extract app name from text using fuzzy matching"""
    common_apps = [
        "whatsapp", "telegram", "instagram", "facebook", "twitter", "youtube", 
        "spotify", "chrome", "gmail", "camera", "gallery", "settings", "calculator",
        "notepad", "word", "excel", "powerpoint", "edge", "github", "android studio"
    ]
    
    text_lower = text.lower()
    best_match = process.extractOne(text_lower, common_apps)
    return best_match[0] if best_match and best_match[1] > 70 else None

def extract_contact_name(text):
    """Extract contact name from text"""
    # Remove common prefixes
    prefixes = ["call", "video call", "send whatsapp to", "send sms to"]
    for prefix in prefixes:
        if text.lower().startswith(prefix):
            return text[len(prefix):].strip()
    return text.strip()

def extract_song_name(text):
    """Extract song name from text"""
    text_lower = text.lower()
    
    # Handle "play a song name [song]" format
    if "play a song name" in text_lower:
        song_start = text_lower.find("play a song name") + len("play a song name")
        song_text = text[song_start:].strip()
        # Remove any trailing words like "and set volume"
        if " and " in song_text:
            song_text = song_text.split(" and ")[0].strip()
        return song_text
    
    # Handle regular "play [song]" format
    prefixes = ["play", "play song", "play music"]
    for prefix in prefixes:
        if text_lower.startswith(prefix):
            song_text = text[len(prefix):].strip()
            # Remove any trailing words like "and set volume"
            if " and " in song_text:
                song_text = song_text.split(" and ")[0].strip()
            return song_text
    
    return None

def extract_search_query(text):
    """Extract search query from text"""
    prefixes = ["search", "search for", "google search", "youtube search"]
    for prefix in prefixes:
        if text.lower().startswith(prefix):
            return text[len(prefix):].strip()
    return text.strip()

# ==================== INTELLIGENT COMMAND PROCESSING ====================

def process_volume_command(text):
    """Process volume commands with percentage/level support"""
    text_lower = text.lower()
    
    # Handle "set volume into X%" format
    if "set volume into" in text_lower or "set volum into" in text_lower:
        percentage = extract_percentage(text)
        number = extract_number(text)
        
        if percentage:
            return f"device_volume::{percentage}%"
        elif number:
            return f"device_volume::{number}%"
        else:
            return "device_volume::50%"  # Default
    
    # Handle "volume down/up X%" format
    if "volume down" in text_lower or "volume up" in text_lower:
        percentage = extract_percentage(text)
        number = extract_number(text)
        
        if percentage:
            return f"volume::{text_lower.split()[0]}::{percentage}%"
        elif number:
            return f"volume::{text_lower.split()[0]}::{number}%"
        else:
            # Default values
            if "down" in text_lower:
                return "volume::down::20%"
            else:
                return "volume::up::20%"
    
    return None

def process_brightness_command(text):
    """Process brightness commands with percentage support"""
    text_lower = text.lower()
    
    if "brightness" in text_lower:
        percentage = extract_percentage(text)
        number = extract_number(text)
        
        if percentage:
            return f"brightness::{percentage}%"
        elif number:
            return f"brightness::{number}%"
        else:
            return "brightness::50%"  # Default
    
    return None

def process_app_command(text):
    """Process app-related commands"""
    text_lower = text.lower()
    
    for action, command_type in APP_COMMANDS.items():
        if action in text_lower:
            app_name = extract_app_name(text)
            if app_name:
                return f"{command_type}::{app_name}"
    
    return None

def process_media_command(text):
    """Process media commands"""
    text_lower = text.lower()
    
    for action, command_type in MEDIA_COMMANDS.items():
        if action in text_lower:
            if "play" in action:
                song_name = extract_song_name(text)
                return f"{command_type}::{song_name}" if song_name else f"{command_type}"
            else:
                return f"{command_type}"
    
    return None

def process_comms_command(text):
    """Process communication commands"""
    text_lower = text.lower()
    
    for action, command_type in COMMS_COMMANDS.items():
        if action in text_lower:
            contact = extract_contact_name(text)
            if contact:
                return f"{command_type}::{contact}"
    
    return None

def process_device_command(text):
    """Process device commands with smart parameter extraction"""
    text_lower = text.lower()
    
    # Handle volume commands
    volume_cmd = process_volume_command(text)
    if volume_cmd:
        return volume_cmd
    
    # Handle brightness commands
    brightness_cmd = process_brightness_command(text)
    if brightness_cmd:
        return brightness_cmd
    
    # Handle other device commands
    for action, command_type in DEVICE_COMMANDS.items():
        if action in text_lower:
            return f"{command_type}"
    
    return None

def process_pc_command(text):
    """Process PC commands"""
    text_lower = text.lower()
    
    for action, command_type in PC_COMMANDS.items():
        if action in text_lower:
            return f"{command_type}"
    
    return None

def process_smart_command(text):
    """Process smart commands"""
    text_lower = text.lower()
    
    for action, command_type in SMART_COMMANDS.items():
        if action in text_lower:
            if "search" in action:
                query = extract_search_query(text)
                return f"{command_type}::{query}" if query else f"{command_type}"
            elif "tell me about" in action:
                topic = text_lower.replace("tell me about", "").strip()
                return f"{command_type}::{topic}" if topic else f"{command_type}"
            else:
                return f"{command_type}"
    
    return None

def process_core_command(text):
    """Process core commands"""
    text_lower = text.lower()
    
    for action, command_type in CORE_COMMANDS.items():
        if action in text_lower:
            return f"{command_type}"
    
    return None

# ==================== MULTIPLE COMMAND PROCESSING ====================

def split_multiple_commands(text):
    """Split text into multiple commands using conjunctions"""
    # Common conjunctions that separate commands
    conjunctions = [" and ", " then ", " also ", " plus ", " & ", " + "]
    
    commands = [text]
    
    for conjunction in conjunctions:
        new_commands = []
        for cmd in commands:
            if conjunction in cmd.lower():
                parts = cmd.split(conjunction)
                new_commands.extend([part.strip() for part in parts if part.strip()])
            else:
                new_commands.append(cmd)
        commands = new_commands
    
    return commands

def extract_structured_command(prompt: str):
    """Extract structured commands using NLP patterns"""
    
    # Try each command category
    command_processors = [
        process_core_command,
        process_app_command,
        process_media_command,
        process_comms_command,
        process_device_command,
        process_pc_command,
        process_smart_command
    ]
    
    for processor in command_processors:
        result = processor(prompt)
        if result:
            print(f"[DEBUG] Extracted command: {result}")
            return result
    
    return None

def extract_all_structured_commands(prompt: str):
    """Extract ALL structured commands from a prompt"""
    
    # Try each command category
    command_processors = [
        process_core_command,
        process_app_command,
        process_media_command,
        process_comms_command,
        process_device_command,
        process_pc_command,
        process_smart_command
    ]
    
    all_results = []
    
    for processor in command_processors:
        result = processor(prompt)
        if result:
            print(f"[DEBUG] Extracted command: {result}")
            all_results.append(result)
    
    return all_results

def process_multiple_commands(prompt: str):
    """Process multiple commands in a single query"""
    # Split the prompt into multiple commands
    individual_commands = split_multiple_commands(prompt)
    
    all_results = []
    
    for cmd in individual_commands:
        if cmd.strip():
            # Try to extract all possible commands from this part
            results = extract_all_structured_commands(cmd.strip())
            if results:
                all_results.extend(results)
            else:
                # If no structured command found, treat as general
                all_results.append(f"general {cmd.strip()}")
    
    # Only return multiple results if we found more than one command
    if len(all_results) > 1:
        return all_results
    elif len(all_results) == 1:
        return all_results
    else:
        return None

# ==================== MAIN INTELLIGENT PROCESSING FUNCTION ====================

def FirstLayerDMM(prompt: str = "test"):
    """
    Advanced Decision Making Model with NLP/NLU capabilities
    Handles multiple commands in a single query
    """
    print(f"[DEBUG] Processing query: {prompt}")
    
    # Check for ownership queries first
    if is_ownership_query(prompt):
        return handle_ownership_query(prompt)
    
    # Process multiple commands
    multiple_results = process_multiple_commands(prompt)
    
    if multiple_results:
        print(f"[DEBUG] Multiple commands detected: {multiple_results}")
        return multiple_results
    
    # Fallback to single command processing
    structured_command = extract_structured_command(prompt)
    if structured_command:
        return [structured_command]
    
    # Fallback to Cohere for complex queries
    return fallback_to_cohere(prompt)

def handle_ownership_query(prompt: str):
    """Handle ownership-related queries"""
    ownership_preamble = """
    You are a professional AI assistant designed to explain your own origin in a respectful and intelligent way. 
    If someone asks questions like "who made you", "who built you", "who developed you", or similar, 
    you should respond by naturally describing your creator.

    Here's how you should describe yourself:

    "I was proudly built by Bicky Muduli, also known as Sh4dow. He is a highly skilled software developer, 
    ethical hacker, and cybersecurity expert. He specializes in penetration testing, secure development, 
    OSINT, and automation systems. With a deep passion for technology and self-learning, Bicky created me 
    as part of his mission to integrate artificial intelligence with practical real-world use cases. 
    He believes in innovation, open learning, and empowering the cybersecurity community."

    If the question is asked in an informal or funny way (like "who's your daddy?"), respond cleverly 
    but still honor Bicky Muduli.
    """
    
    stream = co.chat_stream(
        model='command-r-plus',
        message=prompt,
        temperature=0.7,
        chat_history=[],
        prompt_truncation='OFF',
        connectors=[],
        preamble=ownership_preamble
    )
    
    response = ""
    for event in stream:
        if event.event_type == "text-generation":
            response += event.text
    
    return [f"general {response.strip()}"]

def fallback_to_cohere(prompt: str):
    """Fallback to Cohere for complex queries"""
    
    # Enhanced preamble with all command categories
    enhanced_preamble = """
    You are an advanced AI assistant that understands user intent and translates it into structured commands.
    
    Available command categories:
    
    CORE: nexon, stop service, your name, how are you, current version, joke, today's date, tell me the time
    APP: open [app], start [app], delete [app], lock [app], unlock [app]
    MEDIA: capture photo, take screenshot, record video, change camera, skip 5 sec, play song, play spotify, change song, stop recording
    COMMS: call [contact], video call [contact], send whatsapp [message], send sms [message]
    DEVICE: battery percentage, turn on/off flashlight, turn on/off screen, back to home, set brightness [level], set reminder/alarm, remove water, turn on/off silent/wifi/bluetooth/mobile data, scroll up/down/left/right
    PC: open [app] in pc, shutdown pc, restart pc, lock pc, volume up/down in pc, mute/unmute pc, minimize all, maximize window, close window/page, copy/paste, move upward/downward, turn on sleeping mode, capture photo in laptop, record in laptop, click on, type, send file to pc
    SMART: today's news, weather report, current location, show me location of [person], translate mode, trouble, search [query], what is this, scan and explain, new notification, tell me about [topic]
    
    For volume/brightness commands, extract percentage values (e.g., "volume down 20%" → "volume::down::20%")
    For app commands, extract app names (e.g., "open whatsapp" → "app_open::whatsapp")
    For media commands, extract song names (e.g., "play despacito" → "media_play_song::despacito")
    For search commands, extract search queries (e.g., "search python tutorials" → "smart_search::python tutorials")
    
    Respond with the most appropriate command format. If multiple actions are requested, separate them with commas.
    """
    
    messages = [{"role": "user", "content": f"{prompt}"}]
    stream = co.chat_stream(
        model='command-r-plus',
        message=prompt,
        temperature=0.7,
        chat_history=[],
        prompt_truncation='OFF',
        connectors=[],
        preamble=enhanced_preamble
    )
    
    response = ""
    for event in stream:
        if event.event_type == "text-generation":
            response += event.text
    
    # Parse response into commands
    commands = response.replace("\n", "").split(",")
    commands = [cmd.strip() for cmd in commands if cmd.strip()]
    
    if not commands:
        return ["general " + prompt]
    
    return commands

def is_ownership_query(prompt: str):
    """Check if query is about ownership/creator"""
    ownership_triggers = [
        "who built you", "who made you", "who developed you", "who is your developer", "who created you",
        "who is your creator", "who programmed you", "who is your founder", "who owns you", "your maker",
        "who is the person behind you", "who is your builder", "developer of you", "coded you", "your owner",
        "your father", "who is your father", "who is your daddy", "your papa", "papa", "daddy"
    ]
    
    prompt_lower = prompt.lower()
    return any(trigger in prompt_lower for trigger in ownership_triggers)

# ==================== TESTING ====================

if __name__ == "__main__":
    print("🤖 Enhanced Nexon AI Model - Testing Mode")
    print("=" * 50)
    
    test_queries = [
        "nexon",
        "volume down 30%",
        "set brightness to 75%",
        "open whatsapp",
        "search python tutorials",
        "who made you",
        # Multiple commands
        "nexon open whatsapp and play a song name ham mere safer and set volum into 90%",
        "call mom and send whatsapp message hello",
        "set brightness to 80% and take screenshot",
        "shutdown pc and lock phone"
    ]
    
    for query in test_queries:
        print(f"\n🔍 Query: {query}")
        result = FirstLayerDMM(query)
        print(f"📤 Result: {result}")
        print("-" * 30)
