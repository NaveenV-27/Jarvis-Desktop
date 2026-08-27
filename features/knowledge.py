import wikipedia

from core.speech import speak


def search_wikipedia(query: str) -> None:
    """Searches Wikipedia."""

    if not query:
        speak("What would you like me to search for on Wikipedia?")
        return

    try:
        speak("Searching Wikipedia.")

        result = wikipedia.summary(
            query,
            sentences=2
        )

        print(result)
        speak(result)

    except wikipedia.exceptions.DisambiguationError:
        speak(
            "Multiple results were found. "
            "Please be more specific."
        )

    except wikipedia.exceptions.PageError:
        speak(
            "I couldn't find anything on Wikipedia."
        )

    except Exception as error:
        print(f"Wikipedia error: {error}")

        speak(
            "Something went wrong while searching Wikipedia."
        )