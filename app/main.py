import os
from typing import Callable


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> Callable:
        return self

    def __exit__(self, exc_type: Callable,
                 exc_value: Callable,
                 exc_traceback: Callable) -> None:
        os.remove(self.filename)
