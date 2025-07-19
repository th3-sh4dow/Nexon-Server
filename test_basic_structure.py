#!/usr/bin/env python3
"""
Basic Structure Test - Enhanced Nova AI
Tests the basic structure and command processing logic
"""

import re
from fuzzywuzzy import process

# ==================== COMMAND CATEGORIES & PATTERNS ====================

# Core Commands
CORE_COMMANDS = {
    "nova": "core_activate",
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

def process_core_command(text):
    """Process core commands"""
    text_lower = text.lower()
    
    for action, command_type in CORE_COMMANDS.items():
        if action in text_lower:
            return f"{command_type}"
    
    return None

def extract_structured_command(prompt: str):
    """Extract structured commands using NLP patterns"""
    
    # Try each command category
    command_processors = [
        process_core_command,
        process_app_command,
        process_device_command
    ]
    
    for processor in command_processors:
        result = processor(prompt)
        if result:
            print(f"[DEBUG] Extracted command: {result}")
            return result
    
    return None

def FirstLayerDMM(prompt: str = "test"):
    """
    Basic Decision Making Model with NLP/NLU capabilities
    """
    print(f"[DEBUG] Processing query: {prompt}")
    
    # Try to extract structured commands first
    structured_command = extract_structured_command(prompt)
    if structured_command:
        return [structured_command]
    
    # Fallback to general response
    return ["general " + prompt]

# ==================== TESTING ====================

def test_commands():
    """Test various command types"""
    print("🤖 Enhanced Nova AI - Basic Structure Test")
    print("=" * 50)
    
    test_queries = [
        # Core commands
        "nova",
        "your name",
        "how are you",
        
        # App commands
        "open whatsapp",
        "start telegram",
        "delete instagram",
        
        # Device commands with percentages
        "volume down 30%",
        "volume up 50%",
        "set brightness 75%",
        "set brightness to 90%",
        "volume down 15",
        "set brightness 25",
        
        # Device commands
        "battery percentage",
        "turn on flashlight",
        "turn off screen",
        "back to home",
        
        # Complex queries
        "nova volume down 25% and open whatsapp",
        "set brightness to 80% and take screenshot",
        
        # Hindi commands
        "nova volume kam karo 30%",
        "whatsapp kholo",
        "mummy ko call karo"
    ]
    
    for query in test_queries:
        print(f"\n🔍 Query: {query}")
        result = FirstLayerDMM(query)
        print(f"📤 Result: {result}")
        print("-" * 30)

if __name__ == "__main__":
    test_commands() 