import os
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> isinstance:
        return self

    def __exit__(self, exc_type: type[BaseException],
                 exc_value: BaseException,
                 traceback: TracebackType) -> None:
        os.remove(self.filename)
