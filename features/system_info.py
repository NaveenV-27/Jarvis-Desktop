import platform

import psutil

from core.speech import speak


def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)


def get_memory_usage() -> float:
    return psutil.virtual_memory().percent


def get_battery_status() -> str:
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is unavailable."

    percentage = round(battery.percent)

    if battery.power_plugged:
        return f"Battery is at {percentage} percent and charging."

    return f"Battery is at {percentage} percent."


def system_status() -> None:
    """Reports basic system status."""

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    battery = get_battery_status()

    message = (
        f"CPU usage is {cpu} percent. "
        f"Memory usage is {memory} percent. "
        f"{battery}"
    )

    print(message)
    speak(message)


def computer_info() -> None:
    """Reports basic computer information."""

    system = platform.system()
    release = platform.release()
    machine = platform.machine()

    message = (
        f"You are running {system} {release} "
        f"on a {machine} machine."
    )

    print(message)
    speak(message)