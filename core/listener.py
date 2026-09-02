import speech_recognition as sr

from core.speech import speak
from core.utils import normalize_command


def take_command() -> str | None:
    """Listen to microphone input and convert it to text."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.pause_threshold = 1

        try:
            audio = recognizer.listen(
                source,
                timeout=5
            )

        except sr.WaitTimeoutError:
            speak("Timeout occurred. Please try again.")
            return None

    try:
        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        query = normalize_command(query)

        print(f"You: {query}")

        return query

    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None

    except Exception as error:
        print(f"Speech recognition error: {error}")
        speak("An unexpected error occurred.")
        return None