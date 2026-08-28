from __future__ import annotations

from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_obj = None

    def __enter__(self) -> object:
        self.file_obj = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: object,
            exc_val: object,
            exc_tb: object
    ) -> None:
        self.file_obj.close()
        remove(self.filename)
