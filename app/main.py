from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: type, exc_val: int, exc_tb: str) -> None:
        remove(self.filename)
