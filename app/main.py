import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        print(f"Opening file {self.filename}")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        print(f"Closing file {self.filename}")

    def __del__(self) -> None:
        print(f"Deleting file {self.filename}")
        if os.path.exists(self.filename):
            os.remove(self.filename)
