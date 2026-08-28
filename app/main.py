import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "r") -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print("File not found")
