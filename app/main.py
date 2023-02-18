from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            type_of_error: type,
            value: str,
            traceback: str
    ) -> None:
        self.file.close()
        os.remove(self.filename)
