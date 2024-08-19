from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
