from __future__ import annotations
from os import remove
from types import TracebackType
from typing import Type, Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(file=self.filename, mode="w")
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        self.file.close()
        remove(self.filename)
