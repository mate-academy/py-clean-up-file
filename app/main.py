import os

from typing import TextIO, Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file: Optional[TextIO] = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        if self.file:
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
