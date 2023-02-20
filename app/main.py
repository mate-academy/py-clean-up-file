from __future__ import annotations
from typing import Any
from os import remove


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        remove(self.filename)
