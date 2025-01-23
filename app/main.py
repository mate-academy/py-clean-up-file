import os
from traceback import TracebackException
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: Exception,
                 exc_val: TracebackException, exc_tb: TracebackType) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
