from __future__ import annotations
from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: object,
            exc_val: object,
            exc_tb: object
    ) -> None:
        try:
            remove(self.filename)
        except FileNotFoundError:
            raise FileNotFoundError("The file does not exist")
