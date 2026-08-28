from __future__ import annotations
from types import TracebackType
from typing import Optional, Type
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[Type[BaseException]],
            exc_tb: Optional[TracebackType]
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
