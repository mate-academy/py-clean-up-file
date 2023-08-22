from os import remove
from typing import Any


class CleanUpFile:
    def __init__(
            self,
            filename: str
    ) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()
        try:
            remove(self.filename)
        except FileNotFoundError:
            pass
