from core.speech import speak
from core.utils import remove_phrases

from features.apps import open_application
from features.assistant import set_name
from features.browser import (
    google_search,
    open_google,
    open_youtube,
    youtube_search,
)
from features.knowledge import search_wikipedia
from features.media import play_music, tell_joke
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
from features.system_info import (
    computer_info,
    system_status,
)

from features.files import (
    create_folder,
    find_file,
    open_folder,
)


def process_command(query: str) -> bool:
    """
    Process a recognized voice command.

    Returns True if Jarvis should exit.
    """

    # -------------------------
    # TIME
    # -------------------------

    if any(
        phrase in query
        for phrase in [
            "what time is it",
            "current time",
            "tell me the time",
            "time",
        ]
    ):
        tell_time()
        return False

    # -------------------------
    # DATE
    # -------------------------

    if any(
        phrase in query
        for phrase in [
            "what is the date",
            "what's the date",
            "today's date",
            "tell me the date",
            "date",
        ]
    ):
        tell_date()
        return False

    # -------------------------
    # WIKIPEDIA
    # -------------------------

    if "wikipedia" in query:

        search_query = remove_phrases(
            query,
            [
                "search wikipedia for",
                "search wikipedia",
                "wikipedia",
            ],
        )

        search_wikipedia(search_query)

        return False

    # -------------------------
    # MUSIC
    # -------------------------

    if "play music" in query:

        song_name = query.replace(
            "play music",
            "",
            1,
        ).strip()

        play_music(song_name or None)

        return False

    # -------------------------
    # VOLUME
    # -------------------------

    if "volume up" in query or "increase volume" in query:
        volume_up()
        return False

    if "volume down" in query or "decrease volume" in query:
        volume_down()
        return False

    if query == "mute" or "mute volume" in query:
        mute()
        return False

    # -------------------------
    # BROWSER
    # -------------------------

    if "open youtube" in query:
        open_youtube()
        return False

    if "open google" in query:
        open_google()
        return False

    if "youtube" in query and "search" in query:

        search_query = remove_phrases(
            query,
            [
                "search youtube for",
                "search youtube",
                "youtube",
            ],
        )

        youtube_search(search_query)

        return False

    if query.startswith("search for"):

        search_query = query.replace(
            "search for",
            "",
            1,
        ).strip()

        google_search(search_query)

        return False

    if query.startswith("google"):

        search_query = query.replace(
            "google",
            "",
            1,
        ).strip()

        google_search(search_query)

        return False

    # -------------------------
    # ASSISTANT
    # -------------------------

    if "change your name" in query:
        set_name()
        return False

    # -------------------------
    # SCREENSHOT
    # -------------------------

    if (
        "screenshot" in query
        or "take a screenshot" in query
    ):
        take_screenshot()
        return False

    # -------------------------
    # JOKE
    # -------------------------

    if (
        "tell me a joke" in query
        or query == "joke"
    ):
        tell_joke()
        return False

        # -------------------------
    # SYSTEM INFORMATION
    # -------------------------

    if any(
        phrase in query
        for phrase in [
            "system status",
            "system usage",
            "cpu usage",
            "ram usage",
            "memory usage",
            "how is my computer",
        ]
    ):
        system_status()
        return False

    if any(
        phrase in query
        for phrase in [
            "computer information",
            "computer specs",
            "system specs",
            "what computer am i using",
        ]
    ):
        computer_info()
        return False

    # -------------------------
    # SHUTDOWN
    # -------------------------

    if "shutdown" in query:

        shutdown()

        return True

    # -------------------------
    # RESTART
    # -------------------------

    if "restart" in query:

        restart()

        return True

    # -------------------------
    # EXIT
    # -------------------------

    if any(
        phrase in query
        for phrase in [
            "go offline",
            "offline",
            "exit",
            "quit",
            "goodbye",
        ]
    ):
        speak("Going offline. Have a good day!")

        return True

        # -------------------------
    # OPEN FOLDERS
    # -------------------------

    if query.startswith("open "):

        target = query.replace(
            "open ",
            "",
            1
        ).strip()

        if target in [
            "downloads",
            "download",
            "documents",
            "document",
            "pictures",
            "picture",
            "music",
            "desktop",
        ]:

            if open_folder(target):
                return False

    # -------------------------
    # CREATE FOLDER
    # -------------------------

    if (
        query.startswith("create a folder")
        or query.startswith("create folder")
        or query.startswith("make a folder")
    ):

        folder_name = query

        for phrase in [
            "create a folder called",
            "create a folder named",
            "create a folder",
            "create folder called",
            "create folder named",
            "create folder",
            "make a folder called",
            "make a folder named",
            "make a folder",
        ]:
            folder_name = folder_name.replace(
                phrase,
                "",
                1
            )

        folder_name = folder_name.strip()

        if not folder_name:
            speak("What should I call the folder?")
            return False

        create_folder(folder_name)

        return False

    # -------------------------
    # FIND FILE
    # -------------------------

    if (
        query.startswith("find ")
        or query.startswith("search for a file")
        or query.startswith("find a file")
    ):

        filename = query

        for phrase in [
            "search for a file",
            "find a file",
            "find",
        ]:
            filename = filename.replace(
                phrase,
                "",
                1
            )

        filename = filename.strip()

        if not filename:
            speak("What file should I look for?")
            return False

        matches = find_file(filename)

        if not matches:
            speak(f"I couldn't find a file matching {filename}.")
            return False

        if len(matches) == 1:
            speak(f"I found {matches[0].name}.")
            print(matches[0])
            return False

        speak(
            f"I found {len(matches)} files matching {filename}."
        )

        for match in matches[:10]:
            print(match)

        return False

    # -------------------------
    # APPLICATIONS
    # -------------------------

    if query.startswith("open "):

        app = query.replace(
            "open ",
            "",
            1,
        ).strip()

        if not open_application(app):
            speak(
                f"I don't know how to open {app} yet."
            )

        return False

    # -------------------------
    # UNKNOWN COMMAND
    # -------------------------

    speak(
        "I don't know how to handle that command yet."
    )

    return False