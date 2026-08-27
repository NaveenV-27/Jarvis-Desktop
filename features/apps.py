import os

from core.speech import speak


APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "explorer": "explorer.exe",
}


def open_application(app: str) -> bool:
    """
    Opens a supported application.

    Returns True if the application was found.
    """

    app = app.lower().strip()

    if app in APPS:
        speak(f"Opening {app}")

        os.system(
            f"start {APPS[app]}"
        )

        return True

    return False