from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename = name
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        self.file.close()
        remove(self.filename)
