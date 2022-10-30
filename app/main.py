from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.name = filename
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        if os.path.exists(self.name):
            os.remove(self.name)
        else:
            print("The file does not exist")
