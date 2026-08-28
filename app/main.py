import os

from typing import Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: Type, exc_val: Type, exc_tb: Type) -> None:
        os.remove(self.filename)
