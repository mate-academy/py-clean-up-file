from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' has been removed.")
        else:
            print(f"File '{self.filename}' does not exist.")
