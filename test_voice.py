import pyttsx3
import time


def speak(text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")

    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)

    print(f"Speaking: {text}")

    engine.say(text)
    engine.runAndWait()

    engine.stop()


speak("Hello, this is the first message.")
time.sleep(1)

speak("This is the second message.")
time.sleep(1)

speak("This is the third message.")