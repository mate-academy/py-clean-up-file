from __future__ import annotations

import os.path
from types import TracebackType


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_value: Exception,
            exc_traceback: TracebackType
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
