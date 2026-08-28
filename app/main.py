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
        exc_type: Optional[Type],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
