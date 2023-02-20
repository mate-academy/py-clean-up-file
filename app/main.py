from __future__ import annotations

import os
from traceback import TracebackException
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 exc_type: Exception,
                 exc_value: TracebackException,
                 exc_tb: TracebackType) -> None:
        os.remove(self.filename)
