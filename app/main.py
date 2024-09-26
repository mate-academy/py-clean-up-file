import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: object,
                 exc_value: object,
                 traceback: Any) -> None:
        os.remove(self.filename)
