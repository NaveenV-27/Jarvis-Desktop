import platform

import psutil

from core.speech import speak


def system_status() -> None:
    """Report current CPU, RAM, and battery usage."""

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    message = (
        f"CPU usage is {cpu:.0f} percent. "
        f"Memory usage is {memory:.0f} percent."
    )

    if battery:
        message += (
            f" Battery is at "
            f"{battery.percent:.0f} percent."
        )

        if battery.power_plugged:
            message += " The computer is charging."

    print(message)
    speak(message)


def computer_info() -> None:
    """Report basic operating system information."""

    message = (
        f"You are running "
        f"{platform.system()} "
        f"{platform.release()} "
        f"on a {platform.machine()} machine."
    )

    print(message)
    speak(message)