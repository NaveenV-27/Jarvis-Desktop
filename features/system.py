import datetime
import os

import pyautogui
from pathlib import Path

from core.speech import speak


def tell_time() -> None:
    """Tells the current time."""

    current_time = datetime.datetime.now().strftime(
        "%I:%M:%S %p"
    )

    message = f"The current time is {current_time}"

    print(message)
    speak(message)


def tell_date() -> None:
    """Tells the current date."""

    now = datetime.datetime.now()

    message = (
        f"The current date is "
        f"{now.day} {now.strftime('%B')} {now.year}"
    )

    print(message)
    speak(message)


def take_screenshot() -> None:
    """Takes and saves a screenshot."""

    image = pyautogui.screenshot()

    screenshot_path = (
        Path.home()
        / "Pictures"
        / "screenshot.png"
    )

    image.save(screenshot_path)

    message = f"Screenshot saved as {screenshot_path}"

    print(message)
    speak(message)


def volume_up() -> None:
    """Increases system volume."""

    pyautogui.press(
        "volumeup",
        presses=5
    )


def volume_down() -> None:
    """Decreases system volume."""

    pyautogui.press(
        "volumedown",
        presses=5
    )


def mute() -> None:
    """Mutes or unmutes system volume."""

    pyautogui.press("volumemute")


def shutdown() -> None:
    """Shuts down the computer."""

    speak("Shutting down the system. Goodbye!")

    os.system(
        "shutdown /s /f /t 1"
    )


def restart() -> None:
    """Restarts the computer."""

    speak("Restarting the system. Please wait!")

    os.system(
        "shutdown /r /f /t 1"
    )