import os
from pathlib import Path

from core.speech import speak


SPECIAL_FOLDERS = {
    "downloads": Path.home() / "Downloads",
    "download": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "document": Path.home() / "Documents",
    "pictures": Path.home() / "Pictures",
    "picture": Path.home() / "Pictures",
    "music": Path.home() / "Music",
    "desktop": Path.home() / "Desktop",
}


def open_folder(folder_name: str) -> bool:
    """Open a known Windows folder."""

    folder_name = folder_name.lower().strip()
    folder = SPECIAL_FOLDERS.get(folder_name)

    if folder is None or not folder.exists():
        return False

    speak(f"Opening your {folder_name} folder.")

    os.startfile(str(folder))

    return True


def create_folder(folder_name: str) -> bool:
    """Create a folder on the Desktop."""

    folder_name = folder_name.strip()

    if not folder_name:
        return False

    folder = Path.home() / "Desktop" / folder_name

    if folder.exists():
        speak(f"The folder {folder_name} already exists.")
        return False

    folder.mkdir(parents=True)

    speak(f"Created a folder called {folder_name}.")
    return True


def find_file(filename: str) -> list[Path]:
    """Search common user directories for a file."""

    filename = filename.lower().strip()

    search_locations = [
        Path.home() / "Desktop",
        Path.home() / "Documents",
        Path.home() / "Downloads",
        Path.home() / "Pictures",
    ]

    matches = []

    for location in search_locations:

        if not location.exists():
            continue

        try:
            for path in location.rglob("*"):

                if path.is_file() and filename in path.name.lower():
                    matches.append(path)

        except PermissionError:
            continue

    return matches