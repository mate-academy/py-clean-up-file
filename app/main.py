from __future__ import annotations

from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: str) -> None:
        remove(self.filename)
