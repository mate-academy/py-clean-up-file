from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_typ: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        os.remove(self.filename)
