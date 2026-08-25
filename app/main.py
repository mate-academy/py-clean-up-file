import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = "r"
        self.file = None

    def __enter__(self) -> Any:
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError as e:
            print(e)
            self.file = None
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        if self.file:
            self.file.close()
        os.remove(self.filename)
