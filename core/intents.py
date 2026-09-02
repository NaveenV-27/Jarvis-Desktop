from dataclasses import dataclass
from typing import Callable


@dataclass
class Intent:
    name: str
    triggers: list[str]
    handler: Callable