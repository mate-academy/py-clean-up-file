from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> bool:
        if self.file:
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)

        return False
