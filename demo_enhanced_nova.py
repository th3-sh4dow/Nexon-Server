#!/usr/bin/env python3
"""
Enhanced Nova AI - Live Demonstration
Shows how the intelligent NLP/NLU system processes user commands
"""

import asyncio
import sys
import os

# Add the Backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Backend'))

from Backend.Model import FirstLayerDMM
from Backend.Andriod_Automation import process_android_command
from Backend.PC_Automation import process_pc_command

def print_header():
    """Print the demo header"""
    print("🤖" + "="*60 + "🤖")
    print("🚀 ENHANCED NOVA AI - INTELLIGENT COMMAND PROCESSING")
    print("🤖" + "="*60 + "🤖")
    print("\n🎯 This demo shows how Nova AI understands and processes:")
    print("   • Core system commands")
    print("   • App management commands")
    print("   • Media control commands")
    print("   • Device control with percentages")
    print("   • PC automation commands")
    print("   • Smart AI commands")
    print("   • Complex multi-intent queries")
    print("   • Hindi language support")
    print("\n💡 Try commands like:")
    print("   • 'nova volume down 30%'")
    print("   • 'set brightness to 75%'")
    print("   • 'open whatsapp and call mom'")
    print("   • 'play despacito and take screenshot'")
    print("   • 'shutdown pc and lock phone'")
    print("\n" + "="*62)

def print_command_result(query, result):
    """Print formatted command result"""
    print(f"\n🔍 User Query: {query}")
    print(f"📤 Nova Response: {result}")
    
    # Show what the client device would receive
    if result and isinstance(result, list):
        for cmd in result:
            if cmd.startswith(('app_', 'media_', 'device_', 'comms_', 'smart_')):
                android_cmd = process_android_command(cmd)
                if android_cmd:
                    print(f"📱 Android Command: {android_cmd}")
            elif cmd.startswith('pc_'):
                pc_cmd = process_pc_command(cmd)
                if pc_cmd:
                    print(f"🖥️  PC Command: {pc_cmd}")
            elif cmd.startswith('general '):
                print(f"💬 General Response: {cmd}")
    
    print("-" * 50)

async def interactive_demo():
    """Interactive demonstration mode"""
    print_header()
    
    print("\n🎮 INTERACTIVE MODE")
    print("Type 'exit' to quit, 'help' for examples, 'demo' for auto-demo")
    
    while True:
        try:
            user_input = input("\n👤 You → ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("👋 Goodbye! Thanks for trying Enhanced Nova AI!")
                break
            
            elif user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'demo':
                await auto_demo()
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
    print("   • nova")
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
    print("   • nova volume kam karo 30%")
    print("   • whatsapp kholo")
    print("   • mummy ko call karo")
    print("   • screenshot le lo")
    
    print("\n🔄 COMPLEX QUERIES:")
    print("   • nova volume down 25% and open whatsapp")
    print("   • set brightness to 80% and take screenshot")
    print("   • call mom and send whatsapp message hello")
    print("   • shutdown pc and lock phone")

async def auto_demo():
    """Automatic demonstration with predefined examples"""
    print("\n🎬 AUTO DEMONSTRATION MODE")
    print("=" * 50)
    
    demo_queries = [
        "nova",
        "volume down 30%",
        "set brightness to 75%",
        "open whatsapp",
        "call mom",
        "play despacito",
        "take screenshot",
        "battery percentage",
        "shutdown pc",
        "search python tutorials",
        "nova volume down 25% and open whatsapp",
        "set brightness to 80% and take screenshot",
        "who made you"
    ]
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n🎯 Demo {i}/{len(demo_queries)}")
        result = FirstLayerDMM(query)
        print_command_result(query, result)
        
        if i < len(demo_queries):
            print("\n⏳ Press Enter for next demo...")
            input()

async def main():
    """Main function"""
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        await auto_demo()
    else:
        await interactive_demo()

if __name__ == "__main__":
    asyncio.run(main()) 