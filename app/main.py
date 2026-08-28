import os
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Self:
        try:
            self.file = open(self.filename, "r")
            return self
        except FileNotFoundError:
            self.file = open(self.filename, "w")
            return self

    def __exit__(self, *args, **kwargs) -> None:
        os.remove(self.filename)
