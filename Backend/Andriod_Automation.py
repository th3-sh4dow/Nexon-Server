# ======================== Android_Automation.py ========================

SUPPORTED_APPS = {
    "whatsapp": "com.whatsapp",
    "chrome": "com.android.chrome",
    "youtube": "com.google.android.youtube",
    "gmail": "com.google.android.gm",
    "settings": "com.android.settings",
    "camera": "com.android.camera",
    "spotify": "com.spotify.music"
}

def TranslateAndroidCommand(commands):
    if isinstance(commands, str):
        commands = [commands]

    for command in commands:
        cmd = command.lower().strip()

        if cmd.startswith("open "):
            app = cmd.removeprefix("open ").strip()
            if app in SUPPORTED_APPS:
                print(f"[ANDROID OPEN] Trying to open app: {app}")
            else:
                print(f"[ANDROID OPEN] App '{app}' not supported.")

        elif cmd.startswith("play "):
            query = cmd.removeprefix("play ").strip()
            print(f"[ANDROID PLAY] Playing: {query}")

        else:
            print(f"[ANDROID] Command not handled: {cmd}")

def human_friendly_responses(device_tasks: dict) -> str:
    responses = []
    if "android" in device_tasks:
        android_cmds = ', '.join([cmd for cmd in device_tasks['android']])
        responses.append(f"On your phone, I'll handle these: {android_cmds}.")

    if "pc" in device_tasks:
        pc_cmds = ', '.join([cmd for cmd in device_tasks['pc']])
        responses.append(f"On your computer, the tasks will be: {pc_cmds}.")

    if not responses:
        responses.append("No valid tasks were found for your devices.")

    return " ".join(responses)
