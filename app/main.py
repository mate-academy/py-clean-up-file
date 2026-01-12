from os import remove
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_value: Any,
                 exc_traceback: Any) -> None:
        remove(self.filename)
