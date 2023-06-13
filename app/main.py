import os
from typing import Callable


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: Callable,
                 exc_val: Exception,
                 exc_tb: Callable) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
