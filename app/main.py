import os
from typing import Any


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename = name
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename,  "w")
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self.file.close()
        os.remove(self.filename)
