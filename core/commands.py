from core.speech import speak

from features.assistant import set_name
from features.browser import (
    google_search,
    open_google,
    open_youtube,
)
from features.media import (
    play_music,
    tell_joke,
)
from features.knowledge import search_wikipedia
from features.apps import open_application
from features.system import (
    mute,
    restart,
    shutdown,
    take_screenshot,
    tell_date,
    tell_time,
    volume_down,
    volume_up,
)


def process_command(query: str) -> bool:
    """
    Processes a command.

    Returns True when Jarvis should exit.
    """

    if "time" in query:
        tell_time()

    elif "date" in query:
        tell_date()

    elif "wikipedia" in query:
        search_query = query.replace(
            "wikipedia",
            ""
        ).strip()

        search_wikipedia(search_query)

    elif "play music" in query:
        song_name = query.replace(
            "play music",
            ""
        ).strip()

        play_music(song_name)

    elif "volume up" in query:
        volume_up()

    elif "volume down" in query:
        volume_down()

    elif "mute" in query:
        mute()

    elif "open youtube" in query:
        open_youtube()

    elif "open google" in query:
        open_google()

    elif "change your name" in query:
        set_name()

    elif "screenshot" in query:
        take_screenshot()

    elif "tell me a joke" in query:
        tell_joke()

    elif query.startswith("search for"):
        search_query = query.replace(
            "search for",
            "",
            1
        ).strip()

        google_search(search_query)

    elif query.startswith("google"):
        search_query = query.replace(
            "google",
            "",
            1
        ).strip()

        google_search(search_query)

    elif "shutdown" in query:
        shutdown()
        return True

    elif "restart" in query:
        restart()
        return True

    elif "offline" in query or "exit" in query:
        speak("Going offline. Have a good day!")
        return True

    elif query.startswith("open"):
        app = query.replace(
            "open",
            "",
            1
        ).strip()

        opened = open_application(app)

        if not opened:
            speak(
                f"I don't know how to open {app} yet."
            )

    else:
        speak(
            "Sorry, I don't know how to handle that command."
        )

    return False