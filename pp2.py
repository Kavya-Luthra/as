import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Print all available voices (optional, to choose one)
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Lang: {voice.languages}")
    print(f" - Gender: {voice.gender}\n")

# Set a specific voice (e.g., male or female)
engine.setProperty('voice', voices[1].id)  # You can try 0 or 1 (usually 0 = male, 1 = female on Windows)

# Speak
engine.say("Hello, this is a different voice.")
engine.runAndWait()
