from __future__ import annotations
from typing import Any

from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: object, exc_val: Any, exc_tb: Any) -> None:
        if self.filename:
            remove(self.filename)
