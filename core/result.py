from dataclasses import dataclass


@dataclass
class CommandResult:
    success: bool = True
    should_exit: bool = False
    message: str | None = None