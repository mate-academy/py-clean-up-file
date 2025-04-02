from __future__ import annotations
import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        with open(self.filename, "w") as self.file:
            return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()
        os.remove(self.filename)
