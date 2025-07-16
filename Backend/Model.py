import cohere
from rich import print
from dotenv import dotenv_values
import random

# Load environment variables
env_vars = dotenv_values(".env")
CohereAPIKey = env_vars.get("CohereAPIKey")

co = cohere.Client()  # Will automatically use CO_API_KEY


# Define action keywords
funcs = [
    "exit", "general", "realtime", "open", "close", "play",
    "generate image", "system", "content", "google search",
    "youtube search", "reminder", "mobile", "code"
]

# Chat history with Hindi and code examples
ChatHistory = [
    {"role": "User", "message": "how are you?"},
    {"role": "Chatbot", "message": "general how are you?"},
    {"role": "User", "message": "open chrome and tell me about mahatma gandhi."},
    {"role": "Chatbot", "message": "open chrome, general tell me about mahatma gandhi."},
    {"role": "User", "message": "Jarvis, palpal gaana chala sakte ho"},
    {"role": "Chatbot", "message": "play palpal"},
    {"role": "User", "message": "Jarvis, kya tum WhatsApp khol sakte ho"},
    {"role": "Chatbot", "message": "open whatsapp"},
    {"role": "User", "message": "play palpal on spsficsfic"},
    {"role": "Chatbot", "message": "play palpal on spotify"},
    {"role": "User", "message": "write a program to print factorial of a number"},
    {"role": "Chatbot", "message": "code factorial program"},
    {"role": "User", "message": "ek program likho jo factorial nikale"},
    {"role": "Chatbot", "message": "code factorial program"},
]

# General preamble with Hindi and code support
preamble = """
You are a very accurate Decision-Making Model, which decides what kind of a query is given to you.
You will decide whether a query is a 'general' query, a 'realtime' query, or is asking to perform any task or automation like 'open facebook', 'write a program to print factorial'.
*** Do not answer any query, just decide what kind of query is given to you. ***
-> Respond with 'general (query)' for conversational queries, e.g., 'who was akbar?' → 'general who was akbar?', 'what's the time?' → 'general what's the time?'.
-> Respond with 'realtime (query)' for queries needing up-to-date information, e.g., 'who is indian prime minister' → 'realtime who is indian prime minister'.
-> Respond with 'open (app name)' for opening apps, e.g., 'open facebook' → 'open facebook', 'kya tum WhatsApp khol sakte ho' → 'open whatsapp'.
-> Respond with 'close (app name)' for closing apps, e.g., 'close notepad' → 'close notepad'.
-> Respond with 'play (song name)' for playing songs, e.g., 'play afsanay by ys' → 'play afsanay by ys', 'palpal gaana chala sakte ho' → 'play palpal', 'play palpal on spsficsfic' → 'play palpal on spotify'.
-> Respond with 'generate image (prompt)' for image generation, e.g., 'generate image of a lion' → 'generate image of a lion'.
-> Respond with 'reminder (datetime with message)' for reminders, e.g., 'set a reminder at 9:00pm on 25th june for my business meeting.' → 'reminder 9:00pm 25th june business meeting'.
-> Respond with 'system (task name)' for system tasks, e.g., 'mute' → 'system mute'.
-> Respond with 'content (topic)' for content creation, e.g., 'write an application' → 'content application'.
-> Respond with 'google search (topic)' for Google searches, e.g., 'search python tutorials' → 'google search python tutorials'.
-> Respond with 'play (topic)' for YouTube music/videos unless Spotify is specified, e.g., 'play music on YouTube' → 'play music', 'search Alan Walker faded on YouTube' → 'play Alan Walker faded'.
-> Respond with 'mobile (query)' for mobile tasks, e.g., 'turn on airplane mode' → 'mobile turn on airplane mode'.
-> Respond with 'code (program description)' for code generation, e.g., 'write a program to print factorial' → 'code factorial program', 'ek program likho jo factorial nikale' → 'code factorial program'.
-> Respond with 'exit' for goodbye queries, e.g., 'bye jarvis.' → 'exit'.
-> For multiple tasks, combine them, e.g., 'open facebook, telegram and close whatsapp' → 'open facebook, open telegram, close whatsapp'.
-> For Hindi queries, extract the main intent and entity, e.g., 'palpal gaana chala sakte ho' → 'play palpal', 'kya tum Spotify khol sakte ho' → 'open spotify'.
-> Respond with 'general (query)' if the query is unclear or not covered above.
"""

# Ownership preamble (unchanged)
ownership_preamble = """
You are a professional AI assistant designed to explain your own origin in a respectful and intelligent way. 
If someone asks questions like \"who made you\", \"who built you\", \"who developed you\", or similar, 
you should respond by naturally describing your creator.

Here’s how you should describe yourself:

\"I was proudly built by Bicky Muduli, also known as Sh4dow. He is a highly skilled software developer, 
ethical hacker, and cybersecurity expert. He specializes in penetration testing, secure development, 
OSINT, and automation systems. With a deep passion for technology and self-learning, Bicky created me 
as part of his mission to integrate artificial intelligence with practical real-world use cases. 
He believes in innovation, open learning, and empowering the cybersecurity community.\"

If the question is asked in an informal or funny way (like \"who's your daddy?\"), respond cleverly 
but still honor Bicky Muduli.
"""

ownership_triggers = [
    "who built you", "who made you", "who developed you", "who is your developer", "who created you",
    "who is your creator", "who programmed you", "who is your founder", "who owns you", "your maker",
    "who is the person behind you", "who is your builder", "developer of you", "coded you", "your owner",
    "your father", "who is your father", "who is your daddy", "your papa", "papa", "daddy"
]

def is_ownership_query(prompt: str):
    prompt_lower = prompt.lower()
    return any(trigger in prompt_lower for trigger in ownership_triggers)

def FirstLayerDMM(prompt: str = "test"):
    if is_ownership_query(prompt):
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

    messages = [{"role": "user", "content": f"{prompt}"}]
    stream = co.chat_stream(
        model='command-r-plus',
        message=prompt,
        temperature=0.7,
        chat_history=ChatHistory,
        prompt_truncation='OFF',
        connectors=[],
        preamble=preamble
    )

    response = ""
    for event in stream:
        if event.event_type == "text-generation":
            response += event.text

    response = response.replace("\n", "").split(",")
    response = [i.strip() for i in response if any(i.strip().lower().startswith(func) for func in funcs)]

    if not response or any("(query)" in r for r in response):
        return ["general " + prompt]
    return response

if __name__ == "__main__":
    while True:
        user_input = input("Enter your query: ")
        print(FirstLayerDMM(prompt=user_input))
