from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename = name
        self.file = open(name, "a")

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: str, value: str, traceback: str) -> None:
        self.file.close()
        remove(self.filename)
