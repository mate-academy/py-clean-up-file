from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __del__(self) -> None:
        remove(self.filename)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__del__()
