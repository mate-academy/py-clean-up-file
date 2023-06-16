from __future__ import annotations
from typing import Any
from os import remove, path


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if path.exists(self.filename):
            remove(self.filename)
