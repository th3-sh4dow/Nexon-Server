#!/usr/bin/env python3
"""
Enhanced Nova AI - Concept Demonstration
Shows the intelligent command processing concept without external dependencies
"""

import re

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
    """Extract app name from text using simple matching"""
    common_apps = [
        "whatsapp", "telegram", "instagram", "facebook", "twitter", "youtube", 
        "spotify", "chrome", "gmail", "camera", "gallery", "settings", "calculator",
        "notepad", "word", "excel", "powerpoint", "edge", "github", "android studio"
    ]
    
    text_lower = text.lower()
    for app in common_apps:
        if app in text_lower:
            return app
    return None

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
    prefixes = ["play", "play song", "play music"]
    for prefix in prefixes:
        if text.lower().startswith(prefix):
            return text[len(prefix):].strip()
    return text.strip()

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
    
    media_actions = {
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
    
    for action, command_type in media_actions.items():
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
    
    comms_actions = {
        "call": "comms_call",
        "video call": "comms_video_call",
        "send whatsapp": "comms_whatsapp",
        "send sms": "comms_sms"
    }
    
    for action, command_type in comms_actions.items():
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

def process_multiple_commands(prompt: str):
    """Process multiple commands in a single query"""
    # Split the prompt into multiple commands
    individual_commands = split_multiple_commands(prompt)
    
    all_results = []
    
    for cmd in individual_commands:
        if cmd.strip():
            result = extract_structured_command(cmd.strip())
            if result:
                all_results.append(result)
            else:
                # If no structured command found, treat as general
                all_results.append(f"general {cmd.strip()}")
    
    return all_results

# ==================== MAIN INTELLIGENT PROCESSING FUNCTION ====================

def FirstLayerDMM(prompt: str = "test"):
    """
    Advanced Decision Making Model with NLP/NLU capabilities
    Handles multiple commands in a single query
    """
    print(f"[DEBUG] Processing query: {prompt}")
    
    # Process multiple commands
    multiple_results = process_multiple_commands(prompt)
    
    if multiple_results:
        print(f"[DEBUG] Multiple commands detected: {multiple_results}")
        return multiple_results
    
    # Fallback to single command processing
    structured_command = extract_structured_command(prompt)
    if structured_command:
        return [structured_command]
    
    # Fallback to general response
    return ["general " + prompt]

# ==================== DEMONSTRATION ====================

def print_header():
    """Print the demo header"""
    print("🤖" + "="*60 + "🤖")
    print("🚀 ENHANCED NEXON AI - INTELLIGENT COMMAND PROCESSING")
    print("🤖" + "="*60 + "🤖")
    print("\n🎯 This demo shows how Nexon AI understands and processes:")
    print("   • Core system commands")
    print("   • App management commands")
    print("   • Media control commands")
    print("   • Device control with percentages")
    print("   • PC automation commands")
    print("   • Smart AI commands")
    print("   • Complex multi-intent queries")
    print("   • Hindi language support")
    print("\n💡 Try commands like:")
    print("   • 'nexon volume down 30%'")
    print("   • 'set brightness to 75%'")
    print("   • 'open whatsapp and call mom'")
    print("   • 'play despacito and take screenshot'")
    print("   • 'shutdown pc and lock phone'")
    print("\n" + "="*62)

def print_command_result(query, result):
    """Print formatted command result"""
    print(f"\n🔍 User Query: {query}")
    print(f"📤 Nexon Response: {result}")
    
    # Show what the client device would receive
    if result and isinstance(result, list):
        for cmd in result:
            if cmd.startswith(('app_', 'media_', 'device_', 'comms_', 'smart_')):
                print(f"📱 Android Command: {cmd}")
            elif cmd.startswith('pc_'):
                print(f"🖥️  PC Command: {cmd}")
            elif cmd.startswith('general '):
                print(f"💬 General Response: {cmd}")
    
    print("-" * 50)

def interactive_demo():
    """Interactive demonstration mode"""
    print_header()
    
    print("\n🎮 INTERACTIVE MODE")
    print("Type 'exit' to quit, 'help' for examples, 'demo' for auto-demo")
    
    while True:
        try:
            user_input = input("\n👤 You → ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("👋 Goodbye! Thanks for trying Enhanced Nexon AI!")
                break
            
            elif user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'demo':
                auto_demo()
                continue
            
            elif not user_input:
                continue
            
            # Process the command
            result = FirstLayerDMM(user_input)
            print_command_result(user_input, result)
            
        except KeyboardInterrupt:
            print("\n\n👋 Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'help' for examples.")

def print_help():
    """Print help information"""
    print("\n📚 COMMAND EXAMPLES:")
    print("\n🎯 CORE COMMANDS:")
    print("   • nexon")
    print("   • your name")
    print("   • how are you")
    print("   • current version")
    print("   • joke")
    print("   • today's date")
    print("   • tell me the time")
    
    print("\n📱 APP COMMANDS:")
    print("   • open whatsapp")
    print("   • start telegram")
    print("   • delete instagram")
    print("   • lock facebook")
    print("   • unlock twitter")
    
    print("\n🎵 MEDIA COMMANDS:")
    print("   • capture photo")
    print("   • take screenshot")
    print("   • record video")
    print("   • play despacito")
    print("   • play spotify")
    print("   • change song")
    
    print("\n📞 COMMUNICATION:")
    print("   • call mom")
    print("   • video call dad")
    print("   • send whatsapp hello")
    print("   • send sms urgent")
    
    print("\n⚙️ DEVICE CONTROL:")
    print("   • battery percentage")
    print("   • turn on flashlight")
    print("   • set brightness 75%")
    print("   • volume down 30%")
    print("   • turn on wi-fi")
    print("   • scroll up")
    
    print("\n🖥️ PC COMMANDS:")
    print("   • open notepad in pc")
    print("   • shutdown pc")
    print("   • volume up in pc")
    print("   • minimize all")
    print("   • copy")
    print("   • paste")
    
    print("\n🧠 SMART COMMANDS:")
    print("   • today's news")
    print("   • weather report")
    print("   • current location")
    print("   • search python tutorials")
    print("   • tell me about AI")
    
    print("\n🔢 PERCENTAGE EXAMPLES:")
    print("   • volume down 20%")
    print("   • volume up 50%")
    print("   • set brightness 75%")
    print("   • volume down 15")
    print("   • set brightness 90")
    
    print("\n🇮🇳 HINDI EXAMPLES:")
    print("   • nexon volume kam karo 30%")
    print("   • whatsapp kholo")
    print("   • mummy ko call karo")
    print("   • screenshot le lo")
    
    print("\n🔄 COMPLEX QUERIES:")
    print("   • nexon open whatsapp and play a song name ham mere safer and set volum into 90%")
    print("   • call mom and send whatsapp message hello")
    print("   • set brightness to 80% and take screenshot")
    print("   • shutdown pc and lock phone")

def auto_demo():
    """Automatic demonstration with predefined examples"""
    print("\n🎬 AUTO DEMONSTRATION MODE")
    print("=" * 50)
    
    demo_queries = [
        "nexon",
        "volume down 30%",
        "set brightness to 75%",
        "open whatsapp",
        "call mom",
        "play despacito",
        "take screenshot",
        "battery percentage",
        "shutdown pc",
        "search python tutorials",
        # Multiple commands
        "nexon open whatsapp and play a song name ham mere safer and set volum into 90%",
        "call mom and send whatsapp message hello",
        "set brightness to 80% and take screenshot",
        "shutdown pc and lock phone"
    ]
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n🎯 Demo {i}/{len(demo_queries)}")
        result = FirstLayerDMM(query)
        print_command_result(query, result)
        
        if i < len(demo_queries):
            print("\n⏳ Press Enter for next demo...")
            input()

def main():
    """Main function"""
    interactive_demo()

if __name__ == "__main__":
    main() 