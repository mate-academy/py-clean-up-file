import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            print(f"File '{self.filename}' does not exist.")
        return False
