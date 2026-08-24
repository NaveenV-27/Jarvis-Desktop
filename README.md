# Jarvis - Python Voice Assistant

A simple voice-controlled desktop assistant built with Python.

Jarvis can listen to voice commands, respond using text-to-speech, perform Wikipedia searches, play music, tell jokes, take screenshots, and perform basic system operations.

## Features

- Voice recognition
- Text-to-speech responses
- Time and date information
- Wikipedia search
- Play music from the local Music directory
- Open YouTube
- Open Google
- Change the assistant's name
- Take screenshots
- Tell random jokes
- Shutdown the system
- Restart the system
- Exit/offline mode

## Technologies Used

- Python
- pyttsx3
- SpeechRecognition
- PyAudio
- Wikipedia
- PyAutoGUI
- PyJokes

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Install the required dependencies:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyautogui pyjokes pyaudio
```

## Running the Project

Run the Python file:

```bash
python main.py
```

Jarvis will greet you and start listening for commands.

## Example Commands

You can try commands such as:

- "What is the time?"
- "Tell me the date"
- "Search Wikipedia for Python"
- "Play music"
- "Open YouTube"
- "Open Google"
- "Change your name"
- "Take a screenshot"
- "Tell me a joke"
- "Shutdown"
- "Restart"
- "Exit"

## Project Structure

```text
Jarvis/
│
├── main.py
├── assistant_name.txt
└── README.md
```

## How It Works

The application follows a simple flow:

```text
User Speech
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
Execute Action
     ↓
Text-to-Speech Response
```

The assistant uses Google's speech recognition service to convert voice input into text and `pyttsx3` to generate spoken responses.

## Notes

- The project is currently designed primarily for Windows.
- Music is played from the user's default Music directory.
- Screenshots are saved in the Pictures directory.
- Shutdown and restart commands immediately execute system commands, so use them carefully.
- The text-to-speech engine is initialized for each `speak()` call to ensure reliable speech output.

## Future Improvements

- Better project architecture
- Modular command system
- Application launching
- Google and YouTube search
- Weather information
- Reminders and alarms
- System information
- Volume control
- AI-powered command understanding
- Tool/function calling
- Conversational memory

## License

This project is open-source and available for learning and personal use.