import os
from typing import Optional
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str = "file.txt") -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional,
            exc_val: Optional,
            exc_tb: TracebackType
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
