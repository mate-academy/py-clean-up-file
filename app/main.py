import os
from types import TracebackType
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Exception, exc_val: Exception,
                 exc_tb: TracebackType) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
