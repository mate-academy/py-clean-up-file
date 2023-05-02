from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self, exc_type: None, exc_value: None, exc_traceback: None
    ):
        remove(self.filename)
