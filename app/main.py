from __future__ import annotations

from os import remove
from os import path

from types import TracebackType
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Optional[type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        if path.exists(self.filename):
            remove(self.filename)
