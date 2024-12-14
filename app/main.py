from __future__ import annotations
from os import path, remove
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[Any]) -> None:
        if path.exists(self.filename):
            remove(self.filename)
