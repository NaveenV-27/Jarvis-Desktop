import pyttsx3


def speak(audio: str) -> None:
    """Converts text to speech."""

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    print(f"Speaking: {audio}")

    engine.say(str(audio))
    engine.runAndWait()
    engine.stop()