from __future__ import annotations
import os

from typing import Optional, Type
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(f"{self.filename}", "w")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType]
    ) -> None:
        self.file.close()
        self.__delete__()

    def __delete__(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
