from __future__ import annotations
import os


class CleanUpFile():
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: str, exc_value: str, exc_tb: str) -> None:
        os.remove(self.filename)
