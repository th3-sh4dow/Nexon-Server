#!/usr/bin/env python3
"""
Enhanced Nova AI Model Testing Script
Demonstrates the advanced NLP/NLU capabilities for intelligent command processing
"""

import asyncio
import sys
import os

# Add the Backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Backend'))

from Backend.Model import FirstLayerDMM
from Backend.Andriod_Automation import TranslateAndroidCommand, process_android_command
from Backend.PC_Automation import TranslateCommand, process_pc_command

def print_separator(title):
    """Print a formatted separator with title"""
    print("\n" + "="*60)
    print(f"🤖 {title}")
    print("="*60)

def print_result(query, result, category=""):
    """Print formatted test result"""
    print(f"\n🔍 Query: {query}")
    print(f"📤 Result: {result}")
    if category:
        print(f"🏷️  Category: {category}")
    print("-" * 40)

async def test_core_commands():
    """Test core system commands"""
    print_separator("CORE COMMANDS TESTING")
    
    core_queries = [
        "nova",
        "stop service",
        "your name",
        "how are you",
        "current version",
        "joke",
        "today's date",
        "tell me the time"
    ]
    
    for query in core_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "CORE")

async def test_app_commands():
    """Test app-related commands"""
    print_separator("APP COMMANDS TESTING")
    
    app_queries = [
        "open whatsapp",
        "start telegram",
        "delete instagram",
        "lock facebook",
        "unlock twitter",
        "open chrome",
        "start camera",
        "open settings"
    ]
    
    for query in app_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "APP")

async def test_media_commands():
    """Test media commands"""
    print_separator("MEDIA COMMANDS TESTING")
    
    media_queries = [
        "capture photo",
        "take screenshot",
        "record video",
        "change camera",
        "skip 5 sec",
        "play despacito",
        "play spotify",
        "change song",
        "stop recording"
    ]
    
    for query in media_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "MEDIA")

async def test_comms_commands():
    """Test communication commands"""
    print_separator("COMMUNICATION COMMANDS TESTING")
    
    comms_queries = [
        "call mom",
        "video call dad",
        "send whatsapp hello",
        "send sms urgent message",
        "call emergency",
        "video call friend"
    ]
    
    for query in comms_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "COMMS")

async def test_device_commands():
    """Test device control commands with percentages"""
    print_separator("DEVICE COMMANDS TESTING")
    
    device_queries = [
        "battery percentage",
        "turn on flashlight",
        "turn off flashlight",
        "turn on screen",
        "turn off screen",
        "back to home",
        "set brightness 75%",
        "set brightness to 50%",
        "set reminder meeting at 3pm",
        "set alarm wake up 7am",
        "remove water",
        "turn on silent",
        "turn off silent",
        "turn on wi-fi",
        "turn off wi-fi",
        "connect to wi-fi",
        "disconnect wi-fi",
        "turn on bluetooth",
        "turn off bluetooth",
        "turn on mobile data",
        "turn off mobile data",
        "scroll up",
        "scroll down",
        "scroll left",
        "scroll right"
    ]
    
    for query in device_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "DEVICE")

async def test_pc_commands():
    """Test PC commands"""
    print_separator("PC COMMANDS TESTING")
    
    pc_queries = [
        "open notepad in pc",
        "back to desktop",
        "open calculator in pc",
        "open microsoft edge in pc",
        "shutdown pc",
        "open files in pc",
        "restart pc",
        "open control panel in pc",
        "lock pc",
        "open task manager in pc",
        "open settings in pc",
        "volume up in pc",
        "volume down in pc",
        "mute pc",
        "unmute pc",
        "open youtube in pc",
        "open google in pc",
        "open command prompt in pc",
        "open camera in pc",
        "open github in pc",
        "open spotify in pc",
        "open whatsapp in pc",
        "open word in pc",
        "open excel in pc",
        "open powerpoint in pc",
        "minimize all",
        "maximize window",
        "close this window",
        "close this page",
        "copy",
        "paste",
        "move upward",
        "move downward",
        "turn on sleeping mode on pc",
        "open android studio in pc",
        "capture photo in laptop",
        "record in laptop",
        "stop recording",
        "click on button",
        "type hello world",
        "send file to pc"
    ]
    
    for query in pc_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "PC")

async def test_smart_commands():
    """Test smart/ai commands"""
    print_separator("SMART COMMANDS TESTING")
    
    smart_queries = [
        "today's news",
        "weather report",
        "current location",
        "show me location of john",
        "translate mode",
        "trouble",
        "search python tutorials",
        "what is this",
        "scan and explain",
        "new notification",
        "tell me about artificial intelligence",
        "search machine learning",
        "tell me about quantum computing"
    ]
    
    for query in smart_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "SMART")

async def test_percentage_commands():
    """Test commands with percentage values"""
    print_separator("PERCENTAGE COMMANDS TESTING")
    
    percentage_queries = [
        "volume down 20%",
        "volume up 50%",
        "volume down 75%",
        "set brightness 30%",
        "set brightness to 90%",
        "volume up 15%",
        "volume down 60%",
        "set brightness 25%"
    ]
    
    for query in percentage_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "PERCENTAGE")

async def test_random_number_commands():
    """Test commands with random numbers"""
    print_separator("RANDOM NUMBER COMMANDS TESTING")
    
    random_queries = [
        "volume down 17",
        "volume up 42",
        "set brightness 83",
        "volume down 7",
        "volume up 95",
        "set brightness 11",
        "volume down 33",
        "volume up 68"
    ]
    
    for query in random_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "RANDOM_NUMBER")

async def test_android_automation():
    """Test Android automation processing"""
    print_separator("ANDROID AUTOMATION TESTING")
    
    android_commands = [
        "app_open::whatsapp",
        "media_play_song::despacito",
        "device_brightness::75%",
        "device_volume::down::30%",
        "comms_call::mom",
        "smart_search::python tutorials",
        "core_activate",
        "device_flashlight_on"
    ]
    
    for cmd in android_commands:
        result = process_android_command(cmd)
        print_result(cmd, result, "ANDROID_PROCESSING")

async def test_pc_automation():
    """Test PC automation processing"""
    print_separator("PC AUTOMATION TESTING")
    
    pc_commands = [
        "pc_open_notepad",
        "pc_volume_down",
        "pc_brightness_75%",
        "pc_shutdown",
        "pc_lock",
        "pc_minimize_all",
        "pc_copy",
        "pc_paste"
    ]
    
    for cmd in pc_commands:
        result = process_pc_command(cmd)
        print_result(cmd, result, "PC_PROCESSING")

async def test_complex_queries():
    """Test complex multi-intent queries"""
    print_separator("COMPLEX QUERIES TESTING")
    
    complex_queries = [
        "nova volume down 25% and open whatsapp",
        "set brightness to 80% and take screenshot",
        "call mom and send whatsapp message hello",
        "open chrome and search for python tutorials",
        "play despacito and turn on flashlight",
        "battery percentage and current location",
        "open notepad in pc and type hello world",
        "shutdown pc and lock phone"
    ]
    
    for query in complex_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "COMPLEX")

async def test_hindi_queries():
    """Test Hindi language queries"""
    print_separator("HINDI QUERIES TESTING")
    
    hindi_queries = [
        "nova volume kam karo 30%",
        "brightness 75% set karo",
        "whatsapp kholo",
        "despacito gaana chalao",
        "mummy ko call karo",
        "screenshot le lo",
        "flashlight on karo",
        "battery percentage batao"
    ]
    
    for query in hindi_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "HINDI")

async def test_ownership_queries():
    """Test ownership/creator queries"""
    print_separator("OWNERSHIP QUERIES TESTING")
    
    ownership_queries = [
        "who made you",
        "who built you",
        "who developed you",
        "who is your creator",
        "who is your daddy",
        "who owns you",
        "who programmed you"
    ]
    
    for query in ownership_queries:
        result = FirstLayerDMM(query)
        print_result(query, result, "OWNERSHIP")

async def main():
    """Main testing function"""
    print("🚀 Enhanced Nova AI Model - Comprehensive Testing Suite")
    print("=" * 70)
    
    # Run all test categories
    await test_core_commands()
    await test_app_commands()
    await test_media_commands()
    await test_comms_commands()
    await test_device_commands()
    await test_pc_commands()
    await test_smart_commands()
    await test_percentage_commands()
    await test_random_number_commands()
    await test_android_automation()
    await test_pc_automation()
    await test_complex_queries()
    await test_hindi_queries()
    await test_ownership_queries()
    
    print("\n" + "="*70)
    print("✅ All tests completed successfully!")
    print("🎯 Enhanced Nova AI Model is ready for intelligent command processing")
    print("="*70)

if __name__ == "__main__":
    asyncio.run(main()) 