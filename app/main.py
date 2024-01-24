from __future__ import annotations
from types import TracebackType
from os import remove


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        self.file = open(f"{self.filename}", "w")
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_val: Exception,
            exc_tb: TracebackType
    ) -> None:
        if hasattr(self, "file") and self.file:
            self.file.close()
            remove(f"{self.filename}")
