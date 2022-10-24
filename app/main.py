from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        if not os.path.isfile(self.filename):
            return self

    def __exit__(self, exc_type: None, exc_val: None,
                 exc_tb: str) -> None:
        os.remove(self.filename)
