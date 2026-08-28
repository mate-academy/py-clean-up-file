from __future__ import annotations

import os
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
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType]
    ) -> Optional[bool]:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            return
