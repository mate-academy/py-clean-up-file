import os
from typing import Any


class CleanUpFile:

    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
