from __future__ import annotations


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        del self
