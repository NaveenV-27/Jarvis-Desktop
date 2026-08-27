from pathlib import Path
import datetime

from core.speech import speak
from core.listener import take_command


BASE_DIR = Path(__file__).resolve().parent.parent
NAME_FILE = BASE_DIR / "assistant_name.txt"


def load_name() -> str:
    """Loads the assistant name."""

    try:
        return NAME_FILE.read_text().strip() or "Jarvis"

    except FileNotFoundError:
        return "Jarvis"


def set_name() -> None:
    """Changes the assistant's name."""

    speak("What would you like to name me?")

    name = take_command()

    if name:
        NAME_FILE.write_text(name)

        speak(
            f"Alright, I will be called {name} from now on."
        )

    else:
        speak("Sorry, I couldn't catch that.")


def wish_me() -> None:
    """Greets the user based on the current time."""

    speak("Welcome back, sir!")

    hour = datetime.datetime.now().hour

    if 4 <= hour < 12:
        greeting = "Good morning!"

    elif 12 <= hour < 16:
        greeting = "Good afternoon!"

    elif 16 <= hour < 24:
        greeting = "Good evening!"

    else:
        greeting = "Good night, see you tomorrow."

    speak(greeting)

    assistant_name = load_name()

    message = (
        f"{assistant_name} at your service. "
        "Please tell me how may I assist you."
    )

    speak(message)