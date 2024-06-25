from __future__ import annotations

from typing import Any

from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = "w"

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        remove(self.filename)
