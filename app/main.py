from os import remove
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None:
        self.file.close()
        remove(self.filename)
