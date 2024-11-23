import os.path
from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        if os.path.exists(self.filename):
            remove(self.filename)