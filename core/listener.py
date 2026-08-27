import speech_recognition as sr

from core.speech import speak


def take_command() -> str | None:
    """Listens to microphone input and converts it to text."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1

        try:
            audio = recognizer.listen(source, timeout=5)

        except sr.WaitTimeoutError:
            speak("Timeout occurred. Please try again.")
            return None

    try:
        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        print(f"You said: {query}")

        return query.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None

    except Exception as error:
        print(f"Error: {error}")
        speak("An unexpected error occurred.")
        return None