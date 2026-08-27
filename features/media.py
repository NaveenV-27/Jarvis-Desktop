import os
import random
from pathlib import Path

import pyjokes

from core.speech import speak


def play_music(song_name: str | None = None) -> None:
    """Plays music from the Music directory."""

    song_dir = Path.home() / "Music"

    if not song_dir.exists():
        speak("I could not find your Music folder.")
        return

    songs = list(song_dir.iterdir())

    songs = [
        song
        for song in songs
        if song.is_file()
    ]

    if song_name:
        songs = [
            song
            for song in songs
            if song_name.lower() in song.name.lower()
        ]

    if songs:
        song = random.choice(songs)

        os.startfile(str(song))

        speak(f"Playing {song.stem}")

    else:
        speak("No song found.")


def tell_joke() -> None:
    """Tells a random joke."""

    joke = pyjokes.get_joke()

    print(joke)
    speak(joke)