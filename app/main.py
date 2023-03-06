import os

from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self, exc_type: object, exc_val: object, exc_tb: object
    ) -> None:
        self.file.close()
        os.remove(self.filename)
