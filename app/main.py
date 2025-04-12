import os
from os import path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self, mode: str = "w") -> object:
        self.file = open(self.filename, mode)
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()
        path.exists(self.filename)
        os.remove(self.filename)
