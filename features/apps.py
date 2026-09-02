import os

from core.speech import speak


APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "paint": "mspaint.exe",
    "explorer": "explorer.exe",
}


def open_application(app: str) -> bool:
    """Open a supported Windows application."""

    app = app.lower().strip()

    executable = APPS.get(app)

    if executable is None:
        return False

    speak(f"Opening {app}")

    os.system(f"start {executable}")

    return True


def list_supported_apps() -> list[str]:
    return list(APPS.keys())