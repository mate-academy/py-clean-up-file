from __future__ import annotations
from traceback import TracebackException
from types import TracebackType
from typing import Optional
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: Optional[Exception],
            exc_val: Optional[TracebackException],
            exc_tb: Optional[TracebackType]) -> None:
        self.file.close()
        os.remove(self.filename)
