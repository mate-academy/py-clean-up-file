from typing import TextIO
from os import remove


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "r") -> None:
        self.mode = mode
        self.filename = filename
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()
        remove(self.filename)
