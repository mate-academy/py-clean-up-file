import os
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        os.remove(self.filename)
