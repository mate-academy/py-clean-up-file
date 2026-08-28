from os.path import exists
from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, *_) -> None:
        if exists(self.filename):
            remove(self.filename)
