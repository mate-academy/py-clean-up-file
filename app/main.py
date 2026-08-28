from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: type, exc_val: str,
                 exc_tb: BaseException) -> None:
        self.file.close()
        os.remove(self.filename)
