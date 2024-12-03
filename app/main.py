from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> bool:
        try:
            with open(self.filename, "r"):
                pass
            os.remove(self.filename)
        except FileNotFoundError:
            pass
        return False
