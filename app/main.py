import _io
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None


    def __enter__(self, mode: str = "w") -> _io.TextIOWrapper:
        self.file = open(self.filename, mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.filename)


