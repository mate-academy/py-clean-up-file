import os
from typing import Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: object,
                 exc_value: object,
                 traceback: Any) -> None:
        os.remove(self.filename)
