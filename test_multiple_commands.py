#!/usr/bin/env python3
"""
Test Multiple Commands Processing
"""

import re

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
    
    # Handle "play song name [song]" format
    if "play song name" in text_lower:
        song_start = text_lower.find("play song name") + len("play song name")
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
    """Extract app name from text"""
    common_apps = [
        "whatsapp", "telegram", "instagram", "facebook", "twitter", "youtube", 
        "spotify", "chrome", "gmail", "camera", "gallery", "settings", "calculator"
    ]
    
    text_lower = text.lower()
    for app in common_apps:
        if app in text_lower:
            return app
    return None

def process_command(cmd):
    """Process individual command"""
    cmd_lower = cmd.lower()
    
    # Core commands
    if "nexon" in cmd_lower:
        return "core_activate"
    
    # App commands
    if "open" in cmd_lower:
        app = extract_app_name(cmd)
        if app:
            return f"app_open::{app}"
    
    # Media commands
    if "play" in cmd_lower:
        song = extract_song_name(cmd)
        if song:
            return f"media_play_song::{song}"
    
    # Volume commands
    if "set volume into" in cmd_lower or "set volum into" in cmd_lower or "set voloume into" in cmd_lower:
        percentage = extract_percentage(cmd)
        number = extract_number(cmd)
        if percentage:
            return f"device_volume::{percentage}%"
        elif number:
            return f"device_volume::{number}%"
    
    return None

def process_multiple_commands(prompt):
    """Process multiple commands in a single query"""
    print(f"Processing: {prompt}")
    
    # Split the prompt into multiple commands
    individual_commands = split_multiple_commands(prompt)
    print(f"Split commands: {individual_commands}")
    
    all_results = []
    
    for cmd in individual_commands:
        if cmd.strip():
            result = process_command(cmd.strip())
            if result:
                all_results.append(result)
                print(f"Command '{cmd.strip()}' → {result}")
            else:
                print(f"Command '{cmd.strip()}' → No match")
    
    return all_results

# Test the system
test_queries = [
    "nexon open whatsapp and play a song name ham mere safer and set volum into 90%",
    "nexon open whatsapp play song name pal pal and set voloume into 50%",
    "open whatsapp and call mom",
    "set brightness to 75% and take screenshot"
]

print("🤖 Testing Multiple Command Processing")
print("=" * 50)

for query in test_queries:
    print(f"\n🔍 Query: {query}")
    results = process_multiple_commands(query)
    print(f"📤 Results: {results}")
    print("-" * 30) 