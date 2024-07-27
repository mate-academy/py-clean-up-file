from __future__ import annotations
import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]] | None,
            exc_val: Optional[BaseException] | None,
            exc_tb: Optional[TracebackType] | None
    ) -> None:
        self.file.close()

    def __del__(self) -> None:
        if os.path.exists(self.filename):
            self.file.close()
            os.remove(self.filename)
