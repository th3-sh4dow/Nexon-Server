# ======================== Android_Automation.py ========================

SUPPORTED_APPS = {
    "whatsapp": "com.whatsapp",
    "telegram": "org.telegram.messenger",
    "instagram": "com.instagram.android",
    "facebook": "com.facebook.katana",
    "twitter": "com.twitter.android",
    "youtube": "com.google.android.youtube",
    "gmail": "com.google.android.gm",
    "settings": "com.android.settings",
    "camera": "com.android.camera",
    "gallery": "com.android.gallery3d",
    "spotify": "com.spotify.music",
    "chrome": "com.android.chrome",
    "calculator": "com.android.calculator2",
    "notepad": "com.example.notepad",
    "word": "com.microsoft.office.word",
    "excel": "com.microsoft.office.excel",
    "powerpoint": "com.microsoft.office.powerpoint",
    "edge": "com.microsoft.emmx",
    "github": "com.github.android",
    "android studio": "com.google.android.studio"
}

def TranslateAndroidCommand(commands):
    """
    Enhanced Android command translator that handles intelligent command formats
    """
    if isinstance(commands, str):
        commands = [commands]

    processed_commands = []
    
    for command in commands:
        cmd = command.lower().strip()
        processed_cmd = process_android_command(cmd)
        if processed_cmd:
            processed_commands.append(processed_cmd)
            print(f"[ANDROID] Processed command: {processed_cmd}")

    return processed_commands

def process_android_command(cmd):
    """Process individual Android command with intelligent parsing"""
    
    # Core Commands
    if cmd.startswith("core_"):
        return handle_core_command(cmd)
    
    # App Commands
    elif cmd.startswith("app_"):
        return handle_app_command(cmd)
    
    # Media Commands
    elif cmd.startswith("media_"):
        return handle_media_command(cmd)
    
    # Communication Commands
    elif cmd.startswith("comms_"):
        return handle_comms_command(cmd)
    
    # Device Commands
    elif cmd.startswith("device_"):
        return handle_device_command(cmd)
    
    # Smart Commands
    elif cmd.startswith("smart_"):
        return handle_smart_command(cmd)
    
    # Legacy format support
    else:
        return handle_legacy_command(cmd)

def handle_core_command(cmd):
    """Handle core system commands"""
    if "activate" in cmd:
        return "core::activate"
    elif "stop_service" in cmd:
        return "core::stop_service"
    elif "name" in cmd:
        return "core::name"
    elif "health" in cmd:
        return "core::health"
    elif "version" in cmd:
        return "core::version"
    elif "joke" in cmd:
        return "core::joke"
    elif "date" in cmd:
        return "core::date"
    elif "time" in cmd:
        return "core::time"
    return None

def handle_app_command(cmd):
    """Handle app-related commands"""
    if "open" in cmd:
        # Extract app name from command
        app_name = extract_app_name_from_command(cmd)
        if app_name:
            return f"app::open::{app_name}"
    elif "start" in cmd:
        app_name = extract_app_name_from_command(cmd)
        if app_name:
            return f"app::start::{app_name}"
    elif "delete" in cmd:
        app_name = extract_app_name_from_command(cmd)
        if app_name:
            return f"app::delete::{app_name}"
    elif "lock" in cmd:
        app_name = extract_app_name_from_command(cmd)
        if app_name:
            return f"app::lock::{app_name}"
    elif "unlock" in cmd:
        app_name = extract_app_name_from_command(cmd)
        if app_name:
            return f"app::unlock::{app_name}"
    return None

def handle_media_command(cmd):
    """Handle media-related commands"""
    if "capture_photo" in cmd:
        return "media::capture_photo"
    elif "screenshot" in cmd:
        return "media::screenshot"
    elif "record_video" in cmd:
        return "media::record_video"
    elif "change_camera" in cmd:
        return "media::change_camera"
    elif "skip_5sec" in cmd:
        return "media::skip_5sec"
    elif "play_song" in cmd:
        song_name = extract_parameter_from_command(cmd)
        return f"media::play_song::{song_name}" if song_name else "media::play_song"
    elif "play_spotify" in cmd:
        return "media::play_spotify"
    elif "change_song" in cmd:
        return "media::change_song"
    elif "stop_recording" in cmd:
        return "media::stop_recording"
    return None

def handle_comms_command(cmd):
    """Handle communication commands"""
    if "call" in cmd:
        contact = extract_parameter_from_command(cmd)
        return f"comms::call::{contact}" if contact else "comms::call"
    elif "video_call" in cmd:
        contact = extract_parameter_from_command(cmd)
        return f"comms::video_call::{contact}" if contact else "comms::video_call"
    elif "whatsapp" in cmd:
        message = extract_parameter_from_command(cmd)
        return f"comms::whatsapp::{message}" if message else "comms::whatsapp"
    elif "sms" in cmd:
        message = extract_parameter_from_command(cmd)
        return f"comms::sms::{message}" if message else "comms::sms"
    return None

def handle_device_command(cmd):
    """Handle device control commands with percentage support"""
    if "battery" in cmd:
        return "device::battery"
    elif "flashlight_on" in cmd:
        return "device::flashlight_on"
    elif "flashlight_off" in cmd:
        return "device::flashlight_off"
    elif "screen_on" in cmd:
        return "device::screen_on"
    elif "screen_off" in cmd:
        return "device::screen_off"
    elif "home" in cmd:
        return "device::home"
    elif "brightness" in cmd:
        # Extract percentage from command
        percentage = extract_percentage_from_command(cmd)
        return f"device::brightness::{percentage}%" if percentage else "device::brightness::50%"
    elif "reminder" in cmd:
        reminder_text = extract_parameter_from_command(cmd)
        return f"device::reminder::{reminder_text}" if reminder_text else "device::reminder"
    elif "alarm" in cmd:
        alarm_text = extract_parameter_from_command(cmd)
        return f"device::alarm::{alarm_text}" if alarm_text else "device::alarm"
    elif "water_ejection" in cmd:
        return "device::water_ejection"
    elif "silent_on" in cmd:
        return "device::silent_on"
    elif "silent_off" in cmd:
        return "device::silent_off"
    elif "wifi_on" in cmd:
        return "device::wifi_on"
    elif "wifi_off" in cmd:
        return "device::wifi_off"
    elif "wifi_connect" in cmd:
        return "device::wifi_connect"
    elif "wifi_disconnect" in cmd:
        return "device::wifi_disconnect"
    elif "bluetooth_on" in cmd:
        return "device::bluetooth_on"
    elif "bluetooth_off" in cmd:
        return "device::bluetooth_off"
    elif "mobile_data_on" in cmd:
        return "device::mobile_data_on"
    elif "mobile_data_off" in cmd:
        return "device::mobile_data_off"
    elif "scroll_up" in cmd:
        return "device::scroll_up"
    elif "scroll_down" in cmd:
        return "device::scroll_down"
    elif "scroll_left" in cmd:
        return "device::scroll_left"
    elif "scroll_right" in cmd:
        return "device::scroll_right"
    return None

def handle_smart_command(cmd):
    """Handle smart/ai commands"""
    if "news" in cmd:
        return "smart::news"
    elif "weather" in cmd:
        return "smart::weather"
    elif "location" in cmd:
        return "smart::location"
    elif "track_location" in cmd:
        person = extract_parameter_from_command(cmd)
        return f"smart::track_location::{person}" if person else "smart::track_location"
    elif "translate" in cmd:
        return "smart::translate"
    elif "emergency" in cmd:
        return "smart::emergency"
    elif "search" in cmd:
        query = extract_parameter_from_command(cmd)
        return f"smart::search::{query}" if query else "smart::search"
    elif "object_detection" in cmd:
        return "smart::object_detection"
    elif "scan_text" in cmd:
        return "smart::scan_text"
    elif "read_notification" in cmd:
        return "smart::read_notification"
    elif "wikipedia" in cmd:
        topic = extract_parameter_from_command(cmd)
        return f"smart::wikipedia::{topic}" if topic else "smart::wikipedia"
    return None

def handle_legacy_command(cmd):
    """Handle legacy command format for backward compatibility"""
    if cmd.startswith("open "):
        app = cmd.removeprefix("open ").strip()
        if app in SUPPORTED_APPS:
            return f"app::open::{app}"
        else:
            print(f"[ANDROID OPEN] App '{app}' not supported.")
            return None

    elif cmd.startswith("play "):
        query = cmd.removeprefix("play ").strip()
        return f"media::play_song::{query}"

    elif cmd.startswith("volume::"):
        # Handle volume commands with percentage
        parts = cmd.split("::")
        if len(parts) >= 3:
            direction = parts[1]
            percentage = parts[2]
            return f"device::volume::{direction}::{percentage}"
        return None

    else:
        print(f"[ANDROID] Command not handled: {cmd}")
        return None

def extract_app_name_from_command(cmd):
    """Extract app name from command string"""
    # Remove command prefix and extract app name
    prefixes = ["app_open::", "app_start::", "app_delete::", "app_lock::", "app_unlock::"]
    for prefix in prefixes:
        if cmd.startswith(prefix):
            return cmd[len(prefix):].strip()
    return None

def extract_parameter_from_command(cmd):
    """Extract parameter from command string"""
    # Find the last :: and extract everything after it
    if "::" in cmd:
        return cmd.split("::")[-1].strip()
    return None

def extract_percentage_from_command(cmd):
    """Extract percentage value from command string"""
    import re
    percentage_pattern = r'(\d+)\s*%'
    matches = re.findall(percentage_pattern, cmd)
    return int(matches[0]) if matches else None

def human_friendly_responses(device_tasks: dict) -> str:
    """Generate human-friendly responses for device tasks"""
    responses = []
    
    if "android" in device_tasks and device_tasks["android"]:
        android_cmds = device_tasks['android']
        cmd_descriptions = []
        
        for cmd in android_cmds:
            if cmd.startswith("app::open::"):
                app = cmd.split("::")[-1]
                cmd_descriptions.append(f"open {app}")
            elif cmd.startswith("media::play_song::"):
                song = cmd.split("::")[-1]
                cmd_descriptions.append(f"play {song}")
            elif cmd.startswith("device::brightness::"):
                level = cmd.split("::")[-1]
                cmd_descriptions.append(f"set brightness to {level}")
            elif cmd.startswith("device::volume::"):
                parts = cmd.split("::")
                direction = parts[2]
                level = parts[3]
                cmd_descriptions.append(f"turn volume {direction} to {level}")
            else:
                cmd_descriptions.append(cmd.replace("::", " "))
        
        responses.append(f"On your phone, I'll: {', '.join(cmd_descriptions)}.")

    if "pc" in device_tasks and device_tasks["pc"]:
        pc_cmds = ', '.join([cmd for cmd in device_tasks['pc']])
        responses.append(f"On your computer: {pc_cmds}.")

    if not responses:
        responses.append("No valid tasks were found for your devices.")

    return " ".join(responses)

# ==================== TESTING ====================

if __name__ == "__main__":
    print("🤖 Android Automation Testing")
    print("=" * 40)
    
    test_commands = [
        "app_open::whatsapp",
        "media_play_song::despacito",
        "device_brightness::75%",
        "device_volume::down::30%",
        "comms_call::mom",
        "smart_search::python tutorials",
        "open chrome",  # Legacy format
        "play despacito"  # Legacy format
    ]
    
    for cmd in test_commands:
        print(f"\n🔍 Command: {cmd}")
        result = process_android_command(cmd)
        print(f"📤 Result: {result}")
        print("-" * 30)
