# 🤖 Enhanced Nova AI - Intelligent Command Processing System

## 🚀 Overview

Enhanced Nova AI is a sophisticated artificial intelligence system that uses advanced NLP (Natural Language Processing) and NLU (Natural Language Understanding) to intelligently process user commands and translate them into structured actions for client devices.

## ✨ Key Features

### 🧠 Advanced NLP/NLU Capabilities
- **Intelligent Intent Recognition**: Understands user intent from natural language
- **Parameter Extraction**: Automatically extracts percentages, numbers, app names, and other parameters
- **Multi-language Support**: Handles English and Hindi commands
- **Context Awareness**: Understands complex multi-intent queries
- **Fuzzy Matching**: Handles typos and variations in app names

### 📱 Comprehensive Command Categories

#### 🎯 Core Commands
- `nova` - Activates Nova with acknowledgment
- `stop service` - Stops Nova background service
- `your name` - Speaks out Nova's name and version
- `how are you` - Responds to how it's feeling
- `current version` - Tells current version of Nova
- `joke` - Tells a joke
- `today's date` - Tells today's date
- `tell me the time` - Tells current time

#### 📱 App Commands
- `open [app name]` - Opens requested app
- `start [app name]` - Starts given app
- `delete [app name]` - Uninstalls app
- `lock [app name]` - Locks app
- `unlock [app name]` - Unlocks app

#### 🎵 Media Commands
- `capture photo` - Takes a photo with camera
- `take screenshot` - Takes a screenshot
- `record video` - Starts video recording
- `change camera` - Switches camera (front/back)
- `skip 5 sec` - Skips forward 5 sec in media
- `play song` - Starts playing a song
- `play spotify` - Opens Spotify & starts playing
- `change song` - Skips to next song
- `stop recording` - Stops video/screen recording

#### 📞 Communication Commands
- `call [contact]` - Makes a voice call
- `video call [contact]` - Starts a video call
- `send whatsapp [message]` - Sends WhatsApp message
- `send sms [message]` - Sends SMS

#### ⚙️ Device Commands (with Percentage Support)
- `battery percentage` - Speaks battery level
- `turn on/off flashlight` - Controls flashlight
- `turn on/off screen` - Controls screen
- `back to home` - Goes to home screen
- `set brightness [level]` - Adjusts brightness (supports percentages)
- `set reminder/alarm` - Sets reminder/alarm
- `remove water` - Water ejection feature
- `turn on/off silent` - Controls silent mode
- `turn on/off wi-fi/bluetooth/mobile data` - Controls connectivity
- `scroll up/down/left/right` - Controls scrolling

#### 🖥️ PC Commands
- `open [app] in pc` - Opens applications on PC
- `shutdown pc` - Shuts down computer
- `restart pc` - Restarts PC
- `lock pc` - Locks computer
- `volume up/down in pc` - Controls PC volume
- `mute/unmute pc` - Controls PC audio
- `minimize all` - Minimizes all windows
- `maximize window` - Maximizes window
- `close this window/page` - Closes active window/tab
- `copy/paste` - Clipboard operations
- `move upward/downward` - Scrolls up/down
- `turn on sleeping mode on pc` - Puts PC to sleep
- `capture photo in laptop` - Takes photo from laptop camera
- `record in laptop` - Starts recording from laptop
- `click on [element]` - Clicks on element
- `type [text]` - Types text
- `send file to pc` - Transfers file

#### 🧠 Smart Commands
- `today's news` - Reads latest news
- `weather report` - Tells weather
- `current location` - Speaks GPS location
- `show me location of [person]` - Tracks location of person
- `translate mode` - Activates translator
- `trouble` - Handles emergency
- `search [query]` - Performs web search
- `what is this` - Object detection
- `scan and explain` - Reads and explains text
- `new notification` - Reads latest notification
- `tell me about [topic]` - Fetches Wikipedia summary

## 🔢 Percentage and Number Support

The system intelligently handles percentage and number values:

### Volume Control
```bash
"volume down 30%" → device_volume::down::30%
"volume up 50%" → device_volume::up::50%
"volume down 15" → device_volume::down::15%
```

### Brightness Control
```bash
"set brightness 75%" → device_brightness::75%
"set brightness to 90%" → device_brightness::90%
"set brightness 25" → device_brightness::25%
```

## 🌐 Multi-language Support

### Hindi Commands
```bash
"nova volume kam karo 30%" → device_volume::down::30%
"whatsapp kholo" → app_open::whatsapp
"mummy ko call karo" → comms_call::mummy
"screenshot le lo" → media_screenshot
```

## 🔄 Complex Multi-intent Queries

The system can handle complex queries with multiple intents:

```bash
"nova volume down 25% and open whatsapp" → 
  [device_volume::down::25%, app_open::whatsapp]

"set brightness to 80% and take screenshot" → 
  [device_brightness::80%, media_screenshot]

"call mom and send whatsapp message hello" → 
  [comms_call::mom, comms_whatsapp::hello]

"shutdown pc and lock phone" → 
  [pc_shutdown, device_lock]
```

## 🏗️ System Architecture

### Core Components

1. **Model.py** - Main NLP/NLU processing engine
   - Intent recognition
   - Parameter extraction
   - Command categorization
   - Multi-language support

2. **Android_Automation.py** - Android device command processing
   - App management
   - Device control
   - Media operations
   - Communication handling

3. **PC_Automation.py** - PC automation command processing
   - Application launching
   - System control
   - Volume/brightness management
   - Window management

### Command Flow

```
User Input → Model.py → Intent Recognition → Parameter Extraction → 
Command Generation → Device-Specific Processing → Client Device Execution
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Installation

1. Clone the repository
2. Install dependencies
3. Set up environment variables in `.env` file
4. Run the demo

### Environment Variables

Create a `.env` file with:

```env
CohereAPIKey=your_cohere_api_key
GroqAPIKey=your_groq_api_key
YouTubeAPIKey=your_youtube_api_key
Username=YourName
Assistantname=Nova
```

### Running the Demo

```bash
# Interactive demo
python demo_enhanced_nova.py

# Auto demo
python demo_enhanced_nova.py --auto

# Comprehensive testing
python test_enhanced_model.py
```

## 🧪 Testing

### Interactive Testing
```bash
python demo_enhanced_nova.py
```

### Comprehensive Testing
```bash
python test_enhanced_model.py
```

### Example Commands to Try

```bash
# Basic commands
nova
volume down 30%
set brightness to 75%
open whatsapp

# Complex commands
nova volume down 25% and open whatsapp
set brightness to 80% and take screenshot
call mom and send whatsapp message hello

# Hindi commands
nova volume kam karo 30%
whatsapp kholo
mummy ko call karo

# PC commands
shutdown pc
open notepad in pc
volume up in pc
```

## 🔧 API Integration

### Flask Server Integration

The enhanced system integrates seamlessly with the existing Flask server:

```python
@app.route("/ask", methods=["POST"])
def ask_jarvis():
    data = request.get_json()
    query = data['query']
    device_id = data.get('device_id', None)
    
    # Enhanced processing
    final_output, device_action = asyncio.run(MainExecution(query, device_id))
    
    return jsonify({
        "tts_text": device_action.get("tts_text", final_output),
        "device_command": device_action.get("device_command", "")
    })
```

## 📊 Performance Features

- **Fast Processing**: Optimized NLP processing for real-time responses
- **Memory Efficient**: Minimal memory footprint
- **Scalable**: Can handle multiple concurrent requests
- **Reliable**: Robust error handling and fallback mechanisms

## 🔒 Security Features

- **Input Validation**: All user inputs are validated and sanitized
- **Command Filtering**: Malicious commands are filtered out
- **Rate Limiting**: Built-in rate limiting for API endpoints
- **Secure Communication**: Encrypted communication with client devices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Bicky Muduli (Sh4dow)** - Creator and lead developer
- **Cohere** - For advanced NLP capabilities
- **Groq** - For code generation features
- **SpaCy** - For natural language processing

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

---

**Enhanced Nova AI** - Making AI interaction more natural and intelligent! 🤖✨ 