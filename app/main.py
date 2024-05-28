from __future__ import annotations
from types import TracebackType
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: TypeError,
            exc_val: ValueError,
            exc_tb: TracebackType
    ) -> None:
        os.remove(self.filename)
