import webbrowser as wb

from urllib.parse import quote_plus

from core.speech import speak


def open_youtube() -> None:
    speak("Opening YouTube")

    wb.open("https://youtube.com")


def open_google() -> None:
    speak("Opening Google")

    wb.open("https://google.com")


def google_search(query: str) -> None:
    """Searches Google."""

    if not query:
        speak("What would you like me to search for?")
        return

    search_url = (
        f"https://www.google.com/search?q="
        f"{quote_plus(query)}"
    )

    speak(f"Searching Google for {query}")

    wb.open(search_url)