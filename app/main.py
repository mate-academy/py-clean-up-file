from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> annotations:
        return self

    def __exit__(self, exc_type: type, exc_val: int, exc_tb: str) -> None:
        remove(self.filename)
