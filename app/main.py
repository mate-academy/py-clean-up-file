from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "w") -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
