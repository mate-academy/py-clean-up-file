from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exc_type: Any, exc_value: Any, exc_traceback: Any) -> None:
        if not self.filename:
            return
        try:
            open(self.filename, "r")
        except FileNotFoundError:
            return
        else:
            os.remove(self.filename)
