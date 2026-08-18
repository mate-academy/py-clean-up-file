import os
from typing import TextIO


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> TextIO:
        self.handle = open(self.filename, "a")

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            self.handle.close()
            print(f"Delete file: {self.filename}")
        return False
