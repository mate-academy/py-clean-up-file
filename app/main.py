import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        os.remove(self.filename)
        return True
