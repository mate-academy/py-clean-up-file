from __future__ import annotations
from os import remove


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Exception,
                 exc_val: Exception,
                 exc_tb: Exception) -> None:
        if self.filename:
            remove(self.filename)
