from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self, mode: str = "w") -> CleanUpFile:
        self.file = open(self.filename, mode)
        return self

    def __exit__(
            self,
            exc_type: object,
            exc_val: object,
            exc_tb: object
    ) -> None :
        self.file.close()
        os.remove(self.filename)
