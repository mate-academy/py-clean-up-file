from __future__ import annotations
from os.path import exists
from os import remove


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, *_) -> None:
        if exists(self.filename):
            remove(self.filename)
