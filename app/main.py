import os
from typing import Callable


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> Callable:
        return self

    def __exit__(self, exc_type: Callable,
                 exc_val: Callable, exc_tb: Callable) -> None:
        os.remove(self.filename)
