import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_val: Exception,
            exc_tb: TracebackType
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
