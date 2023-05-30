from typing import TextIO, Any
from os import remove


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "r") -> None:
        self.mode = mode
        self.filename = filename
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        remove(self.filename)
