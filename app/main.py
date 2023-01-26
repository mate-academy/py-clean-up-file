import os
from typing import Any


class CleanUpFile:
    def __init__(self, fn: str, mode: str = "w") -> None:
        self.filename = fn
        self.mode = mode

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        os.remove(f"./{self.filename}")
