import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, *args: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
